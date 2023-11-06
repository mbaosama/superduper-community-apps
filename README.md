# SuperDuperDB Examples & Use-Cases
This repo contains a collection of SuperDuperDB use-cases ranging notebook demo to apps demo. Below are the list of use-cases
- **Movie Sentiment analysis of IMBD review.** Find [here](https://github.com/SuperDuperDB/examples/blob/main/contrib/sentiment_analysis_use_case.ipynb)

  **Technologies used:** MongoDB, HuggingFace , SuperDuperDB

  **Things to note when running:** You may need to install the following library  

   ```
   !pip install accelerate -U
   ```

- **Transcribing , Vector searching & asking questions based on audio recordings.** Find [here](https://github.com/SuperDuperDB/examples/blob/main/contrib/voice_memos.ipynb).

  **Technologies used:** MongoDB, OpenAI, SuperDuperDB, Facebook Transformers

   **Things to note when running:** You may need to install the following libraries 
  ```
  !pip install --upgrade transformers 
  !pip install soundfile librosa
  !pip install sentencepiece
  ```

- **Preprocessing and storing images features for images in the database.** Find [here](https://github.com/SuperDuperDB/examples/blob/main/contrib/resnet_features.ipynb)

    **Technologies used:** MongoDb, SuperDuperDB, torchvision

    **Things to note when running:** Remember to  uncomment the code below in cell 2 in order to download the code
    ```
    !curl -O https://superduperdb-public.s3.eu-west-1.amazonaws.com/valsmall2014.zip
    ```


- **Chuncking larging documents and vector searching for substrings within the document.** Find [here](https://github.com/SuperDuperDB/examples/blob/main/contrib/chunked_vector_search.ipynb)


    **Technologies used:** MongoDB, OpenAI and SuperDuperDB

    **Things to note when running:** Remember to add the OPENAPI key in cell 1 like this
    ```
    os.environ['OPENAI_API_KEY'] = <OPENAPI>
    ```

- **Ecommerce search engine web app.** Find [here](https://github.com/SuperDuperDB/examples/tree/main/contrib/ecommerce_semantic_search_app)

    **Technologies used:** MongoDB, OpenAI, SuperDuperDB, Streamlit

    **Things to note when running:** Find how to kickstart in the Readme [here](https://github.com/SuperDuperDB/examples/blob/main/contrib/ecommerce_semantic_search_app/README.md)

For more info about SuperDuperDB framework and its awesome functionality, check the main open-source repo [here](https://bit.ly/sdexamples)