import ast
import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import warnings
warnings.filterwarnings("ignore")

ES_HOSTS = ['http://localhost:9200']
FILE_PATH = 'test.json'
INDEX_NAME = "1"
DOC_TYPE = "_doc"

with open(FILE_PATH, 'r') as f:
    metric_doc = json.load(f)

for metric in metric_doc:
    metric['_index'] = INDEX_NAME
    metric['_type'] = DOC_TYPE
    metric['_id'] = metric['id']
    metric['nameLength'] = len(metric['displayName'])

es = Elasticsearch(hosts=ES_HOSTS, version="7.10.2")

if es.indices.exists(index=INDEX_NAME):
    print("Deleting the existing index " + str(INDEX_NAME))
    es.indices.delete(index=INDEX_NAME)

mapping_str = (
    "{'properties':{"
    + "    'name':{"
    + "        'type':'text',"
    + "        'fields':{"
    + "            'exact':{"
    + "                'type':'keyword'"
    + "            },"
    + "            'normalize':{"
    + "                'type':'keyword',"
    + "                'normalizer': 'lowercase_normalizer'"
    + "            }"
    + "        },"
    + "        'analyzer':'drive_metric_analyzer'"
    + "    },'displayName':{"
    + "        'type':'text',"
    + "        'fields':{"
    + "            'exact':{"
    + "                'type':'keyword'"
    + "            },"
    + "            'normalize':{"
    + "                'type':'keyword',"
    + "                'normalizer': 'lowercase_normalizer'"
    + "            }"
    + "        },"
    + "        'analyzer':'drive_metric_analyzer'"
    + "    },'metricName':{"
    + "        'type':'text',"
    + "        'analyzer':'keyword'"
    + "    }"
    + "}}"
)
mapping = ast.literal_eval(mapping_str)

# Define the index settings
settings = {
    "settings": {
        "analysis": {
            "analyzer": {
                "drive_metric_analyzer": {
                    "type": "custom",
                    "tokenizer": "whitespace",
                    "filter": [
                        "lowercase",
                        "finance_synonym",
                        "special_char_filter"
                    ]
                }
            },
            "filter": {
                "finance_synonym": {
                    "type": "synonym",
                    "synonyms": [
                        "stock,share,equity",
                        "bond,debt",
                        "bull,bear",
                        "asset,possession",
                        "capital,resources",
                        "earnings,revenue",
                        "interest,dividend",
                        "liquidity,solvency",
                        "market,industry",
                        "risk,volatility",
                        "value,worth",
                        "debt,obligation",
                        "credit,financing",
                        "equity,net worth",
                        "investment,savings",
                        "market,economy",
                        "profit,gain",
                        "hr,people",
                        "rate,charge",
                        "return,yield",
                        "security,collateral"
                    ]
                },
                "special_char_filter": {
                    "type": "word_delimiter_graph",
                    "preserve_original": True
                }
            },
            "normalizer": {
                "lowercase_normalizer": {
                    "type": "custom",
                    "filter": [
                        "lowercase"
                    ]
                }
            }
        }
    }
}

# Create the index with the mapping and settings
es.indices.create(index=INDEX_NAME, body={
    "mappings": mapping,
    **settings
})
es.indices.open(index=INDEX_NAME)
print("Created new index " + str(INDEX_NAME))

print("Starting bulk write to index total docs " + str(len(metric_doc)))
bulk(es, metric_doc)
print("Sucesfully updated the index with dump")
