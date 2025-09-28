---
layout: home
title: Home
---

<section class="hero">
  <h1>Ryunosuke Abe</h1>
  <p class="subtitle">
    Graduate researcher blending natural language processing with neuroscience-inspired representation learning
    to uncover interpretable structure in high-dimensional embeddings.
  </p>
  <div class="meta">
    <span class="tag blue">NAIST · NLP Lab</span>
    <span class="tag green">Nonlinear ICA</span>
    <span class="tag pink">Identifiability</span>
  </div>
  <div class="meta" style="margin-top:1.4rem;">

    <a class="btn primary" href="{{ '/publications/' | relative_url }}">Read Publications</a>
    <a class="btn ghost" href="{{ '/projects/' | relative_url }}">Explore Projects</a>
    <a class="btn ghost" href="{{ '/cv/' | relative_url }}">Download CV</a>

  </div>
</section>

<section class="grid-2">
  <div>
    <article class="card">
      <h2>About</h2>
      <p>
        I am a master’s student at the Nara Institute of Science and Technology, advised by Prof. Takashi Ninomiya.
        My work lies at the intersection of computational linguistics and machine learning, where I design methods that
        reveal low-dimensional, meaningful factors inside massive language representations.
      </p>
      <p>
        I especially enjoy collaborating across disciplines—drawing from cognitive neuroscience to inform the structure of
        algorithms and collaborating with linguists to validate the interpretability of new embeddings.
      </p>
    </article>

    <article class="card">
      <h2>Research Focus</h2>
      <div class="highlight-grid">
        <div class="highlight">
          <h3>Neuroscience-guided embedding design</h3>
          <p>Adapting grid- and place-cell coding principles to organize linguistic spaces with geometric structure.</p>
        </div>
        <div class="highlight">
          <h3>Learning with auxiliary context</h3>
          <p>Extending nonlinear ICA (CEBRA) with contextual variables and contrastive objectives for robust alignment.</p>
        </div>
        <div class="highlight">
          <h3>Identifiability guarantees</h3>
          <p>Proving when InfoNCE-based training recovers consistent latent factors across datasets and random seeds.</p>
        </div>
      </div>
    </article>
  </div>

  <figure class="card profile-image">

    <img src="{{ '/assets/img/portrait.jpg' | relative_url }}" alt="Portrait of Ryunosuke Abe" class="responsive">

    <figcaption class="figure-note">
      Replace this placeholder by adding <code>assets/img/portrait.jpg</code> to the repository.
    </figcaption>
  </figure>
</section>

<section class="card">
  <h2>Recent Highlights</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="period">2024</span>
      <h3>Workshop talk on neuroscience-inspired representation learning</h3>
      <p>Presented a study on aligning transformer embeddings with hippocampal cell coding at an interdisciplinary meetup.</p>
    </div>
    <div class="timeline-item">
      <span class="period">2023</span>
      <h3>Launched collaboration with NAIST Cognitive Neuroscience Center</h3>
      <p>Initiated a joint project to evaluate language model representations against neural activity collected in VR experiments.</p>
    </div>
    <div class="timeline-item">
      <span class="period">2022</span>
      <h3>Undergraduate thesis on robust language grounding</h3>
      <p>Explored contrastive learning techniques that stabilize semantics across multilingual corpora and noisy modalities.</p>
    </div>
  </div>
</section>

<section class="card">
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

<section class="callout">
  <h2>Let’s build interpretable language intelligence.</h2>
  <p>
    I am open to research collaborations, visiting positions, and opportunities to present this work to diverse audiences.
    Reach out if you are exploring similar directions or want to co-design new experiments.
  </p>
  <a class="btn primary" href="mailto:ryunosuke.abe@example.com">Contact Me</a>
</section>
