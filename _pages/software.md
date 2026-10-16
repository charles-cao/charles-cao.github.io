---
layout: page
permalink: /software/
title: Software
description: Open-source tools from my research.
nav: true
nav_order: 2
---

## PyTextAD

**A Python library for text anomaly detection, at both the document level and the token level.**

<a href="https://github.com/charles-cao/pytextad" class="btn btn-sm z-depth-0" role="button"><i class="fa-brands fa-github"></i> GitHub</a>
<a href="https://pytextad.readthedocs.io" class="btn btn-sm z-depth-0" role="button"><i class="fa-solid fa-book"></i> Docs</a>
<a href="https://huggingface.co/spaces/Charles-Cao/pytextad" class="btn btn-sm z-depth-0" role="button"><i class="fa-solid fa-play"></i> Online Demo</a>
<a href="https://pypi.org/project/pytextad/" class="btn btn-sm z-depth-0" role="button"><i class="fa-brands fa-python"></i> PyPI</a>

[![GitHub stars](https://img.shields.io/github/stars/charles-cao/pytextad?style=social)](https://github.com/charles-cao/pytextad)
[![PyPI version](https://img.shields.io/pypi/v/pytextad)](https://pypi.org/project/pytextad/)
[![PyPI downloads](https://img.shields.io/pypi/dm/pytextad)](https://pypi.org/project/pytextad/)

```bash
pip install pytextad
```

- **One interface, 23 detectors.** Every detector exposes `fit`, `decision_function` and `predict`.
- **Token-level detection.** Any detector can score every token, and token scores roll up into document scores.
- **Faithful implementations.** Each detector is either the authors' original code or numerically checked against it.
- **Benchmarks included.** Six datasets with a label for every word, evaluated at both token and document levels.
- **Works with PyOD.** `DocumentDetector` and `TokenDetector` wrap any embedding detector, including PyOD models.

Detectors include CVDD, DATE and FATE (trained end to end), and embedding detectors such as DAGMM, GOAD, DROCC, ICL, SLAD, DTE, MCM, SIK and TokenCore.

Related papers: [Towards Token-Level Text Anomaly Detection]({{ '/publications/' | relative_url }}) (WWW 2026), [Text Anomaly Detection with Simplified Isolation Kernel]({{ '/publications/' | relative_url }}) (Findings of EMNLP 2025), [TAD-Bench]({{ '/publications/' | relative_url }}) (Machine Learning 2026).
