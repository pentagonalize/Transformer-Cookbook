# Transformer Cookbook

This repository is synced with the [Transformer Cookbook Overleaf project](https://www.overleaf.com/read/jysmqmhpvpwn#1c6afe).

# What's Cooking? 

Informally, this is an initiative within the [FLaNN](https://flann.super.site/) community to make a "recipe-book" for transformer
Formally, this is a collection of algorithmic constructions that we can show transformers are able to implement (in theory).
Many of these constructions have been used in a series of work that has shown lower bounds on the expressivity of transformers (See [the survey](https://arxiv.org/abs/2311.00208)), however, their proofs lay scattered around the appendices of different papers. We think a centralized collection of everything we've proven transformers can do, alongisde the constructions, will be useful for researchers. 

This collection will be cover constructions implementable in unique hard attention, average hard attention, and the standard softmax attention transformer. The exact details on what we consider an "implementable construction" will be fleshed out as the project unfolds. The scope will be limited to theoretical constructions and not empirical observations. That is, we'll only talk about what algorithms we can engineer into transformers, not what algorithms people have been able to reverse-engineer from transformers. 

# How can I contribute?

Feel free to make a pull request! For other suggestions and to get more involved, email me [ayang4@nd.edu](mailto:ayang4@nd.edu) and I can add you to our discord server. 