import time
import datetime
import itertools
from pymongo import MongoClient

client = MongoClient()
db = client['docker-practice']

for i in itertools.count():
    post = {
        'count': i,
        'date': datetime.datetime.utcnow()
    }
    post_id = db.posts.insert_one(post).inserted_id

    print(f'Inserted a new document: {post_id}')
    time.sleep(5)
