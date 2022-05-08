from flask import Blueprint

user_bp = Blueprint('user',__name__)

@user_bp.route('/')
def user_center():
    return '用户中心'

@user_bp.route('/register', methods=['GET','POST'])
def user_register():

    return '用户注册'

@user_bp.route('/login', methods=['GET','POST'])
def user_login():

    return '用户登录'

@user_bp.route('/logout', methods=['GET','POST'])
def user_logout():

    return '用户退出'