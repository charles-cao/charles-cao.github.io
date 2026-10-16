---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# Welcome!

I am a postdoctoral researcher jointly supervised by Great Bay University and Tsinghua Shenzhen International Graduate School, Tsinghua University, working with Dr. Sikun Yang and Prof. Yujiu Yang. I was selected for the Ministry of Education Overseas Postdoctoral Talent Program in 2025. I received my PhD in Computer Science from Deakin University, Australia, in 2025, under the supervision of Dr. Ye Zhu and Prof. Kai Ming Ting. Before that, I received the M.Sc. degree in Data Science from Deakin University in 2021 and the B.Sc. degree in Information Technology from Monash University in 2020.

My research focuses on the theory and algorithms of anomaly detection, including isolation-based and kernel-based methods, streaming data, text anomaly detection, and incomplete heterogeneous data. My work has appeared in venues such as WWW, ICDM, Findings of EMNLP, JAIR, Machine Learning, Artificial Intelligence Review, and Machine Intelligence Research <a href='https://scholar.google.com/citations?user=zn19uAcAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

In my free time, I enjoy playing basketball and fishing.

# 🔥 News
- *2026.08*: &nbsp;🎉 Our paper on Isolation-based Spherical Ensemble Representations (ISER) is accepted by ICDM 2026.
- *2026*: &nbsp;🎉 TAD-Bench is published in Machine Learning.
- *2026.01*: &nbsp;🎉 Our paper on token-level text anomaly detection is accepted by WWW 2026.
- *2025.10*: &nbsp;🎤 Organized the ATKD special session at ADMA 2025.
- *2025.08*: &nbsp;🎉 Our paper on text anomaly detection with Simplified Isolation Kernel is accepted by Findings of EMNLP 2025.
- *2025.06*: &nbsp;🎓 Joined Great Bay University and Tsinghua University as a postdoctoral researcher.

# 📖 Educations
- *2022.03 - 2025.06*, Doctor of Philosophy in Computer Science. Deakin University, Australia.
- *2020.08 - 2021.10*, Master of Data Science. Deakin University, Australia.
- *2017.03 - 2020.07*, Bachelor of Information Technology. Monash University, Australia.

# 📝 Publications 

(* corresponding author)

**2026**

- **Cao, Y.**, Yang, S., Tian, H., He, K., Qi, L., Liu, M., & Yang, Y. (2026). Isolation-based Spherical Ensemble Representations for Anomaly Detection. IEEE International Conference on Data Mining (ICDM 2026). [[arXiv]](https://arxiv.org/abs/2510.13311)

- **Cao, Y.**, Yu, B., Yang, S., Liu, M., & Yang, Y. (2026). Towards Token-Level Text Anomaly Detection. In Proceedings of the ACM Web Conference 2026 (WWW 2026), pp. 8733-8736. [[arXiv]](https://arxiv.org/abs/2601.13644)

- **Cao, Y.**, Yang, S., Li, C., Xiang, H., Qi, L., Liu, B., Li, R., & Liu, M. (2026). TAD-Bench: A Comprehensive Benchmark for Embedding-Based Text Anomaly Detection. Machine Learning, 115(7), 155. [[arXiv]](https://arxiv.org/abs/2501.11960)

**2025**

- **Cao, Y.**, Yang, S., Yang, Y., Qi, L., & Liu, M. (2025). Text Anomaly Detection with Simplified Isolation Kernel. In Findings of the Association for Computational Linguistics: EMNLP 2025. [[Paper]](https://aclanthology.org/2025.findings-emnlp.680/)

- **Cao, Y.**, Xiang, H., Zhang, H., Zhu, Y., & Ting, K. M. (2025). Anomaly Detection Based on Isolation Mechanisms: A Survey. Machine Intelligence Research, 22(5), 849-865.

- **Cao, Y.**, Ma, Y., Zhu, Y., & Ting, K. M. (2025). Revisiting Streaming Anomaly Detection: Benchmark and Evaluation. Artificial Intelligence Review, 58(1), 8.

**2024**

- **Cao, Y.**, Ma, Y., Tang, X., Rasheed, R. A., & Li, H. X. (2024). A Data-Driven Framework for Identifying Abnormal Status in Natural Gas Wells. In Advanced Data Mining and Applications (ADMA 2024), pp. 105-119.

- **Cao, Y.**, Pokhrel, S. R., Zhu, Y., Doss, R., & Li, G. (2024). Automation and Orchestration of Zero Trust Architecture: Potential Solutions and Challenges. Machine Intelligence Research, 21(2), 294-317.

- **Cao, Y.**, Zhu, Y., Ting, K. M., Salim, F. D., Li, H. X., Yang, L., & Li, G. (2024). Detecting Change Intervals with Isolation Distributional Kernel. Journal of Artificial Intelligence Research, 79, 273-306.

- **Cao, Y.**, Zhu, Y., Ting, K. M., Salim, F. D., Li, H. X., Yang, L., & Li, G. (2024). Detecting Change Intervals with Isolation Distributional Kernel (Abstract Reprint). IJCAI 2024, p. 8476.

- Gan, C., Zheng, J., Zhu, Q., **Cao, Y.**, & Zhu, Y. (2024). A Survey of Dialogic Emotion Analysis: Developments, Approaches and Perspectives. Pattern Recognition, 110794.

- Li, C., **Cao, Y.\***, Zhu, Y., Cheng, D., Li, C., & Morimoto, Y. (2024). Ripple Knowledge Graph Convolutional Networks for Recommendation Systems. Machine Intelligence Research.

- Gan, C., Fu, X., Feng, Q., Zhu, Q., **Cao, Y.**, & Zhu, Y. (2024). A Multimodal Fusion Network with Attention Mechanisms for Visual-Textual Sentiment Analysis. Expert Systems with Applications, 242, 122731.

- Gong, L., Zhang, H., Liu, Z., Ting, K. M., **Cao, Y.**, & Zhu, Y. (2024). Local Subsequence-Based Distribution for Time Series Clustering. In Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD 2024), pp. 259-270.

**2023**

- Li, C., **Cao, Y.\***, Zhu, Y., Zhang, J., Annisa, A., Cheng, D., ... & Morimoto, Y. (2023). An Enhanced Distributed Algorithm for Area Skyline Computation Based on Apache Spark. In International Conference on Knowledge Science, Engineering and Management (KSEM 2023), pp. 35-43.

- Liu, Y., Zhang, Y., **Cao, Y.\***, Zhu, Y., Zaidi, N., Ranaweera, C., ... & Zhu, Q. (2023). Kernel-Based Feature Extraction for Time Series Clustering. In International Conference on Knowledge Science, Engineering and Management (KSEM 2023), pp. 276-283.

- Zhang, B., **Cao, Y.\***, Zhu, Y., Rajasegarar, S., Liu, G., Li, H. X., ... & Li, G. (2023). An Improved Visual Assessment with Data-Dependent Kernel for Stream Clustering. In Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD 2023), pp. 197-209. **(Best Paper Nomination)**

# 💰 Grants
- 2025, Ministry of Education Overseas Postdoctoral Talent Program, Principal Investigator.
- Guangdong Basic and Applied Basic Research Foundation, Youth Program, Principal Investigator.
- Guangdong-Dongguan Joint Fund, Youth Program, Participant.

# 💬 Tutorial Talks
- **Moving Beyond Traditional Anomaly Detection (2023).** Ye Zhu (Deakin University), Gang Li (Deakin University), Chen Li (Nagoya University), **Yang Cao** (Deakin University). The 27th Pacific-Asia Conference on Knowledge Discovery and Data Mining (PAKDD 2023).

- **Revolutionizing Anomaly Detection: Approaches and Guidelines (2023).** Mark Carman (Politecnico di Milano), Ye Zhu (Deakin University), Gang Li (Deakin University), **Yang Cao** (Deakin University). ECML PKDD 2023.

- **Moving Beyond Traditional Anomaly Detection (2023).** Ye Zhu (Deakin University), Gang Li (Deakin University), **Yang Cao** (Deakin University). The 32nd International Joint Conference on Artificial Intelligence (IJCAI 2023).

# 🤝 Academic Services
- Special Session Chair, Special Session on ATKD, ADMA 2025.
- Reviewer: ICML, NeurIPS, IJCAI.

# 💻 Experience
- *2025.06 - Present*. *Postdoctoral Researcher*. Great Bay University and Tsinghua Shenzhen International Graduate School, Tsinghua University.
- *2022 - 2025*. *Teaching Assistant*. Deakin University.
  - SIT718, Real World Analytics
  - MIS772, Predictive Analytics
  - SIT708, Mobile Application Development
  - MIS373, Artificial Intelligence for Business (workshop material development)

# 🎖 Honors and Awards
- 2023, **Best Paper Nomination**, PAKDD 2023.
- 2020, **Wong Swee Soon Prize for Student Excellence** (Industry Experience studio projects), Monash University, Australia.
