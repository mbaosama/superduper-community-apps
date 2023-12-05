<p align="center">
  <a href="https://www.superduperdb.com">
    <img width="90%" src="https://raw.githubusercontent.com/SuperDuperDB/superduperdb/main/docs/hr/static/img/SuperDuperDB_logo_color.svg">
  </a>
</p>
<div align="center">

# Bring AI to your favorite database! 

</div>

<div align="center">

## <a href="https://superduperdb.github.io/superduperdb/"><strong>Docs</strong></a> | <a href="https://docs.superduperdb.com/blog"><strong>Blog</strong></a> | <a href="https://docs.superduperdb.com/docs/category/use-cases"><strong>Use-Cases</strong></a> | <a href="https://demo.superduperdb.com/user-redirect/lab/tree/examples"><strong> Jupyter Live Demo</strong></a> | <a href="https://join.slack.com/t/superduperdb/shared_invite/zt-1zuojj0k0-RjAYBs1TDsvEa7yaFGa6QA"><strong> Slack </strong></a> | <a href="https://www.youtube.com/channel/UC-clq9x8EGtQc6MHW0GF73g"><strong> Youtube </strong></a>

</div>


<p align="center">
	<a href="https://github.com/superduperdb/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache_2.0-green" alt="License - Apache 2.0"></a>		
  <a href="https://github.com/superduperdb/superduperdb/actions"><img src="https://github.com/superduperdb/superduperdb/workflows/CI/badge.svg" alt="CI"></a>
  <a href="https://codecov.io/gh/superduperdb/superduperdb/branch/main"><img src="https://codecov.io/gh/superduperdb/superduperdb/branch/main/graph/badge.svg" alt="Coverage"></a>
  <a href="https://pypi.org/project/superduperdb"><img src="https://img.shields.io/pypi/v/superduperdb?color=%23007ec6&label=pypi%20package" alt="Package version"></a>
  <a href="https://pypi.org/project/superduperdb"><img src="https://img.shields.io/pypi/pyversions/superduperdb.svg" alt="Supported Python versions"></a>      	
  <a href="https://twitter.com/superduperdb" target="_blank"><img src="https://img.shields.io/twitter/follow/nestframework.svg?style=social&label=Follow @SuperDuperDB"></a>
</p>


---


<div align="center">	

 `🔮 SuperDuperDB is open-source: Please leave a star ⭐️ to support the project!`
 </div>


---

# SuperDuperDB Examples & Use-Cases

Welcome to the SuperDuperDB Examples repository! Here, you'll find a collection of diverse use-cases showcasing the capabilities of SuperDuperDB, from notebook demos to full-fledged applications.

## Community Use-Cases

### [Building a Semantic Search Engine](https://github.com/SuperDuperDB/superduper-community-apps/tree/main/apps/ecommerce_semantic_search_app)

This Semantic Search Engine was developed with the following objectives:

- Utilizing Superduperdb to create a practical business use case of a vector database using MongoDB as the backend.
- Comparing the differences between a basic Semantic search engine and a simple Full-Text Search Engine.

**Basic Components Used:**
- **Backend:** MongoDB
- **Embedding:** OpenAI
- **Vector Search Functionality:** SuperduperDB
- **Frontend:** Streamlit


### [Implementing Chunked Vector Search with Multiple Inputs per Document](https://github.com/SuperDuperDB/superduper-community-apps/blob/main/notebooks/chunked_vector_search.ipynb)

Let's find specific text within documents using vector-search. In this example, we show how to do vector-search. But here, we want to go one step further. Let's search for smaller pieces of text within larger documents. For instance, a developer may store entire documents but wants to find specific parts or references inside those documents.

Here we will show you an example with Wikipedia dataset. Implementing this kind of search is usually more complex, but with superduperdb, it's just one extra command.

Real-life use cases for the described problem of searching for specific text within documents using vector-search with smaller text units.

In each of these scenarios, the ability to efficiently search for and retrieve smaller text units within larger documents can significantly enhance data analysis and retrieval capabilities.

### [Image features](https://github.com/SuperDuperDB/superduper-community-apps/blob/main/notebooks/resnet_features.ipynb)

#### Building an Image Feature Database in torchvision

In this example, we show how to utilize a pre-trained network from torchvision to produce image features. The images are automatically fetched and stored in MongoDB. We use a subset of the CoCo dataset (https://cocodataset.org/#home) to illustrate the process.

Real-life use cases for creating a database of image features using a pre-trained network in torchvision:

Use Case: Enhance image search capabilities in e-commerce platforms.
How: Generate image features for products using a pre-trained network. Store these features in a database for efficient image retrieval, making it easier for users to find similar products.
Content-Based Recommendation Systems:

Use Case: Improve content recommendations in media streaming services.
How: Extract image features from movie or show frames. Store these features in a database to recommend content with similar visual characteristics to users based on their preferences.
Facial Recognition in Security Systems:

Use Case: Strengthen facial recognition systems in security applications.
How: Utilize a pre-trained neural network to extract facial features from images. Store these features in a database for quick and accurate identification in security and surveillance scenarios.
Medical Image Analysis:

Use Case: Streamline image organization in photo libraries or social media platforms.
How: Extract features from uploaded images using a pre-trained model. Use these features to automatically generate relevant tags, making it easier for users to search and categorize their photos.
These use cases demonstrate how creating a database of image features using torchvision can be applied across various domains to enhance functionality and improve user experiences.

### [Sentiment analysis](https://github.com/SuperDuperDB/superduper-community-apps/blob/main/notebooks/sentiment_analysis_use_case.ipynb)
Sentiment analysis with transformers and SuperDuperDB

In this document, we're doing sentiment analysis using Hugging Face's transformers library. We demonstrate that you can perform this task seamlessly in SuperDuperDB, using MongoDB to store the data.

Sentiment analysis has some real-life use cases:

Customer Feedback & Review Analysis: Analyzing customer

 reviews and feedback to understand overall satisfaction, identify areas for improvement, and respond to customer concerns. It is used in the E-commerce industry frequently.

Brand Monitoring: Monitoring social media, blogs, news articles, and online forums to gauge public sentiment towards a brand, product, or service. Addressing negative sentiment and capitalizing on positive feedback.

Sentiment analysis plays a crucial role in understanding and responding to opinions and emotions expressed across various domains, contributing to better decision-making and enhanced user experiences.

All of these can be done with your existing database and SuperDuperDB. You can integrate similar code into your ETL infrastructure as well. Let's see an example.

______________________________________________________________

## 🚀 Submit Your Community App and Get Featured!

Have you built an exciting app using SuperDuperDB that you want to showcase to the community? We'd love to feature it here!

### How to Submit:

1. **Create a Pull Request:**
   Fork this repository, add details about your app to the README.md, and create a pull request.

2. **Include Information:**
   Make sure to include details such as the purpose of your app, components used, a brief description, and any unique features.

3. **Add Contact Information:**
   Provide a way for the community to reach out to you, whether it's through GitHub, email, or any preferred communication channel.

4. **Highlight Your Contributions:**
   If your app uses specific features of SuperDuperDB or integrates with other technologies, highlight those contributions.

### Benefits of Submission:

- **Community Recognition:**
  Your app will be showcased in the SuperDuperDB community, giving you visibility and recognition.

- **Connect with Others:**
  Connect with fellow developers, share insights, and collaborate on potential improvements or extensions to your app.

- **Contribute to the Ecosystem:**
  Contribute to the growth of the SuperDuperDB ecosystem by sharing your innovative applications with the community.

Let's build an inspiring collection of community apps together! 🔥


# Contributing

There many ways to contribute, and they are not limited to creating community apps for us. We welcome all contributions. Read our [contributing](https://github.com/SuperDuperDB/examples/blob/main/CONTRIBUTING.md) guideline.

# Code of Conduct

This repository is part of the SuperDuperDB, thus the SuperDuperDB [Code of Conduct](https://github.com/SuperDuperDB/examples/blob/main/CODE_OF_CONDUCT.md) applies.

# License

SuperDuperDB is open-source and intended to be a community effort, and it wouldn't be possible without your support and enthusiasm. It is distributed under the terms of the Apache 2.0 license. Any contribution made to this project will be subject to the same provisions.

## More Information

For more details about the SuperDuperDB framework and its impressive functionality, visit the main open-source repository [here](https://bit.ly/sdexamples).
