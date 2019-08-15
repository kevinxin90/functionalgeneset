import requests


def load_data(data_folder):
    url = 'http://mygene.info/v3/query?q=_exists_:pathway&fields=pathway&fetch_all=TRUE'
    cnt = 0
    total = 1
    pathway_ids = set()
    while cnt < total:
        doc = requests.get(url).json()
        total = doc['total']
        cnt += len(doc['hits'])
        print('current cnt {}'.format(cnt))
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
                               'name': record['name']}
