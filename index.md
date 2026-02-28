---
layout: home
title: Home
---

<section class="card photo-reel" id="gallery" data-photo-reel>
  <div class="photo-reel__head">
    <h2>Photo Reel</h2>
    <p>Monochrome by default. Hover on desktop, or scroll into view on mobile, to restore original color.</p>
  </div>
  <div class="photo-stage">
    {% assign gallery_files = site.static_files | where_exp: "file", "file.path contains '/Photos-3-001/'" | sort: "path" %}
    {% assign photo_count = 0 %}
    {% for file in gallery_files %}
      {% assign ext = file.extname | downcase %}
      {% if ext == '.jpg' or ext == '.jpeg' or ext == '.png' or ext == '.webp' or ext == '.avif' %}
        {% assign photo_count = photo_count | plus: 1 %}
        <figure class="photo-frame{% if photo_count == 1 %} is-active{% endif %}" data-photo-frame>
          <img src="{{ file.path | relative_url }}" alt="Photo reel image {{ photo_count }}">
          <figcaption>Photo / {% if photo_count < 10 %}0{% endif %}{{ photo_count }}</figcaption>
        </figure>
      {% endif %}
    {% endfor %}
  </div>
  <div class="photo-dots" data-photo-dots aria-label="Photo reel controls"></div>
</section>

<section class="hero" id="top">
  <div class="hero-content">
    <h1>Ryunosuke Abe</h1>
    <p class="subtitle">
      Master's student at NAIST. Mathematical Information Lab.
    </p>
    <div class="meta">
      <span class="tag blue">NLP </span>
      <span class="tag green">Neuroscience</span>
      <span class="tag pink">Representaiton Learning</span>
    </div>
    <div class="meta" style="margin-top:1.4rem;">
      <a class="btn ghost" href="{{ '/publications/' | relative_url }}">Read Publications</a>
      <a class="btn ghost" href="{{ '/projects/' | relative_url }}">Explore Projects</a>
      <a class="btn ghost" href="{{ '/cv/' | relative_url }}">Download CV</a>
    </div>
  </div>
  <div class="hero-image">
    <figure>
      <img src="{{ '/material/light.jpg' | relative_url }}" alt="Portrait of Ryunosuke Abe" data-theme-image data-light-src="{{ '/material/light.jpg' | relative_url }}" data-dark-src="{{ '/material/dark.jpg' | relative_url }}">
    </figure>
  </div>
</section>

<section class="grid-2" id="about">
  <div class="info-grid">
    <article class="card">
      <h2>About</h2>
      <p>
        I am a master's student at the Nara Institute of Science and Technology, advised by Kubo Takatomi.
        I was affiliated faculty of literature at Keio University during my undergraduate studies.
        Through my undergraduate experience, hard days since it hardly did not fit my interests,
        I came to realize that my interests lie in the language and the neural mechanisms behind it.
        I am just starting out my research career, and excited to explore new ideas and collaborate with others.
      </p>
    </article>

    <article class="card" id="research">
      <h2>Research Focus</h2>
      <div class="highlight-grid">
        <div class="highlight">
          <h3>Neuroscience guided representation learning</h3>
          <p>Using CEBRA for consistent representation within linear transformations.</p>
        </div>
        <div class="highlight">
          <h3>Knowledge structure with non linear space</h3>
          <p>Identifying the structure of "knowledge" represented by language which shared by different modalities.</p>
        </div>
      </div>
    </article>
  </div>
</section>

<section class="card" id="highlights">
  <h2>Recent Highlights</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="period">2025</span>
      <h3>I wish I had Highlights</h3>
      <p>Just started my research career.</p>
    </div>
  </div>
</section>

<section class="card" id="education">
  <h2>Education</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="period">2025 – 2027</span>
      <h3>MS in Information Science</h3>
      <p>Nara Institute of Science and Technology — Representation learning for language with auxiliary signals.</p>
    </div>
    <div class="timeline-item">
      <span class="period">2020 – 2025</span>
      <h3>BA in Literature</h3>
      <p>Keio University — Linguistics, cognitive science, and digital humanities coursework.</p>
    </div>
  </div>
</section>

<section class="callout" id="contact">
  <h2>Robust Representation Learning</h2>
  <p>
    I am open to research collaborations, visiting positions, and opportunities to present this work to diverse audiences.
    Reach out if you are exploring similar directions or want to co-design new experiments.
  </p>
  <a class="btn primary" href="mailto:abe.ryunosuke.at2@naist.ac.jp">Contact Me</a>
</section>
