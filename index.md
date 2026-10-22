---
layout: home
title: ホーム
lang: ja
translation_key: index
permalink: /
---

{% include home-gallery.html image_label="ギャラリー写真" caption="写真" controls_label="写真を選択" %}

<section class="hero" id="top">
  <div class="hero-content">
    <h1>Ryunosuke Abe</h1>
    <p class="subtitle">
      奈良先端科学技術大学院大学 修士課程。数理情報学研究室。
    </p>
    <div class="meta">
      <span class="tag blue">自然言語処理</span>
      <span class="tag green">神経科学</span>
      <span class="tag pink">表現学習</span>
    </div>
    <div class="meta" style="margin-top:1.4rem;">
      <a class="btn ghost" href="{{ '/publications/' | relative_url }}">論文を見る</a>
      <a class="btn ghost" href="{{ '/projects/' | relative_url }}">プロジェクトを見る</a>
      <a class="btn ghost" href="{{ '/cv/' | relative_url }}">経歴を見る</a>
    </div>
  </div>
  {% include home-portrait.html alt="Ryunosuke Abe のポートレート" %}
</section>

<section class="grid-2" id="about">
  <div class="info-grid">
    <article class="card">
      <h2>自己紹介</h2>
      <p>
        奈良先端科学技術大学院大学の修士課程に在籍し、Kubo Takatomi先生の指導を受けています。
        学部時代は慶應義塾大学文学部で学びました。
        自分の関心と学びの方向について悩んだ経験から、言語と、その背後にある神経の仕組みに興味を持つようになりました。
        研究の道を歩み始めたところで、新しいアイデアの探究や共同研究を楽しみにしています。
      </p>
    </article>

    <article class="card" id="research">
      <h2>研究テーマ</h2>
      <div class="highlight-grid">
        <div class="highlight">
          <h3>神経科学に着想を得た表現学習</h3>
          <p>CEBRAを用い、線形変換の範囲で一貫した表現を学習することを目指しています。</p>
        </div>
        <div class="highlight">
          <h3>非線形空間における知識構造</h3>
          <p>言語で表現され、異なるモダリティの間でも共有される「知識」の構造を探っています。</p>
        </div>
      </div>
    </article>
  </div>
</section>

<section class="card" id="highlights">
  <h2>近況</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="period">2025</span>
      <h3>紹介できる成果を目指して</h3>
      <p>研究活動を始めたところです。</p>
    </div>
  </div>
</section>

<section class="card" id="education">
  <h2>学歴</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="period">2025 – 2027</span>
      <h3>情報科学分野・修士課程</h3>
      <p>奈良先端科学技術大学院大学 — 補助信号を用いた言語の表現学習。</p>
    </div>
    <div class="timeline-item">
      <span class="period">2020 – 2025</span>
      <h3>文学部</h3>
      <p>慶應義塾大学 — 言語学、認知科学、デジタル・ヒューマニティーズを学びました。</p>
    </div>
  </div>
</section>

<section class="callout" id="contact">
  <h2>頑健な表現学習に向けて</h2>
  <p>
    共同研究や研究滞在、さまざまな方に研究を紹介する機会に関心があります。
    近いテーマに取り組んでいる方や、新しい実験を一緒に考えてみたい方は、ぜひご連絡ください。
  </p>
  <a class="btn primary" href="mailto:abe.ryunosuke.at2@naist.ac.jp">連絡する</a>
</section>
