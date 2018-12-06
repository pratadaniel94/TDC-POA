from pymongo import MongoClient

def connect_mongodb():
    try:
        con = MongoClient()
        return con['tdc'] 
    except Exception as e:
        return e
