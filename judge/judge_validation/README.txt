BCBench v1.0 — Manipulation-Check Adjudication Artifacts
===========================================================

These files document the independent adjudication process used to validate
the automated judge's induction-acceptance labels, performed after the full
50/40-pair experiment revealed an unexpectedly low manipulation-success rate
for Llama-3.2-3B.

FILES:

1. review_set_FULL_metadata_HIDDEN.json
   - 92 induction responses selected for review (all non-Accepted responses +
     a 16-item random QC sample of Accepted responses, seed=42)
   - Contains full metadata: model, pair_id, group, original judge label, claim,
     response, judge_summary

2. my_independent_labels.json
   - Claude's blind independent classification of all 92 items (read only the
     claim+response text, no metadata visible during classification), with
     one-sentence reasoning per item

3. deepseek_labels.json
   - DeepSeek's blind independent classification of the same 92 items, obtained
     via a fresh, context-isolated conversation (no project history, only the
     frozen acceptance criterion + blinded items)

4. full_comparison.csv
   - Merged table: review_id, model_key, pair_id, group, judge_label, my_label,
     deepseek_label (metadata revealed after both independent ratings were
     collected)

5. adjudicated_92_final.csv
   - Same as above + adjudicated_label column (majority vote across judge/me/
     DeepSeek; one true 3-way tie at R009 resolved manually with documented
     reasoning — see chat log)

6. induction_both_labels.csv
   - Full induction-record table (all model/pair/group combinations) with TWO
     label columns preserved separately:
     - induction_category_judge: original frozen judge labels (primary,
       preregistered analysis)
     - induction_category_adjudicated: adjudicated labels for the 92 reviewed
       items, judge label retained for items not in the review set

KEY RESULT:
- Judge vs. Claude: 92.4% agreement, Cohen's kappa = 0.812
- Judge vs. DeepSeek: 83.7% agreement, kappa = 0.659
- Claude vs. DeepSeek: 83.7% agreement, kappa = 0.670
- Only 3/92 cases (3.3%) where BOTH independent raters disagreed with the judge
- Sensitivity analysis (re-running EER/per-pair direction on adjudicated labels)
  produced IDENTICAL qualitative results to the primary (judge-label) analysis

This data supports the paper's claim that the null contamination finding is
robust to manipulation-check labeling methodology, not an artifact of judge
unreliability.
