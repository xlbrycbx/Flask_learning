from flask import Blueprint, render_template, request, redirect, url_for

from apps.user.model import User

user_bp = Blueprint('user',__name__)

users=[]
@user_bp.route('/')
def user_center():
    print(url_for('user.user_register'))

    return render_template('user/show.html',users=users)

@user_bp.route('/register', methods=['GET','POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')

        if password == repassword:
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')

            user = User(username, password, phone)
            users.append(user)

            return redirect('/')
    else:
        return render_template('user/register.html')

@user_bp.route('/del')
def del_user():
    username = request.args.get('username')
    for user in users:
        if username == user.username:
            users.remove(user)
            # return render_template('user/show.html',users=users)
            return redirect('/')
    else:
        return '删除失败'


@user_bp.route('/login', methods=['GET','POST'])
def user_login():

    return '用户登录'

@user_bp.route('/logout', methods=['GET','POST'])
def user_logout():

    return '用户退出'