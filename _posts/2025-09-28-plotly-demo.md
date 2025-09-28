---
layout: post
title: "Plotlyデモ: インタラクティブ図を埋め込む"
---

GitHub PagesではHTMLブロックに直接Plotlyを記述して可視化できます。

<div id="plotly-demo" style="width:100%;max-width:800px;height:480px"></div>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script>
const x = Array.from({length: 100}, (_, i) => i/10);
const y = x.map(v => Math.sin(v));
Plotly.newPlot('plotly-demo', [ {x:x, y:y, mode:'lines', name:'sin(x)'} ], {margin:{t:20}});
</script>

> 注: 外部CDNにアクセスできる環境で表示されます。
