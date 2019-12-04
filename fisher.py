from app import create_app

app = create_app()

# 入口文件——生产环境 nginx + uwsgi，不会启用 flask 自带的服务器
if __name__ == '__main__':
    # debug=True——打开调试模式，更改代码就可以不用总重启
    # host='0.0.0.0'——可以让外网访问
    # app.config['DEBUG']——1是dict的子类
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
