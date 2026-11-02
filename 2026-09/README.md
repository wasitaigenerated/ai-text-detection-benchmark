# September 2026 edition: Pangram, GPTZero, ZeroGPT, tropa-2 and tropa-3

2,572 texts (1,260 human from 44 sources in 7 languages, 891 AI from 62 models, 421 humanized by six
tools). ZeroGPT, tropa-2 and tropa-3 scored all of them, GPTZero 894 and Pangram 513.

- Write-up: https://wasitaigenerated.com/research/ai-detector-benchmark-pangram-gptzero-zerogpt-tropa-3-2026
- Dataset card with every column and licence: https://huggingface.co/datasets/wasitaigeneratedcom/ai-detector-benchmark-2026-09

## Files

```
benchmark_2026-09.parquet   one row per text with every detector's verdict (same file as on Hugging Face)
eval.py                     reproduces the headline tables
```

```bash
pip install pandas pyarrow
python eval.py
```

## Headline (513 texts scored by all five detectors)

Human row = share wrongly flagged as AI (lower is better); other rows = share detected.

| | n | ZeroGPT | Pangram | GPTZero | tropa-2 | tropa-3 |
|---|---:|---:|---:|---:|---:|---:|
| Human | 247 | 0.8 % | 0.0 % | 0.0 % | 0.4 % | 0.0 % |
| Raw AI | 159 | 21.4 % | 44.0 % | 61.6 % | 77.4 % | 95.6 % |
| Paraphrased AI | 33 | 9.1 % | 9.1 % | 6.1 % | 18.2 % | 54.5 % |
| Humanized AI | 74 | 4.1 % | 35.1 % | 25.7 % | 28.4 % | 54.1 % |

Verdict rules: third-party tools count as AI only with the label "AI" ("Mixed" is reported separately in
the write-up). tropa-3 counts as AI at a display score ≥ 90, the threshold that flags 0.1 % of 239,490
held-out human texts; tropa-2 at the threshold that flags the same 0.1 % of those texts.

**Caveat:** the AI and humanized texts come from the same generators and humanizers tropa-3 was
trained on (different prompts and documents, no text overlap). Treat tropa-3's numbers, especially on
humanized text, as an upper bound.
