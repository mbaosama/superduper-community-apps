import pandas as pd
import re

def get_image_url(input_string):
    """
    Get the URL string which  contains'_01_' in the list of URL strings
    """
    urls = input_string.split('~')
    filtered_urls = [url for url in urls if re.search(r'_01_', url)]
    if len(filtered_urls) ==0:
        results = 'None'
    else:
        results = filtered_urls[0]

    return results



def data_transformation(file_path):
    """
    Gets CSV Path and transforms it to a record of dictionaries
    
    """
    df = pd.read_csv(file_path)
    df = df.loc[:,['name', 'color', 'description', 'images', 'category']]
    data = df.drop_duplicates()
    data = data.groupby('name',as_index=False).agg({'color': ', '.join, 'description':'first','category':'first', 'images':'first'})
    data['images'] = data.apply(lambda x: get_image_url(x['images']), axis=1)
    data = data[data['images']!='None']
    data['description'] = data['description'] + 'In '+ data['color']
    return data.to_dict(orient='records')


if __name__ == '__main__':
    FILE_PATH = 'data/adidas_usa.csv'
    data_dic = data_transformation(FILE_PATH)
    print(data_dic[:2])
