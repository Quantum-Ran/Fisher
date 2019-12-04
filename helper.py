def is_isbn_or_keyword(query):
    """
    判断是否是isbn或者是关键字
    :return:
    """
    if len(query) == 13 and query.isdisgit():
        isbn_or_keyword = 'isbn'

    if '-' in query:
        short_query = query.replace('-', '')
        if len(short_query) == 10 and short_query.isdisgit():
            isbn_or_keyword = 'isbn'
    isbn_or_keyword = 'keyword'
    return isbn_or_keyword
