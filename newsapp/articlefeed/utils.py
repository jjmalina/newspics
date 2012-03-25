import re


def normalize_query(query):
    """
    If the query contains spaces, replace them with +
    If the query contains a hashtag, replace with emptystring
    """
    query = query.replace(' ', '+')
    if re.search(query, '#'):
        query = query.replace('#', '')
    return query