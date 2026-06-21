# BCBench: A Controlled Protocol for Evaluating Cross-Claim Belief Contamination in Large Language Models

**Authors:** Samuel Stephen¹, R. Vignesh¹
¹Karunya Institute of Technology and Sciences, Coimbatore, Tamil Nadu, India

[![DOI](https://zenodo.org/badge/DOI/PLACEHOLDER.svg)](https://doi.org/PLACEHOLDER)

## Overview

BCBench investigates **cross-claim belief contamination**: whether an LLM accepting a false belief about one claim alters its subsequent epistemic behavior toward a second, structurally unrelated claim. This is distinct from prior work on sycophancy, instruction-refutation persistence, knowledge drift, and cognitive anchoring, all of which measure effects *within* a single claim or topic.

This repository contains the full experimental protocol, dataset, judge implementation, validation pipeline, results, and analysis code for BCBench v1.0.

## Key Finding

Evaluating two open 3B-parameter instruction-tuned models (Llama-3.2-3B-Instruct, Qwen2.5-3B-Instruct) under a controlled four-group protocol (Control, Context Control, True Induction, False Induction), we find **no consistent evidence of cross-claim belief contamination**. This null result is robust to independent, blind adjudication of manipulation-check labels (92.4% agreement, Cohen's κ = 0.81, against a context-isolated second rater).

## Repository Structure

```
BCBench/
├── notebook/         Kaggle-ready experiment notebook (generation, judging, calibration, analysis)
├── dataset/          BCBench v1.0 dataset (40 induction pairs, 120 evaluation questions)
├── protocol/         Frozen experimental protocol specification (v0.9)
├── judge/            Judge prompts and independent adjudication/validation artifacts
├── results/          Full experimental results (1,120 records)
├── analysis/         Analysis scripts (EER, per-pair direction, ablations, statistical tests)
├── paper/            Paper draft
├── LICENSE

```

## Reproducing the Experiment

1. Open `notebook/bcbench_pilot_v3.ipynb` in a Kaggle T4 GPU environment.
2. Run cells in order: Setup → Dataset → Model/Judge/Results-writer functions → Sanity check (optional) → Full experiment.
3. Results write to a checkpoint-resumable JSONL file with full provenance (protocol version, dataset version, judge version, random seed) in every record.

See `protocol/BC_Protocol_v0.9.md` for the full experimental design and `judge/judge_validation/README.txt` for the adjudication methodology.

## Dataset

40 matched true/false induction pairs across 7 domains (History, Geography, Film, Sports, Art, Literature, Music), each paired with 3 evaluation questions (Supported, Contradicted, Unverifiable) drawn from 6 disjoint domains (Medicine, Astronomy, Biology, Economics, Physics, Chemistry). See `dataset/dataset_construction_rules.md` for full construction methodology.



## License

See `LICENSE`.

## Contact

Samuel Stephen — samuels24@karunya.edu.in
