---
layout: page
title: Mathcluster
lang: en
translation_key: mathcluster
permalink: /en/mathcluster/
---

<div class="page-stack">
  <section class="card">
    <h2>Overview</h2>
    <p>
      This page is a public-facing overview of the compute systems I manage. It is
      meant to sit between a lab profile and an operations notebook: enough detail
      to explain what each machine is for, how the system is shaped, and what I care
      about when I build or maintain it.
    </p>
    <p>
      The private and operational source of truth lives in the <code>mathcluster</code>
      repository. This page will stay lighter and more narrative than the repo itself.
    </p>
  </section>

  <div class="grid-2">
    <article class="card">
      <h2>What To Publish Here</h2>
      <ul>
        <li>High-level node roles and how I divide work across them</li>
        <li>Hardware snapshots: CPU, memory, GPU, storage, and network highlights</li>
        <li>Operational preferences: Docker-first paths, monitoring, and recovery design</li>
        <li>Short notes on why a given machine exists and what it is good at</li>
      </ul>
    </article>

    <article class="card">
      <h2>Source Notes</h2>
      <ul>
        <li><code>mathcluster/targets.yaml</code> for public targets, access profiles, and queue profiles</li>
        <li><code>mathcluster/env_info/env_status.json</code> for current hardware snapshots</li>
        <li><code>mathcluster/monitoring/headnode/README.md</code> for monitoring and recovery notes</li>
        <li><code>mathcluster/monitoring/env4/README.md</code> for host-local exporter structure</li>
      </ul>
    </article>
  </div>

  <section class="card">
    <h2>Public Targets</h2>
    <p>
      Fill this table from <code>targets.yaml</code> and <code>env_status.json</code>.
      Keep it public-facing: role, strengths, and character first; exact operational
      details only when they are safe to publish.
    </p>
    <div class="spec-table-wrap">
      <table class="spec-table">
        <thead>
          <tr>
            <th>Target</th>
            <th>Role</th>
            <th>Compute</th>
            <th>Memory</th>
            <th>Accelerators</th>
            <th>Notes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>env1</strong></td>
            <td>Primary workstation / large local jobs</td>
            <td>TBD from mathcluster</td>
            <td>TBD</td>
            <td>TBD</td>
            <td>Why this machine exists, and what kinds of experiments belong here.</td>
          </tr>
          <tr>
            <td><strong>env2</strong></td>
            <td>Secondary compute node</td>
            <td>TBD from mathcluster</td>
            <td>TBD</td>
            <td>TBD</td>
            <td>Include any special storage, networking, or monitoring role.</td>
          </tr>
          <tr>
            <td><strong>env3</strong></td>
            <td>Storage-adjacent or shared-data node</td>
            <td>TBD from mathcluster</td>
            <td>TBD</td>
            <td>TBD</td>
            <td>Good place to explain shared disks, throughput, or data locality.</td>
          </tr>
          <tr>
            <td><strong>env4</strong></td>
            <td>Specialized local node</td>
            <td>TBD from mathcluster</td>
            <td>TBD</td>
            <td>TBD</td>
            <td>Highlight what makes this machine distinct from the others.</td>
          </tr>
          <tr>
            <td><strong>cc21</strong></td>
            <td>Batch / queue-based compute</td>
            <td>TBD from queue profiles</td>
            <td>TBD</td>
            <td>TBD</td>
            <td>Summarize the queue model and what workloads should go there.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="card">
    <h2>Design Choices</h2>
    <div class="highlight-grid">
      <div class="highlight">
        <h3>Docker-first execution</h3>
        <p>
          Explain why local nodes prefer containerized execution and what that buys in
          terms of reproducibility, cleanup, and user safety.
        </p>
      </div>
      <div class="highlight">
        <h3>Storage and network topology</h3>
        <p>
          Summarize how fast local storage, shared storage, and direct links fit
          together without turning this page into an admin manual.
        </p>
      </div>
      <div class="highlight">
        <h3>Monitoring and recovery</h3>
        <p>
          Describe the observability stack, exporter strategy, and the kinds of failure
          modes you care about catching early.
        </p>
      </div>
    </div>
  </section>

  <section class="card">
    <h2>What I Care About</h2>
    <div class="timeline">
      <div class="timeline-item">
        <span class="period">Reliability</span>
        <h3>Recovery paths should be explicit</h3>
        <p>
          Placeholder for notes on restarts, backup paths, and keeping key services
          restorable after reboots or hardware changes.
        </p>
      </div>
      <div class="timeline-item">
        <span class="period">Observability</span>
        <h3>Metrics should explain behavior, not just decorate dashboards</h3>
        <p>
          Placeholder for notes on exporter choices, storage accounting, and what
          signals you actually watch.
        </p>
      </div>
      <div class="timeline-item">
        <span class="period">Pragmatism</span>
        <h3>Each node should have a clear job</h3>
        <p>
          Placeholder for the philosophy behind separating workstation, storage,
          and queue-based roles across the cluster.
        </p>
      </div>
    </div>
  </section>
</div>
