from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
uri = "mongodb+srv://krishnavenichalla:KpTBH6OjEd4hoOus@atlascluster.hdu7pay.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.bank

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # inserting one account
    document_to_find = {
        "_id": ObjectId("663edc21285e54993213c40b")
    }

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.insert_one(document_to_find)

    pprint.pprint(result)


except Exception as e:
    print(e)
finally:
    client.close()