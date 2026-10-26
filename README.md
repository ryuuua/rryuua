# Ryunosuke Abe — personal website

公開の停止・再開手順は [`_ops/publication-pause/README.md`](_ops/publication-pause/README.md) に記録しています。

Jekyllで生成する個人サイトです。日本語と英語の本文は別々のMarkdownファイルで管理し、自動翻訳や同期は行いません。文章、段落、項目、掲載情報を言語ごとに自由に編集できます。

## 編集するファイル

| ページ | 日本語 | 英語 |
| --- | --- | --- |
| ホーム | `index.md` | `en/index.md` |
| 自己紹介ページ | — | `en/about.md` |
| プロジェクト | `projects.md` | `en/projects.md` |
| CEBRA NLP | `projects/cebra-nlp.md` | `en/projects/cebra-nlp.md` |
| 論文 | `publications.md` | `en/publications.md` |
| 経歴 | `cv.md` | `en/cv.md` |
| ブログ | `blog.md` | `en/blog.md` |
| 計算環境 | `mathcluster.md` | `en/mathcluster.md` |
| 写真 | `infra-photos.md` | `en/infra-photos.md` |

日本語ホームの内容は `index.md` の4項目（名前・所属、学歴・経歴、主な研究関心、論文・発表）で編集します。英語ホームは `en/index.md` を編集します。日本語版には自己紹介ページを設けていません。

既存のURLは日本語版、`/en/` 以下は英語版です。`baseurl: /rryuua` の場合、ホームは `/rryuua/` と `/rryuua/en/` になります。ヘッダーの言語切替で対応するページへ移動し、メニューやホームへのリンクも選択中の言語を維持します。JavaScriptを無効にしても言語切替を利用できます。

## 新しいページ・片方の言語だけのページ

対応するページでは先頭の `translation_key` を同じ値にし、`lang` と `permalink` を言語ごとに設定します。

```yaml
---
layout: page
title: 新しいページ
lang: ja
translation_key: new-page
permalink: /new-page/
---
```

英語版は `en/new-page.md` に作成し、`lang: en`、`permalink: /en/new-page/` とします。`translation_key: new-page` は共通です。

片方の言語だけにページを作ることもできます。対応するページがないときは、言語切替に「ホームへ」または「home」と表示し、その言語のホームへ移動します。対応ページのないURLを生成することはありません。

記事も `lang` と `translation_key` を指定してください。ホームの記事一覧には、その言語の記事だけが表示されます。現在のRSSフィードは両言語を含む共通フィードです。

## 共通UI・画像

- `_data/i18n.yml`: 各言語のメニュー、ホーム内の目次、フッター、操作ラベル。ナビゲーションの `key` はページの `translation_key` に対応します。掲載順や項目も言語別に変更できます。
- ホームの項目を追加・削除する場合は、該当言語の `sections` も編集してください。`id` と本文のセクションIDを揃えます。
- `_includes/home-gallery.html` と `_includes/home-portrait.html`: 共有する画像表示。各ホームの include に渡すキャプションや代替テキストは言語別に編集できます。
- `_config.yml`: URL、サイト名、各言語の既定の検索用説明文。ページごとの `description` で上書きできます。

既存の `preview.html` と `cebra-nlp-standalone.html` は単独HTMLの参考ページです。公開サイトの言語別コンテンツは上表のMarkdownで編集してください。

## 閲覧数の記録

このサイトのJekyllページでは、Cloudflare Web Analyticsでページ別の閲覧数を確認できます。GitHub Pagesの配信先やDNSを変更する必要はありません。[Cloudflareの設定手順](https://developers.cloudflare.com/web-analytics/get-started/)に従い、Web Analyticsにホスト名 `ryuuua.github.io` を追加してください。

Cloudflareの「Manage site」に表示されるスニペットの `data-cf-beacon` の `token` を `_config.yml` の `cloudflare_web_analytics_token` に設定済みです。本番用にビルドして再公開すると、CloudflareのWeb Analytics画面で「Page views」を確認できます。ブラウザーで計測スクリプトがブロックされる場合があるため、閲覧数は概数です。通常のローカルプレビュー（development）では計測しません。計測開始前の閲覧数は遡って取得できません。

公開設定の変更履歴は [`_ops/publication-pause/README.md`](_ops/publication-pause/README.md) を参照してください。

## ローカル確認

通常のJekyll環境では `bundle install` 後に `bundle exec jekyll serve` を実行し、`http://127.0.0.1:4000/rryuua/` を開きます。ビルドは `bundle exec jekyll build` です。

変更時には両言語のホーム・下層ページ・スマートフォン幅で、言語切替、同言語内のリンク、メニュー、ライト／ダークモードを確認してください。
