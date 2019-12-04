from flask import jsonify
from flask import Blueprint
from helper import is_isbn_or_keyword
from yushu_book import YuShuBook

# #####定义视图函数#####

# # 浏览器通过http请求来访为函数，访问的路径就是 路由
# # 1 @app.route('/hello')——装饰器来注册路由
# # @app.route('/hello')
# # def hello():
#     # 视图函数，除了返回字符串，还会返回
#     # status code 200 404
#     # content-type http header
#     # 默认 content-type = text/html
#     # 视图函数会返回，封装成 Response 对象
#     headers = {
#         'content-type': 'text/plain',
#     }
#     response = make_response('<html></ html>', 404)
#     response.headers = headers
#     return response
#     # return 'hello'
#
#
# # 2 对象注册路由，在基于类的视图（即插视图）必须用
# # app.add_url_rule('/hello', view_func=hello)


# 蓝图实例化
web = Blueprint('web', __name__)
web.route('/book/search/<query>/<page>')


def search(query, page):
    """
    搜索11
    """

    # API
    isbn_or_keyword = is_isbn_or_keyword(query)
    if isbn_or_keyword == 'isbn':
        result = YuShuBook().search_by_isbn(query)
    else:
        result = YuShuBook().search_by_keyword(query)
    return jsonify(result)
