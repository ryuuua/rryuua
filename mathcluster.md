---
layout: page
title: 計算環境
permalink: /mathcluster/
lang: ja
translation_key: mathcluster
published: false
---

<div class="page-stack">
  <section class="card">
    <h2>概要</h2>
    <p>
      管理している計算環境を紹介するページです。研究室の紹介と運用ノートの中間として、
      各マシンの用途、システム全体の構成、構築・保守で大切にしていることをまとめます。
    </p>
    <p>
      非公開の運用情報の正本は <code>mathcluster</code> リポジトリにあります。
      このページでは、構成の意図が伝わる簡潔な紹介を目指します。
    </p>
  </section>

  <div class="grid-2">
    <article class="card">
      <h2>掲載する情報</h2>
      <ul>
        <li>各ノードの役割と処理の分担</li>
        <li>CPU、メモリ、GPU、ストレージ、ネットワークの概要</li>
        <li>Dockerを基本とする実行経路、監視、復旧の設計方針</li>
        <li>各マシンを導入した理由と得意な処理</li>
      </ul>
    </article>
    <article class="card">
      <h2>参照元</h2>
      <ul>
        <li><code>mathcluster/targets.yaml</code>：公開ターゲット、アクセス設定、キュー設定</li>
        <li><code>mathcluster/env_info/env_status.json</code>：ハードウェアの状態記録</li>
        <li><code>mathcluster/monitoring/headnode/README.md</code>：監視・復旧のノート</li>
        <li><code>mathcluster/monitoring/env4/README.md</code>：ホスト内のエクスポーター構成</li>
      </ul>
    </article>
  </div>

  <section class="card">
    <h2>公開ターゲット</h2>
    <p>
      この表は <code>targets.yaml</code> と <code>env_status.json</code> をもとに記入する予定です。
      役割や強みを中心に紹介し、詳細な運用情報は公開できる範囲に限ります。
    </p>
    <div class="spec-table-wrap">
      <table class="spec-table">
        <thead>
          <tr><th>ターゲット</th><th>役割</th><th>計算資源</th><th>メモリ</th><th>アクセラレーター</th><th>備考</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>env1</strong></td><td>主力ワークステーション／大規模なローカル処理</td>
            <td>mathclusterから転記予定</td><td>未記入</td><td>未記入</td>
            <td>導入理由と、このマシンで行う実験を記載予定。</td>
          </tr>
          <tr>
            <td><strong>env2</strong></td><td>補助計算ノード</td>
            <td>mathclusterから転記予定</td><td>未記入</td><td>未記入</td>
            <td>ストレージ、ネットワーク、監視上の特徴を記載予定。</td>
          </tr>
          <tr>
            <td><strong>env3</strong></td><td>ストレージや共有データに近いノード</td>
            <td>mathclusterから転記予定</td><td>未記入</td><td>未記入</td>
            <td>共有ディスク、転送速度、データ配置について記載予定。</td>
          </tr>
          <tr>
            <td><strong>env4</strong></td><td>特定用途のローカルノード</td>
            <td>mathclusterから転記予定</td><td>未記入</td><td>未記入</td>
            <td>他のマシンとの違いを記載予定。</td>
          </tr>
          <tr>
            <td><strong>cc21</strong></td><td>バッチ／キュー方式の計算環境</td>
            <td>キュー設定から転記予定</td><td>未記入</td><td>未記入</td>
            <td>キューの仕組みと適した処理を記載予定。</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="card">
    <h2>設計の方針</h2>
    <div class="highlight-grid">
      <div class="highlight">
        <h3>Dockerを基本とする実行</h3>
        <p>ローカルノードでコンテナ実行を重視する理由と、再現性、後片付け、利用者の安全性への効果を記載予定です。</p>
      </div>
      <div class="highlight">
        <h3>ストレージとネットワークの構成</h3>
        <p>高速なローカルストレージ、共有ストレージ、直接接続をどう組み合わせるか、概要を記載予定です。</p>
      </div>
      <div class="highlight">
        <h3>監視と復旧</h3>
        <p>監視基盤、エクスポーターの方針、早期に検知したい障害を記載予定です。</p>
      </div>
    </div>
  </section>

  <section class="card">
    <h2>大切にしていること</h2>
    <div class="timeline">
      <div class="timeline-item">
        <span class="period">信頼性</span>
        <h3>復旧手順を明確にする</h3>
        <p>再起動、バックアップ経路、ハードウェア変更後の主要サービスの復旧について記載予定です。</p>
      </div>
      <div class="timeline-item">
        <span class="period">可観測性</span>
        <h3>挙動を理解するためのメトリクス</h3>
        <p>エクスポーターの選択、ストレージの使用状況、実際に注視する指標について記載予定です。</p>
      </div>
      <div class="timeline-item">
        <span class="period">実用性</span>
        <h3>各ノードの役割を明確にする</h3>
        <p>ワークステーション、ストレージ、キュー方式の処理を分担する考え方を記載予定です。</p>
      </div>
    </div>
  </section>
</div>
