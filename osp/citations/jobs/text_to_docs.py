

from osp.common.config import config
from osp.citations.models import Text
from osp.citations.models import Citation


def text_to_docs(text_id):

    """
    Query a text against the OSP corpus.

    Args:
        text_id (int): A text row id.
    """

    row = Text.get(Text.id==text_id)


    doc_ids = set()
    for tokens in row.queries:

        # Execute the query.
        results = config.es.search(

            index='document',
            timeout=30,

            body={
                'size': 100000,
                'filter': {
                    'query': {
                        'match_phrase': {
                            'body': {
                                'query': ' '.join(tokens),
                                'slop': 5,
                            }
                        }
                    }
                }
            }

        )

        # Register the doc ids.
        if results['hits']['total'] > 0:
            for hit in results['hits']['hits']:
                doc_ids.add(int(hit['_id']))


    # Build doc -> text links.
    citations = []
    for doc_id in doc_ids:

        citations.append({
            'document': doc_id,
            'text': row.id,
            'tokens': ['TODO'],
        })

    # Bulk-insert the results.
    if citations:
        Citation.insert_many(citations).execute()
