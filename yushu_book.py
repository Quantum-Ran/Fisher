from http import HTTP


class YuShuBook:

    def __init__(self):
        self.isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
        self.keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        # dict
        result = HTTP.get(url)
        return result

    def search_by_keyword(self, keyword, count=15, start=0):
        url = self.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
