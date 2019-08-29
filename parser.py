import requests


def load_data(data_folder=None):
    # load pathways
    url = 'http://mygene.info/v3/query?q=_exists_:pathway&fields=pathway&fetch_all=TRUE'
    cnt = 0
    total = 1
    pathway_ids = set()
    while cnt < total:
        doc = requests.get(url).json()
        if total == 1:
            total = doc['total']
        cnt += len(doc['hits'])
        url = 'http://mygene.info/v3/query?scroll_id=' + doc['_scroll_id']
        for _doc in doc['hits']:
            for db, info in _doc['pathway'].items():
                if isinstance(info, dict):
                    info = [info]
                for record in info:
                    _id = db + ':' + str(record['id'])
                    if _id not in pathway_ids:
                        pathway_ids.add(_id)
                        yield {'_id': _id,
                               db: record['id'],
                               'name': record['name'],
                               'type': 'pathway'}
    # load biological process
    url = 'http://mygene.info/v3/query?q=_exists_:go.BP&fields=go.BP&fetch_all=TRUE'
    cnt = 0
    total = 1
    pathway_ids = set()
    while cnt < total:
        doc = requests.get(url).json()
        total = doc['total']
        cnt += len(doc['hits'])
        url = 'http://mygene.info/v3/query?scroll_id=' + doc['_scroll_id']
        for _doc in doc['hits']:
            info = _doc['go']['BP']
            if isinstance(info, dict):
                info = [info]
            for record in info:
                _id = record['id']
                if _id not in pathway_ids:
                    pathway_ids.add(_id)
                    yield {'_id': _id,
                           'go': _id,
                           'name': record['term'],
                           'type': 'bp'}
    # load molecular function
    url = 'http://mygene.info/v3/query?q=_exists_:go.MF&fields=go.MF&fetch_all=TRUE'
    cnt = 0
    total = 1
    pathway_ids = set()
    while cnt < total:
        doc = requests.get(url).json()
        total = doc['total']
        cnt += len(doc['hits'])
        url = 'http://mygene.info/v3/query?scroll_id=' + doc['_scroll_id']
        for _doc in doc['hits']:
            info = _doc['go']['MF']
            if isinstance(info, dict):
                info = [info]
            for record in info:
                _id = record['id']
                if _id not in pathway_ids:
                    pathway_ids.add(_id)
                    yield {'_id': _id,
                           'go': _id,
                           'name': record['term'],
                           'type': 'mf'}
    # load cellular component
    url = 'http://mygene.info/v3/query?q=_exists_:go.CC&fields=go.CC&fetch_all=TRUE'
    cnt = 0
    total = 1
    pathway_ids = set()
    while cnt < total:
        doc = requests.get(url).json()
        total = doc['total']
        cnt += len(doc['hits'])
        url = 'http://mygene.info/v3/query?scroll_id=' + doc['_scroll_id']
        for _doc in doc['hits']:
            info = _doc['go']['CC']
            if isinstance(info, dict):
                info = [info]
            for record in info:
                _id = record['id']
                if _id not in pathway_ids:
                    pathway_ids.add(_id)
                    yield {'_id': _id,
                           'go': _id,
                           'name': record['term'],
                           'type': 'cc'}
