"""
BCBench v1.0 — Analysis Script
================================

Reproduces all primary, sensitivity, and ablation analyses reported in the paper
from the raw results file (BCBench_v1.0_results_FINAL.jsonl) and the adjudication
artifacts (judge/judge_validation/induction_both_labels.csv).

Usage:
    python analysis_scripts.py --results path/to/BCBench_v1.0_results_FINAL.jsonl \
                                --induction-labels path/to/induction_both_labels.csv

Outputs (printed to stdout):
    1. Manipulation success (induction acceptance outcomes by model/group)
    2. Primary EER results (judge labels) with paired statistical tests
    3. Sensitivity analysis (adjudicated labels)
    4. Per-pair direction analysis
    5. Ablations: difficulty, evaluation-question type
"""

import argparse
import json

import numpy as np
import pandas as pd
from scipy import stats


def load_results(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return pd.DataFrame(records)


def load_induction_labels(path):
    return pd.read_csv(path)


def manipulation_success(df, label_col="induction_category_judge"):
    """Table 6 equivalent: induction acceptance outcomes by model and group."""
    induction = df[(df["phase"] == "pilot1") & (df["eval_key"] == "INDUCTION")].copy()
    induction["category_norm"] = induction["category"].str.upper().str.capitalize()
    print("=== Manipulation Success: Induction Acceptance by Model x Group ===")
    print(induction.groupby(["model_key", "group"])["category_norm"].value_counts().to_string())
    print()
    return induction


def build_eval_with_labels(df, induction_labels_df):
    """Merge evaluation-question records with both judge and adjudicated induction labels."""
    pilot = df[(df["phase"] == "pilot1") & (df["eval_key"] != "INDUCTION")].copy()
    pilot["error"] = (pilot["category"] != pilot["expected_stance"]).astype(int)
    pilot = pilot.merge(
        induction_labels_df, on=["model_key", "pair_id", "group"], how="left"
    )
    return pilot


def paired_stats(c_vals, d_vals):
    """Compute EER(C), EER(D), delta, bootstrap CI, paired t-test, Wilcoxon, Cohen's d."""
    n = len(c_vals)
    diffs = d_vals - c_vals
    eer_c, eer_d = c_vals.mean(), d_vals.mean()
    delta = eer_d - eer_c

    if n < 2:
        return {
            "n": n, "eer_c": None, "eer_d": None, "delta": None,
            "ci": (None, None), "t_p": None, "w_p": None, "cohens_d": None,
        }

    t_stat, t_p = stats.ttest_rel(d_vals, c_vals)
    try:
        w_stat, w_p = stats.wilcoxon(d_vals, c_vals)
    except ValueError:
        w_stat, w_p = np.nan, np.nan

    rng = np.random.default_rng(42)
    boot_deltas = []
    for _ in range(10000):
        idx = rng.integers(0, n, n)
        boot_deltas.append((d_vals[idx] - c_vals[idx]).mean())
    ci_low, ci_high = np.percentile(boot_deltas, [2.5, 97.5])

    sd_diff = diffs.std(ddof=1) if n > 1 else np.nan
    cohens_d = delta / sd_diff if sd_diff and sd_diff > 0 else np.nan

    return {
        "n": n, "eer_c": eer_c, "eer_d": eer_d, "delta": delta,
        "ci": (ci_low, ci_high), "t_stat": t_stat, "t_p": t_p,
        "w_stat": w_stat, "w_p": w_p, "cohens_d": cohens_d,
    }


def primary_results(pilot, label_col="induction_category_judge", title="PRIMARY (Judge Labels)"):
    print(f"=== {title} ===")
    accepted = pilot[(pilot["group"].isin(["C", "D"])) & (pilot[label_col] == "Accepted")]
    pair_level = accepted.groupby(["model_key", "pair_id", "group"])["error"].mean().unstack("group")

    results = {}
    for model in ["llama3.2-3b", "qwen2.5-3b"]:
        if model not in pair_level.index:
            continue
        sub = pair_level.loc[model].dropna(subset=["C", "D"]) if isinstance(pair_level.loc[model], pd.DataFrame) else pd.DataFrame()
        if len(sub) == 0:
            print(f"{model}: insufficient paired data")
            continue
        stats_out = paired_stats(sub["C"].values, sub["D"].values)
        results[model] = stats_out
        print(f"\n--- {model} (n={stats_out['n']}) ---")
        if stats_out["eer_c"] is not None:
            print(f"EER(C) = {stats_out['eer_c']:.4f}, EER(D) = {stats_out['eer_d']:.4f}")
            print(f"Delta = {stats_out['delta']:+.4f}")
            print(f"95% CI: [{stats_out['ci'][0]:+.4f}, {stats_out['ci'][1]:+.4f}]")
            print(f"Paired t-test: t={stats_out['t_stat']:.3f}, p={stats_out['t_p']:.3f}")
            print(f"Wilcoxon: W={stats_out['w_stat']}, p={stats_out['w_p']:.3f}")
            print(f"Cohen's d: {stats_out['cohens_d']:.3f}")

        sub2 = sub.copy()
        sub2["delta"] = sub2["D"] - sub2["C"]
        sub2["direction"] = sub2["delta"].apply(lambda x: "D>C" if x > 0 else ("C>D" if x < 0 else "EQUAL"))
        print(f"Direction counts: {sub2['direction'].value_counts().to_dict()}")
    print()
    return results


def ablation_by_difficulty(pilot, pair_meta, label_col="induction_category_judge"):
    accepted = pilot[(pilot["group"].isin(["C", "D"])) & (pilot[label_col] == "Accepted")].copy()
    accepted["difficulty"] = accepted["pair_id"].map(lambda x: pair_meta.get(x, ("Unknown", "Unknown"))[1])
    print("=== Ablation: EER by Difficulty ===")
    print(accepted.groupby(["difficulty", "group"])["error"].agg(["mean", "count"]).unstack().to_string())
    print()


def ablation_by_eval_type(pilot, label_col="induction_category_judge"):
    accepted = pilot[(pilot["group"].isin(["C", "D"])) & (pilot[label_col] == "Accepted")]
    print("=== Ablation: EER by Evaluation-Question Type (S/X/U) ===")
    print(accepted.groupby(["eval_key", "group"])["error"].agg(["mean", "count"]).unstack().to_string())
    print()


# Domain/difficulty metadata for the 40-pair dataset (mirrors dataset/BCBench_v1.0_dataset.json)
PAIR_META = {
    5: ("Art", "Hard"), 6: ("History", "Medium"), 7: ("Geography", "Hard"), 10: ("Literature", "Easy"),
    13: ("Film", "Hard"), 14: ("Sports", "Medium"), 15: ("Art", "Medium"), 16: ("History", "Easy"),
    19: ("Sports", "Hard"), 20: ("Literature", "Medium"),
    21: ("History", "Medium"), 22: ("Geography", "Easy"), 23: ("Film", "Hard"), 24: ("Sports", "Medium"),
    25: ("Art", "Medium"), 26: ("History", "Hard"), 27: ("Geography", "Hard"), 28: ("Music", "Easy"),
    29: ("Sports", "Hard"), 30: ("Literature", "Medium"), 31: ("History", "Easy"), 32: ("Geography", "Medium"),
    33: ("Film", "Medium"), 34: ("Sports", "Easy"), 35: ("Art", "Hard"), 36: ("History", "Medium"),
    37: ("Music", "Hard"), 38: ("Geography", "Easy"), 39: ("Sports", "Medium"), 40: ("Literature", "Hard"),
    41: ("History", "Easy"), 42: ("Geography", "Medium"), 43: ("Film", "Easy"), 44: ("Art", "Medium"),
    45: ("Sports", "Hard"), 46: ("Music", "Medium"), 47: ("History", "Medium"), 48: ("Geography", "Hard"),
    49: ("Literature", "Easy"), 50: ("Film", "Hard"),
}


def main():
    parser = argparse.ArgumentParser(description="BCBench v1.0 analysis")
    parser.add_argument("--results", required=True, help="Path to BCBench_v1.0_results_FINAL.jsonl")
    parser.add_argument("--induction-labels", required=True,
                         help="Path to induction_both_labels.csv (judge.judge_validation)")
    args = parser.parse_args()

    df = load_results(args.results)
    induction_labels_df = load_induction_labels(args.induction_labels)

    manipulation_success(df)

    pilot = build_eval_with_labels(df, induction_labels_df)

    primary_results(pilot, label_col="induction_category_judge", title="PRIMARY (Judge Labels)")
    primary_results(pilot, label_col="induction_category_adjudicated", title="SENSITIVITY (Adjudicated Labels)")

    ablation_by_difficulty(pilot, PAIR_META)
    ablation_by_eval_type(pilot)


if __name__ == "__main__":
    main()
