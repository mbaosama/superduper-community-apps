import pymongo
import mongomock
from transform_data import data_transformation


database_name = "adidas_full_text_search_db"
collection_name = "adidas_full_text_search_collection"

def connect_to_mongodb(data):
    """
    Connect to MongoDB, get the specified database and collection objects, and return them.
    """
   
    with mongomock.MongoClient() as mongo_client:
        db = mongo_client[database_name]
        collection = db[collection_name]
        collection.insert_many(data)

    return db, collection




if __name__ == '__main__':
    file_path = 'adidas_usa.csv'
    data_dic = data_transformation(file_path)
    db, collection = connect_to_mongodb(data_dic)
    results = collection.find({
    "$or": [
        {"description": {"$regex": 'shoe', "$options": "i"}},
        {"name": {"$regex": 'shoe', "$options": "i"}}
         ]
       }, projection={'name': 1, 'color': 1,'images': 1 , 'description': 1}
       ).limit(6)
    for result in results:
        print(result)

