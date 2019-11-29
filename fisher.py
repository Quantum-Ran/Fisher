from flask import Flask, make_response

# 实例化 Flask()
app = Flask(__name__)
# 由于生产环境不允许使用测试模式，所以我们在开启测试模式要使用配置文件进行修改
# 导入配置文件
app.config.from_object('config')


# #####定义视图函数#####

# 浏览器通过http请求来访为函数，访问的路径就是 路由
# 1 @app.route('/hello')——装饰器来注册路由
@app.route('/hello')
def hello():
    # 视图函数，除了返回字符串，还会返回
    # status code 200 404
    # content-type http header
    # 默认 content-type = text/html

    # 视图函数会返回，封装成 Response 对象
    headers = {
        'content-type': 'text/plain',
    }
    response = make_response('<html></ html>', 404)
    response.headers = headers
    return response
    # return 'hello'


# 2 对象注册路由，在基于类的视图（即插视图）必须用
# app.add_url_rule('/hello', view_func=hello)

# 入口文件——生产环境 nginx + uwsgi，不会启用 flask 自带的服务器
if __name__ == '__main__':
    # debug=True——打开调试模式，更改代码就可以不用总重启
    # host='0.0.0.0'——可以让外网访问
    # app.config['DEBUG']——1是dict的子类
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
