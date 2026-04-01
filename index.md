---
layout: home
---

{% assign transparent_pixel = 'data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw==' %}
{% assign gallery_sizes = '(max-width: 600px) calc(100vw - 2.3rem), (max-width: 1080px) calc(100vw - 4rem), 1046px' %}
{% assign hero_sizes = '(max-width: 600px) 60vw, (max-width: 900px) 38vw, 260px' %}

<section class="card photo-reel" id="gallery" data-photo-reel>
  <div class="photo-stage">
    {% assign gallery_files = site.static_files | where_exp: "file", "file.path contains '/Photos-3-001/'" | sort: "path" %}
    {% assign photo_count = 0 %}
    {% for file in gallery_files %}
      {% assign ext = file.extname | downcase %}
      {% if ext == '.jpg' or ext == '.jpeg' or ext == '.png' or ext == '.webp' or ext == '.avif' %}
        {% assign photo_count = photo_count | plus: 1 %}
        {% assign filename = file.path | split: '/' | last %}
        {% assign basename = filename | replace: file.extname, '' %}
        {% capture gallery_webp_srcset %}{{ '/optimized/gallery/' | append: basename | append: '-1280.webp' | relative_url }} 1280w, {{ '/optimized/gallery/' | append: basename | append: '-1920.webp' | relative_url }} 1920w{% endcapture %}
        {% capture gallery_jpg_srcset %}{{ '/optimized/gallery/' | append: basename | append: '-1280.jpg' | relative_url }} 1280w, {{ '/optimized/gallery/' | append: basename | append: '-1920.jpg' | relative_url }} 1920w{% endcapture %}
        {% capture gallery_fallback %}{{ '/optimized/gallery/' | append: basename | append: '-1280.jpg' | relative_url }}{% endcapture %}
        <figure class="photo-frame{% if photo_count == 1 %} is-active{% endif %}" data-photo-frame>
          <picture>
            <source
              type="image/webp"
              sizes="{{ gallery_sizes }}"
              {% if photo_count == 1 %}
                srcset="{{ gallery_webp_srcset }}"
              {% else %}
                data-srcset="{{ gallery_webp_srcset }}"
              {% endif %}>
            <source
              type="image/jpeg"
              sizes="{{ gallery_sizes }}"
              {% if photo_count == 1 %}
                srcset="{{ gallery_jpg_srcset }}"
              {% else %}
                data-srcset="{{ gallery_jpg_srcset }}"
              {% endif %}>
            <img
              src="{% if photo_count == 1 %}{{ gallery_fallback }}{% else %}{{ transparent_pixel }}{% endif %}"
              {% if photo_count == 1 %}
                srcset="{{ gallery_jpg_srcset }}"
                loading="eager"
                fetchpriority="high"
              {% else %}
                data-src="{{ gallery_fallback }}"
                data-srcset="{{ gallery_jpg_srcset }}"
                loading="lazy"
              {% endif %}
              sizes="{{ gallery_sizes }}"
              decoding="async"
              alt="Photo reel image {{ photo_count }}">
          </picture>
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
      {% assign light_jpg_640 = '/optimized/material/light-640.jpg' | relative_url %}
      {% assign light_jpg_1024 = '/optimized/material/light-1024.jpg' | relative_url %}
      {% assign light_webp_640 = '/optimized/material/light-640.webp' | relative_url %}
      {% assign light_webp_1024 = '/optimized/material/light-1024.webp' | relative_url %}
      {% assign dark_jpg_640 = '/optimized/material/dark-640.jpg' | relative_url %}
      {% assign dark_jpg_1024 = '/optimized/material/dark-1024.jpg' | relative_url %}
      {% assign dark_webp_640 = '/optimized/material/dark-640.webp' | relative_url %}
      {% assign dark_webp_1024 = '/optimized/material/dark-1024.webp' | relative_url %}
      {% capture light_jpg_srcset %}{{ light_jpg_640 }} 640w, {{ light_jpg_1024 }} 1024w{% endcapture %}
      {% capture light_webp_srcset %}{{ light_webp_640 }} 640w, {{ light_webp_1024 }} 1024w{% endcapture %}
      {% capture dark_jpg_srcset %}{{ dark_jpg_640 }} 640w, {{ dark_jpg_1024 }} 1024w{% endcapture %}
      {% capture dark_webp_srcset %}{{ dark_webp_640 }} 640w, {{ dark_webp_1024 }} 1024w{% endcapture %}
      <picture>
        <source
          type="image/webp"
          sizes="{{ hero_sizes }}"
          data-theme-source
          data-light-srcset="{{ light_webp_srcset }}"
          data-dark-srcset="{{ dark_webp_srcset }}"
          srcset="{{ light_webp_srcset }}">
        <source
          type="image/jpeg"
          sizes="{{ hero_sizes }}"
          data-theme-source
          data-light-srcset="{{ light_jpg_srcset }}"
          data-dark-srcset="{{ dark_jpg_srcset }}"
          srcset="{{ light_jpg_srcset }}">
        <img
          src="{{ light_jpg_640 }}"
          srcset="{{ light_jpg_srcset }}"
          sizes="{{ hero_sizes }}"
          width="1024"
          height="683"
          loading="eager"
          decoding="async"
          alt="Portrait of Ryunosuke Abe"
          data-theme-image
          data-light-src="{{ light_jpg_640 }}"
          data-dark-src="{{ dark_jpg_640 }}"
          data-light-srcset="{{ light_jpg_srcset }}"
          data-dark-srcset="{{ dark_jpg_srcset }}">
      </picture>
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
