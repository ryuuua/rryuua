---
layout: page
title: CEBRA NLP
permalink: /en/projects/cebra-nlp/
lang: en
translation_key: cebra-nlp
---

## Overview
A research project applying CEBRA, a nonlinear ICA framework, to language representation learning. It explores low-dimensional structures and semantic axes within embedding spaces, combining contrastive variables such as context, style, and task labels for stable nonlinear recovery and visualization.

## Background
- Existing LLM embeddings are high-dimensional and difficult to interpret, including when assessing transfer to downstream tasks.
- CEBRA has been used successfully in time-series and neural activity analysis, while applications to natural language remain less explored.
- Using nonlinear ICA to extract latent states relevant to language understanding may support analysis, control, and more robust conversational agents.

## Objectives
- Redesign and stabilize the CEBRA objective to incorporate context variables.
- Assess the interpretability of low-dimensional latent axes, including semantic categories, style, and emotion.
- Publish research logs and code to support reproducible analysis.

## Methods
1. Extract token or sentence embeddings from pretrained language models, including BERT and GPT models.
2. Use auxiliary variables such as sentiment, speaker attributes, and genre for contrastive learning.
3. Compare forward models and inverse mappings to evaluate latent-space stability and identification performance.
4. Combine UMAP/CEBRA plots with nearest-neighbor analysis to interpret latent axes.

## Datasets
- GLUE benchmarks for sentiment and natural language inference
- Labeled text such as MultiNLI, SST-2, and Yelp Review
- Auxiliary signals from self-supervised tasks on Wikipedia and CC-News

## Progress
- [x] Set up sentence embedding extraction and preprocessing
- [x] Implement the CEBRA loss and explore hyperparameters for stable training
- [ ] Evaluate latent axes on labeled data with linear classifiers and clustering
- [ ] Integrate multimodal conditions, such as speech transcripts
- [ ] Publish research notes and a visualization dashboard

## Outputs
- Code repository (in preparation)
- Experiment reports and visualization snapshots (planned for publication from private Notion notes)
- Conference paper: "Low-dimensional structure in language embeddings via CEBRA" (in preparation)

## Next Steps
- Additional experiments to measure generalization to low-resource languages
- Automatic interpretation of latent axes using measures of statistical independence
- Collaboration, especially in multimodal dialogue and information visualization
