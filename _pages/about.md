---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  dl {
    margin-bottom: 60px; /* 调整这个值以获得合适的间距 */
    clear: both;
  }

  img {
    display: block;
    margin: 0px 10px 10px 0px; /* 图片居中 上右下左*/ 
    max-width: 100%; /* 限制图片最大宽度 */
  }

  hr {
    margin: 40px 0;
    border-color: #eee;
  }

  dl dd {
  color: #666; 
  margin-top: 5px; 
  margin-bottom: 5px;
}

  dl dd strong {
  font-weight: bold;
  color: black;
  }

  /* 下面添加publications部分的类选择器 */
  .publications {
  color: #333;
  }

  .publications strong {
  font-weight: bold;
  color: black; 
  }

    .co-first {
    color: red;
  }

  /* 新增标题统一样式 */
  h2 {
    font-size: 1.8em;
    color: #2c3e50;
    margin: 30px 0 15px;
    border-bottom: 2px solid #3498db;
    padding-bottom: 8px;
  }

  h3 {
    font-size: 1.4em;
    margin: 20px 0 10px;
  }

  /* 修改现有图片样式 */
  .pub-item {
    display: flex;
    gap: 30px;
    align-items: flex-start;
    margin: 40px 0;
    padding: 20px;
    background: #f9f9f9;
    border-radius: 8px;
    transition: transform 0.3s ease;
  }

  .pub-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  }

  .pub-item img {
    width: 40%;
    min-width: 300px;
    border-radius: 4px;
    object-fit: cover;
  }

  @media (max-width: 768px) {
    .pub-item {
      flex-direction: column;
    }
    .pub-item img {
      width: 100%;
      min-width: auto;
    }
  }

  /* 新增颜色规范 */
  :root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --text-color: #444;
  }

  body {
    color: var(--text-color);
    line-height: 1.6;
  }

  a {
    color: var(--secondary-color);
    text-decoration: none;
    transition: color 0.3s ease;
  }

  a:hover {
    color: #2980b9;
    text-decoration: underline;
  }

  ul, ol {
    padding-left: 30px;
    margin: 15px 0;
  }

  li {
    margin: 8px 0;
    line-height: 1.5;
  }

  /* 新增移动端优化 */
  @media (max-width: 480px) {
    h2 {
      font-size: 1.5em;
    }
    
    .pub-item {
      padding: 15px;
      margin: 25px 0;
    }
    
    .pub-item h3 {
      font-size: 1.2em;
    }
  }
</style>

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>


Hello, I am Hao Li, a third-year Ph.D. student at the School of Electronic Information at Wuhan University, under the supervision of Professor [Hao Jiang](http://eis.whu.edu.cn/index/szdwDetail?rsh=00007828&newskind_id=20160320222026165YIdDsQIbgNtoE). My research interests lie in the integration of social networks, graph neural networks, and large language models.

🌟[Email](whulh@whu.edu.cn) / [Github](https://github.com/Lihaogx) / [Wechat](../images/wechat.jpg) / [Google Scholar](https://scholar.google.com/citations?hl=zh-CN&user=xv78JsEAAAAJ)


# 🔎 Research 
My research interests lie in the integration of social networks, graph neural networks, and large language models. Specifically, I work in the following areas:

1. **Graph Neural Networks**
   - Dynamic Graph Embedding
   - Persistent Homology on graphs

2. **Social Networks and Graph Neural Networks**
   - Opinion Dynamics on Graphs
   - Special Structures in Social Graphs

3. **Large Language Models for Social Sciences**
   - Agents and Social Simulation
   - Enhancing Sociological Research through Large Language Models
<hr/>

# 🔥 News
<div style="max-height: 200px; overflow-y: auto;">
  <ul>
    <li><strong>2025.01:</strong> Our paper "UniGO: A Unified Graph Neural Network for Modeling Opinion Dynamics on Graphs" has been accepted by <strong>WWW 2025</strong>. 🎉 See you in Sydney!</li>
    <li><strong>2025.12:</strong> Our paper "Political Actor Agent: Simulating Legislative System for Roll Call Votes Prediction with Large Language Models" has been accepted as an oral presentation by <strong>AAAI 2025</strong>. 🎉 See you in Philadelphia!</li>
    <li><strong>2024.05:</strong> One paper "Dynamic Neural Dowker Network: Approximating Persistent Homology in Dynamic Directed Graphs" has been accepted at <strong>KDD 2024</strong>. 🎉 See you in Barcelona!</li>
  </ul>
</div>
<hr/>


# 📃 Publications 
<div style="display: flex; align-items: center;">
  <img src="../images/UniGO.jpg" alt="UniGO" style="width: 350px;">
  <div>
    <h3><a href="https://openreview.net/forum?id=bElAkCL6zb#discussion" target="_blank">UniGO: A Unified Graph Neural Network for Modeling Opinion Dynamics on Graphs</a></h3>
    <p><strong>Hao Li</strong>, Jiang Hao, Yuke Zheng, Hao Sun, Wenying Gong<br>
    THE WEB CONFERENCE, 2025</p>
  </div>
</div>

<br/>

<div style="display: flex; align-items: center;">
  <img src="../images/PAA.jpg" alt="Political Actor Agent" style="width: 350px;">
  <div>
    <h3><a href="https://arxiv.org/abs/2412.07144" target="_blank">Political Actor Agent: Simulating Legislative System for Roll Call Votes Prediction with Large Language Models</a></h3>
    <p><strong>Hao Li</strong>, Ruoyuan Gong, Jiang Hao<br>
    Proceedings of the AAAI conference on artificial intelligence(AAAI), 2025</p>
  </div>
</div>

<br >

<div style="display: flex; align-items: center;">
  <img src="../images/DNDN.jpg" alt="Dynamic Neural Dowker Networks" style="width: 350px;">
  <div>
    <h3><a href="https://dl.acm.org/doi/abs/10.1145/3637528.3671980" target="_blank">Dynamic Neural Dowker Network: Approximating Persistent Homology in Dynamic Directed Graphs</a></h3>
    <p><strong>Hao Li</strong>, Jiang Hao, Fan Jiajun, Ye Dongsheng, Du Liang<br>
    Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2024</p>
  </div>
</div>

<br/>

<div style="display: flex; align-items: center;">
  <img src="../images/DHGAT.jpg" alt="DHGAT" style="width: 350px;">
  <div>
    <h3><a href="https://www.sciencedirect.com/science/article/abs/pii/S092523122301161X" target="_blank">DHGAT: Hyperbolic representation learning on dynamic graphs via attention networks</a></h3>
    <p><strong>Hao Li</strong>, Hao Jiang, Dongsheng Ye, Qiang Wang, Liang Du, Yuanyuan Zeng, Liu yuan, Yingxue Wang, Cheng Chen<br>
    Neurocomputing</p>
  </div>
</div>

<br/>

<div style="display: flex; align-items: center;">
  <img src="../images/fedogm.jpg" alt="Prediction of Occupational Group Mobility" style="width: 350px;">
  <div>
    <h3><a href="https://ieeexplore.ieee.org/abstract/document/10415798/" target="_blank">Federated Learning for Privacy-Preserving Prediction of Occupational Group Mobility Using Multi-Source Mobile Data</a></h3>
    <p><strong>Hao Li</strong>, Jiang Hao, Haoran Xian, Qimei Chen<br>
    IEEE International Conference on Data Mining (ICDM), 2023</p>
  </div>
</div>

<hr/>


# 📝 Service
### Conference Reviewer
- Reviewer for WWW'2025
- Reviewer for ICWSM'2025
- Reviewer for KDD'2024
- Reviewer for ICDM'2024

<hr/>

# 🎓 Educations
- 2015-2019 Bachelor's Degree, Electronic Information School, Wuhan University, China
- 2019-present Integrated Master-Ph.D. Student, Electronic Information School, Wuhan University, China
