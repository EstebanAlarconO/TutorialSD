from time import sleep
from elasticsearch import Elasticsearch
import ssl
import random

busquedas = ('Trap Card', 'Normal Monster', 'Flip Effect Monster', 'Effect Monster', 'Spell Card', 'Tuner Monster', 'Token', 'Synchro Monster', 
'XYZ Monster', 'Pendulum Effect Monster', 'Fusion Monster', 'Normal Tuner Monster', 'Spirit Monster', 'Union Effect Monster', 'Ritual Monster', 
'Ritual Effect Monster', 'Gemini Monster', 'Toon Monster', 'Pendulum Normal Monster', 'Pendulum Flip Effect Monster', 'Synchro Tuner Monster', 
'XYZ Pendulum Effect Monster', 'Pendulum Tuner Effect Monster', 'Synchro Pendulum Effect Monster')


ELASTIC_PASSWORD = "EjZC5k4FiUu70FvUYXUHkI1M"
CLOUD_ID = "Tutorial:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDcwOGUyODI1ODUzODQzNmI5ZjRlMjI1ZGE2MTIxMTQ1JDFhNTA5MjA0NzA5MzRjNDViOGQ5ZmY2ZDMyNTVlZGMz"

con = Elasticsearch(cloud_id=CLOUD_ID,
                    basic_auth=("elastic", ELASTIC_PASSWORD), 
                    ssl_version=ssl.TLSVersion.TLSv1_2, 
                    verify_certs=False
                    )

if __name__== "__main__":

    while True:
        carta = random.choice(busquedas)
        query_body = {"size": 10000,
                        "query": {
                            "bool": {
                            "must": [
                                {"term": {
                                "Type.keyword": carta
                                }}
                            ]
                            }
                        }
                    }

        resp = con.search(index="cards", query=query_body)
        valor = [doc['_source'] for doc in resp['hits']['hits']]
        print(valor[:10])
        sleep(10)