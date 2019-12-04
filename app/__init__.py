# #####核心app初始文件#####
from flask import Flask


def create_app():
    """
    创建核心对象
    """
    # 实例化 Flask()
    app = Flask(__name__)
    # 由于生产环境不允许使用测试模式，所以我们在开启测试模式要使用配置文件进行修改
    # 导入配置文件
    app.config.from_object('config')
    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
