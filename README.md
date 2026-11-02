# AI Text Detection Benchmark

Open, dated benchmarks of **AI text detectors**: the same texts scored by several detectors on the same
day, with every text and verdict published. Run by [WasItAIGenerated](https://www.wasitaigenerated.com).

| Edition | What is tested | Folder | Write-up |
|---|---|---|---|
| **September 2026** | 2,572 texts incl. six humanizers; Pangram, GPTZero, ZeroGPT, tropa-2, tropa-3 | [`2026-09/`](2026-09/) | [wasitaigenerated.com](https://www.wasitaigenerated.com/research/ai-detector-benchmark-pangram-gptzero-zerogpt-tropa-3-2026) |
| August 2026 | 522 texts; GPTZero, ZeroGPT, tropa-2 | [`2026-08/`](2026-08/) | [wasitaigenerated.com](https://www.wasitaigenerated.com/research/ai-detector-benchmark-gptzero-zerogpt-tropa-2-2026) |

September data on Hugging Face: https://huggingface.co/datasets/wasitaigeneratedcom/ai-detector-benchmark-2026-09

Each folder has its own README with the headline table, the verdict rules and the caveats. Read the
caveats before quoting a number: we build these sets ourselves, and our detectors have seen similar
content in training.

## Evaluate your own detector

Score every row's text in `2026-09/benchmark_2026-09.parquet`, add a column and run
[`2026-09/eval.py`](2026-09/eval.py). Then email **patrick@wasitaigenerated.com** with your results and how
you ran the detector. We link every submission from the write-up, including results that beat ours.

## Related benchmarks

- [ai-image-detection-benchmark](https://github.com/wasitaigenerated/ai-image-detection-benchmark): AI image detectors, incl. WhatsApp and Instagram copies
- [ai-video-detection-benchmark](https://github.com/wasitaigenerated/ai-video-detection-benchmark): AI video detectors, incl. messenger copies
- Data on Hugging Face: [text, September 2026](https://huggingface.co/datasets/wasitaigeneratedcom/ai-detector-benchmark-2026-09) · [images and video, October 2026](https://huggingface.co/datasets/wasitaigeneratedcom/frontier-image-video-bench-2026-10)
- Want to audit a detector, ours included? [Call for benchmarks](https://www.wasitaigenerated.com/call-for-benchmarks) (free API credits for researchers)

## License

Code (`eval.py`): MIT (see `LICENSE`). Data, results and text: CC BY 4.0 (see `LICENSE-DATA`), except texts whose source license is listed per row.
