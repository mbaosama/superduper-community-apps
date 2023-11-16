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

## Use-Cases

### 1. Movie Sentiment Analysis of IMDB Reviews
- **Demo Notebook:** [Movie Sentiment Analysis](https://github.com/SuperDuperDB/examples/blob/main/contrib/sentiment_analysis_use_case.ipynb)
- **Technologies used:** MongoDB, HuggingFace, SuperDuperDB
- **Note:** Ensure you have the required libraries installed by running:
  
  ```bash
  pip install accelerate -U
  ```

### 2. Transcribing, Vector Searching & Asking Questions based on Audio Recordings
- **Demo Notebook:** [Voice Memos](https://github.com/SuperDuperDB/examples/blob/main/contrib/voice_memos.ipynb)
- **Technologies used:** MongoDB, OpenAI, SuperDuperDB, Facebook Transformers
- **Note:** Install necessary libraries before running:
  
  ```bash
  pip install --upgrade transformers 
  pip install soundfile librosa
  pip install sentencepiece
  ```

### 3. Preprocessing and Storing Image Features in the Database
- **Demo Notebook:** [ResNet Features](https://github.com/SuperDuperDB/examples/blob/main/contrib/resnet_features.ipynb)
- **Technologies used:** MongoDB, SuperDuperDB, torchvision
- **Note:** Uncomment the code in cell 2 to download required data:
  
  ```bash
  curl -O https://superduperdb-public.s3.eu-west-1.amazonaws.com/valsmall2014.zip
  ```

### 4. Chunking Large Documents and Vector Searching for Substrings
- **Demo Notebook:** [Chunked Vector Search](https://github.com/SuperDuperDB/examples/blob/main/contrib/chunked_vector_search.ipynb)
- **Technologies used:** MongoDB, OpenAI, SuperDuperDB
- **Note:** Add your OpenAI API key in cell 1:
  
  ```python
  os.environ['OPENAI_API_KEY'] = "<OPENAPI>"
  ```

### 5. E-commerce Search Engine Web App
- **Demo App:** [E-commerce Semantic Search App](https://github.com/SuperDuperDB/examples/tree/main/contrib/ecommerce_semantic_search_app)
- **Technologies used:** MongoDB, OpenAI, SuperDuperDB, Streamlit
- **Note:** Follow the instructions in the [Readme](https://github.com/SuperDuperDB/examples/blob/main/contrib/ecommerce_semantic_search_app/README.md) to kickstart the app.


# Contributing

There many ways to contribute, and they are not limited to creating community apps for us. We welcome all contributions. Read our [contributing](https://github.com/SuperDuperDB/superduper-community-apps/blob/main/CODE_OF_CONDUCT.md) guideline.

# Code of Conduct

This repository is part of the SuperDuperDB, thus the SuperDuperDB [Code of Conduct](https://github.com/SuperDuperDB/superduper-community-apps/blob/main/CONTRIBUTING.md) applies.

# License

SuperDuperDB is open-source and intended to be a community effort, and it wouldn't be possible without your support and enthusiasm. It is distributed under the terms of the Apache 2.0 license. Any contribution made to this project will be subject to the same provisions.

## More Information

For more details about the SuperDuperDB framework and its impressive functionality, visit the main open-source repository [here](https://bit.ly/sdexamples).
