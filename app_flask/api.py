from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import ssl

app = Flask(__name__)

ELASTIC_PASSWORD = "EjZC5k4FiUu70FvUYXUHkI1M"
CLOUD_ID = "Tutorial:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJDcwOGUyODI1ODUzODQzNmI5ZjRlMjI1ZGE2MTIxMTQ1JDFhNTA5MjA0NzA5MzRjNDViOGQ5ZmY2ZDMyNTVlZGMz"

con = Elasticsearch(cloud_id=CLOUD_ID,
                    basic_auth=("elastic", ELASTIC_PASSWORD), 
                    ssl_version=ssl.TLSVersion.TLSv1_2, 
                    verify_certs=False
                    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        results = request.form['search']
        query_body = {"size": 10000,
                        "query": {
                            "bool": {
                            "must": [
                                {"term": {
                                "Type.keyword": results
                                }}
                            ]
                            }
                        }
                    }
        resp = con.search(index="cards", body=query_body)
        valor = [doc['_source'] for doc in resp['hits']['hits']]
        largo = len(valor)
        return render_template('index.html', total = largo, values = valor[:10]) 
    
    return render_template('index.html')
    

if __name__== "__main__":
    app.run(debug = True)