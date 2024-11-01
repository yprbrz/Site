from bson import ObjectId
from .mongodb import get_db
import random
import string


class MongoModel:
    collection_name = ''  # Spécifie le nom de la collection

    @classmethod
    def get_collection(cls):
        db = get_db()
        return db[cls.collection_name]

    @classmethod
    def insert(cls, data):
        collection = cls.get_collection()
        return collection.insert_one(data).inserted_id

    @classmethod
    def find(cls, query={}):
        collection = cls.get_collection()
        documents = collection.find(query)
        # Convertir ObjectId en chaîne pour chaque document
        result = []
        for doc in documents:
            doc['_id'] = str(doc['_id'])  # Conversion de ObjectId en str
            result.append(doc)
        return result

    @classmethod
    def update(cls, query, data):
        collection = cls.get_collection()
        return collection.update_one(query, {'$set': data})

    @classmethod
    def delete(cls, query):
        collection = cls.get_collection()
        return collection.delete_one(query)


class User(MongoModel):
    collection_name = 'users'

    @classmethod
    def create_user(cls, username, password):
        data = {
            "username": username,
            "password": password
        }
        return cls.insert(data)

    @classmethod
    def create_multiple_users(cls, count=100):
        users = []
        for i in range(1, count + 1):
            username = f"user{i}"
            password = f"password{i}"
            users.append({"username": username, "password": password})

        collection = cls.get_collection()
        result = collection.insert_many(users)
        return result.inserted_ids

    @classmethod
    def get_user(cls, user_id):
        query = {"_id": ObjectId(user_id)}
        users = cls.find(query)
        return users[0] if users else None

    @classmethod
    def get_users(cls):
        users = cls.find()
        return users if users else None

    @classmethod
    def update_user(cls, user_id, new_data):
        query = {"_id": ObjectId(user_id)}
        return cls.update(query, new_data)

    @classmethod
    def delete_user(cls, user_id):
        query = {"_id": ObjectId(user_id)}
        return cls.delete(query)
