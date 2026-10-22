# 公開停止と作業再開

2026-10-23（日本時間）に、ユーザーの依頼で GitHub Pages の公開設定を解除し、公開用ワークフローを無効化しました。

- リポジトリ: `ryuuua/rryuua`
- 公開URL: `https://ryuuua.github.io/rryuua/`
- 配信ワークフロー: `.github/workflows/jekyll-gh-pages.yml` / ID `193267302`
- 配信ワークフロー状態: `disabled_manually`
- 作業保存ブランチ: `codex/site-paused-20261023`（ローカル）
- 停止前の設定と確認結果: `2026-10-23/`
- リポジトリ、画像、履歴、日英対応の作業内容は保持。リモートへのソース変更は行っていません。

GitHub Pages API の解除結果は HTTP 204、その後の設定取得は HTTP 404 でした。解除直後にはCDNに以前のページが残る場合があります。公開URLの実測結果は `2026-10-23/status.json` を参照してください。

## 編集作業だけを再開する

```sh
cd /Users/ryua/code/rryuua
git switch codex/site-paused-20261023
```

日本語ホームは `index.md`、英語ホームは `en/index.md`。全ページの対応表はリポジトリ直下の `README.md` にあります。日英それぞれの本文・項目を独立して編集できます。

実装済み: 9組・18ページ、対応ページ間の言語切替、同じ言語内のナビゲーション、表示モードと操作ラベルの切替、対応ページがない場合のホームへの誘導。前回はJekyllビルドとPlaywrightで幅320〜1440px、言語切替、履歴、再読み込み、モバイルメニュー、テーマ維持、JavaScript無効時を確認しました。日英対応は本番には未反映です。

前回のローカルプレビューサーバーは停止しています。このMacでは同梱Ruby gemがIntel用のため、次の方法でプレビューを再生成できます（GitHubへの配信は行いません）。

```sh
GEM_HOME="$PWD/vendor/bundle/ruby/2.6.0" \
GEM_PATH="$PWD/vendor/bundle/ruby/2.6.0" \
JEKYLL_NO_BUNDLER_REQUIRE=true \
arch -x86_64 ruby vendor/bundle/ruby/2.6.0/gems/jekyll-4.3.4/exe/jekyll \
  build --destination /tmp/rryuua-bilingual-preview/rryuua --disable-disk-cache

python3 -m http.server 4177 --bind 127.0.0.1 --directory /tmp/rryuua-bilingual-preview
```

ブラウザーで `http://127.0.0.1:4177/rryuua/` を開きます。終了は Ctrl+C。通常の `bundle exec` は既存のGemfileとインストール済み依存関係の不一致で通らなかったため、上記は前回成功したローカル手順です。

## 公開を再開する場合

以下は再公開が明示的に依頼されたときだけ実行します。「編集作業の再開」だけでは実行しません。

1. 公開する内容を確認し、必要な変更を `main` に反映します。日英対応のローカルブランチをそのまま保存しているだけでは、リモートの `main` には入りません。
2. `gh api repos/ryuuua/rryuua/pages` で現在の設定を確認します。引き続き404なら、保存した設定を使ってPagesを再作成します。

```sh
gh api --method POST repos/ryuuua/rryuua/pages \
  --input _ops/publication-pause/2026-10-23/restore-pages.json
gh api --method PUT repos/ryuuua/rryuua/pages -F https_enforced=true
gh workflow enable jekyll-gh-pages.yml --repo ryuuua/rryuua
gh workflow run jekyll-gh-pages.yml --repo ryuuua/rryuua --ref main
```

3. Actionsの配信成功と、公開URLが意図した内容を返すことを確認します。過去の `pages-build-deployment` は停止前から残っている旧動的ワークフローで、今回の復元では操作不要です。

復元用JSONは `build_type: workflow` と `source: main /` のみを含みます。独自ドメインは設定されていませんでした。

参考: [GitHub Pages REST API](https://docs.github.com/en/rest/pages/pages#create-a-github-pages-site)。公開解除には同APIの `DELETE /repos/{owner}/{repo}/pages` を使用しています。
