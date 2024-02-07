from elasticsearch import Elasticsearch
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

import os


client = Elasticsearch(
    "https://localhost:9200",  # Elasticsearch endpoint
    ca_certs="ca.crt",
    basic_auth=("elastic", os.environ.get("ELASTIC_PASSWORD")),
)

doc = {
    "author": "author_name",
    "text": "Interensting content...",
    "timestamp": datetime.now(),
}
resp = client.index(index="test-index", document=doc)
print(resp["result"])
