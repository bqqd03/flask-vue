import json

from flask import redirect, request, url_for, flash, jsonify
from flask_login import logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from .. import db
from ..models import User



@auth.route('/login', methods=['POST'])
def login():
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    uid = json_data.get("uid")
    password = json_data.get("password")
    user = User.query.filter_by(uid=uid).first()
    if user is None:
        return jsonify({'code': 400, 'msg': '没有该用户'})
    if not check_password_hash(user.password, password):
        return jsonify({'code': 400, 'msg': '密码错误'})
    return jsonify({'code': 200, 'msg': 'ok', 'token': user.role})


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已注销')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['POST'])
def register():
    uid = request.json.get('uid')
    username = request.json.get('username')
    password = request.json.get('password')
    phone = request.json.get('phone')
    email = request.json.get('email')
    role = request.json.get('role')
    password = generate_password_hash(password)
    print('ok')
    user = User(uid=uid,
                username=username,
                password=password,
                phone=phone,
                email=email,
                role=role)
    db.session.add(user)
    db.session.commit()
    return jsonify({'code': 200})
