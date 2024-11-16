import os
from pymongo import MongoClient
from dotenv import load_dotenv
import urllib.parse

class MongoDBClient:
    def __init__(self):
        """
        Initialize the MongoDB client using environment variables.
        """
        # Load environment variables
        load_dotenv()

        # Fetch MongoDB connection details
        mongo_db_url = os.getenv("MONGO_DB_URL")
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")

        # Ensure variables are present
        if not mongo_db_url or not username or not password:
            raise ValueError("Missing environment variables for MongoDB connection.")

        # URL-encode username and password
        username = urllib.parse.quote_plus(username)
        password = urllib.parse.quote_plus(password)

        # Construct the connection URL
        self.connection_url = mongo_db_url.replace(
            "mongodb+srv://", f"mongodb+srv://{username}:{password}@"
        )

        try:
            # Establish a connection
            self.client = MongoClient(self.connection_url)
            print("MongoDB connection established successfully.")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {e}")

    def list_databases(self):
        """
        List all databases in the MongoDB cluster.
        """
        try:
            databases = self.client.list_database_names()
            return databases
        except Exception as e:
            raise RuntimeError(f"Failed to list databases: {e}")


    def get_collection(self, database_name, collection_name):
        """
        Get a specific collection from a database.
        """
        try:
            db = self.client[database_name]
            collection = db[collection_name]
            return collection
        except Exception as e:
            raise RuntimeError(f"Failed to get collection: {e}")

    def insert_document(self, database_name, collection_name, document):
        """
        Insert a single document into a collection.
        """
        try:
            collection = self.get_collection(database_name, collection_name)
            result = collection.insert_one(document)
            return result.inserted_id
        except Exception as e:
            raise RuntimeError(f"Failed to insert document: {e}")

    def find_documents(self, database_name, collection_name, query={}):
        """
        Find documents in a collection based on a query.
        """
        try:
            collection = self.get_collection(database_name, collection_name)
            documents = collection.find(query)
            return list(documents)
        except Exception as e:
            raise RuntimeError(f"Failed to find documents: {e}")

    def update_document(self, database_name, collection_name, query, update_values):
        """
        Update a document in a collection.
        """
        try:
            collection = self.get_collection(database_name, collection_name)
            result = collection.update_one(query, {"$set": update_values})
            return result.modified_count
        except Exception as e:
            raise RuntimeError(f"Failed to update document: {e}")

    def delete_document(self, database_name, collection_name, query):
        """
        Delete a document from a collection.
        """
        try:
            collection = self.get_collection(database_name, collection_name)
            result = collection.delete_one(query)
            return result.deleted_count
        except Exception as e:
            raise RuntimeError(f"Failed to delete document: {e}")



