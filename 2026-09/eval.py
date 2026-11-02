#!/usr/bin/env python3
"""Reproduce the September 2026 headline tables from benchmark_2026-09.parquet.

    pip install pandas pyarrow && python eval.py
"""
import pandas as pd

df = pd.read_parquet("benchmark_2026-09.parquet")
df["cat"] = df["group"].map(lambda g: "human" if g.startswith("human/") else "humanized" if g.startswith("humanized") else g)
DET = {
    "ZeroGPT": lambda d: d.zerogpt_label == "ai",
    "Pangram": lambda d: d.pangram_label == "ai",
    "GPTZero": lambda d: d.gptzero_label == "ai",
    "tropa-2": lambda d: d.tropa2_score >= 0.999988,    # same 0.1% FPR on 239,490 human texts as tropa-3
    "tropa-3": lambda d: d.tropa3_display >= 90,        # display score 90 = 0.1% FPR on 239,490 human texts
}
NEEDS = {"ZeroGPT": "zerogpt_label", "Pangram": "pangram_label", "GPTZero": "gptzero_label"}


def table(dets, title):
    sub = df.dropna(subset=[NEEDS[d] for d in dets if d in NEEDS])
    print(f"\n{title} ({len(sub)} texts; human row = flagged as AI, others = detected)")
    out = sub.groupby("cat").apply(lambda g: pd.Series({"n": len(g), **{d: round(100 * DET[d](g).mean(), 1) for d in dets}}))
    print(out.reindex(["human", "ai_raw", "ai_paraphrase", "humanized"]).to_string())


table(list(DET), "All five detectors")
table(["ZeroGPT", "GPTZero", "tropa-2", "tropa-3"], "Without Pangram")
