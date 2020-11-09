# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from datetime import timedelta
from flask_session import Session
import datetime

# 为了同时让视图函数与模型类用db
db = SQLAlchemy()
bootstrap = Bootstrap()
session = Session()
# 初始化实例
login_manager = LoginManager()
# 验证失败跳转的界面
login_manager.login_view = 'login_blue.login'
# 闪烁信息级别
login_manager.login_message_category = 'info'
# 用户重定向到登录页面时闪出的消息
login_manager.login_message = '请先登录'
# cookie 的默认有效期
login_manager.remember_cookie_duration = timedelta(days=1)


def init_app(app):
    # flask-sqlalchemy初始化
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    session.init_app(app)


def str2datetime(s: str, date_format='%Y-%m-%d %H:%M:%S'):
    """

    :param s: 时间字符串
    :param date_format: 格式化参数
    :return: datetime对象
    """
    dt = datetime.datetime.strptime(s, date_format)
    return dt
