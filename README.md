## Multi-task Learning for Sexism Detection on Tweets

### Overview

This repository contains the code and data for the project "Multi-task Learning for Sexism Detection on Tweets". The project explores the use of multi-task learning to improve the performance of sexism detection models on Twitter data.

### Data

The data used in this project is the [EDOS dataset](https://github.com/rewire-online/edos), which is a collection of English-language posts from Gab and Reddit that have been annotated for sexism. The dataset contains a total of 10,000 posts, which are divided into a training set, a development set, and a test set.

### Model

The model used in this project is a multi-task convolutional neural network (CNN) with BERT-based text embedding. The model is trained on the EDOS dataset using a custom hierarchical loss workflow.


### Data Description

The EDOS dataset is a collection of English-language posts from Gab and Reddit that have been annotated for sexism. The dataset contains a total of 10,000 posts, which are divided into a training set, a development set, and a test set.

Each post in the dataset is annotated with a binary label indicating whether or not the post is sexist. In addition, posts that are labeled as sexist are also annotated with a category of sexism (threats, derogation, animosity, or prejudiced discussion) and a fine-grained vector of sexism. The fine-grained vector of sexism is a 11-dimensional vector that captures different aspects of sexism, such as whether the post is misogynistic, homophobic, or racist.

The EDOS dataset is a valuable resource for researchers working on the development of automated tools for the detection and explanation of online sexism. The dataset is challenging, but it is also realistic and representative of the types of sexist content that users may encounter online.
