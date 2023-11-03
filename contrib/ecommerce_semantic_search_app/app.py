import streamlit as st
from PIL import Image
import pandas as pd
import requests
from io import BytesIO
import pymongo
import re
from transform_data import data_transformation
from store_and_convert_to_vector_index import search_functionality
from store_to_mongodb import connect_to_mongodb


file_path = 'data/adidas_usa.csv'


data_dic = data_transformation(file_path)

vector_db, vector_collection, model = search_functionality(data_dic)

full_text_db, full_text_collection = connect_to_mongodb(data_dic)



def search_vector_database(text):
    """
    Query through the vector database based on the text input
    Do a vector similarity based on the description or the name field and return the first 6 rows of the name, 
    color , image and description
    """
    cur = vector_db.execute(
    vector_collection
        .like({'description':text ,'name': text},  vector_index=f'adidas-index-{model.identifier}')
        .find({}, {'name': 1, 'color': 1,'images': 1 ,'description': 1})
        .sort([('_score', pymongo.DESCENDING)])  
        .limit(6)  
                         )
    return cur

def search_full_text(text):
    """
    Query through the classical database based on the text imput
    Query through the vector database based on the text input
    Do a vector similarity based on the description or the name field and return the first 6 rows of the name, 
    color , image and description 
    """
    results = full_text_collection.find({
    "$or": [
        {"description": {"$regex": text, "$options": "i"}},
        {"name": {"$regex": text, "$options": "i"}}
         ]
       }, projection={'name': 1, 'color': 1,'images': 1 , 'description': 1}
       ).limit(6)
    return results


def get_results_from_database(text):
    """
    Convert the results of two queries into dataframes
    
    """
    vector_results = search_vector_database(text)
    full_text_results = search_full_text(text)
    vector_list = [data.unpack() for data in vector_results]
    full_text_list = [data for data in full_text_results]
    df_vector = pd.DataFrame(vector_list)
    df_full_text = pd.DataFrame(full_text_list)
    return df_vector, df_full_text, vector_list





def home():
    """
    Main function to display the dashboard.
    """
         
    def get_results(data_data, col1, col2,list_name):
            """
            Display the dataframe in the following order
            - Name
            - Resize Image
            - Color
            - Description
            """
            for (index, row), name_col in zip(data_data.iloc[col1:col2, :].iterrows(), list_name):
                with name_col:
                    with st.container():
                        st.markdown(f"###### {row['name']}")
                        response = requests.get(row['images'])
                        image = Image.open(BytesIO(response.content))
                        width, height = 100, 100
                        image = image.resize((width, height))
                        st.image(image)
                        st.write(f"{row['color']}")
                        expander = st.expander("Description")
                        expander.write(f"{row['description']}")


    with st.form(key='searchform'):
        c1, c2 = st.columns((8,2), gap='large')
        with c1:
            search_text =  st.text_input("Search Bar 👇")
        with c2:
            st.write('\n')
            st.write('\n')
            search_button = st.form_submit_button('Submit', use_container_width=True)
        if search_button:
            df_vector, df_full_text, vector_list = get_results_from_database(search_text)
            with st.container():
                st.markdown(""" ## Results Using Semantic Searching Method""")
                if len(df_vector) == 0:
                    st.markdown('### No Results Found. Try modifying the search term')
                else:
                    c5, c6, c7 = st.columns(3)
                    list_name = [c5, c6, c7]
                    get_results(df_vector, 0, 3,list_name)
                    c8, c9, c10 = st.columns(3)
                    list_na = [c8, c9, c10]
                    get_results(df_vector, 3, 6,list_na)
            st.markdown("""---""")
            with st.container():
                st.markdown("""## Results Using Full-text Searching Method """)
                if len(df_full_text)==0:
                    st.markdown('### No Results Found. Try modifying the search term')
                else:
                    c5, c6, c7 = st.columns(3)
                    list_name = [c5, c6, c7]
                    get_results(df_full_text, 0, 3,list_name)
                    c8, c9, c10 = st.columns(3)
                    list_na = [c8, c9, c10]
                    get_results(df_full_text, 3, 6,list_na)
            


if __name__ == '__main__':
    st.set_page_config(page_title="Semantic Search VS Full-Text Search", page_icon="🧑‍🏭", layout='wide', initial_sidebar_state='expanded')
    st.sidebar.header('About Search Engine')
    st.sidebar.write("""
    This Search Engine was created to demo the different results between semantic search and Full-text search. The data used was sourced from [here](https://www.kaggle.com/datasets/thedevastator/adidas-fashion-retail-products-dataset-9300-prod/).
    Demo repo can be found [here](https://github.com/anitaokoh/building_a_semantic_search_engine_with_mongodb).
    """)
                 
    st.sidebar.markdown('''
    ---
    Created with ❤️ by [Anita](https://www.linkedin.com/in/anita-okoh/).
    ''')    
    st.title("🔔  Semantic Search VS Full-Text Search")
    home()