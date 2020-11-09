from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.String(128), unique=True, primary_key=True)
    username = db.Column(db.String(128), index=True)
    password = db.Column(db.String(128), index=True)
    phone = db.Column(db.String(128), unique=True, index=True)
    email = db.Column(db.String(128), unique=True, index=True)
    role = db.Column(db.String(128), index=True)

    def __init__(self, uid, username, password, phone, email, role):
        self.uid = uid
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email
        self.role = role

    def to_json(self):
        json_data = {
            'uid': self.uid,
            'username': self.username,
            'password': self.password,
            'phone': self.phone,
            'email': self.email,
            'role': self.role
        }
        return json_data

class Tixing(db.Model):
    __tablename__ = 'tixing'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)


    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_json(self):
        json_data = {
            'id': self.id,
            'name': self.name,
        }
        return json_data

class Danxuan(db.Model):
    __tablename__ = 'danxuan'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    optionsA = db.Column(db.String(64), index=True)
    optionsB = db.Column(db.String(64), index=True)
    optionsC = db.Column(db.String(64), index=True)
    optionsD = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64), index=True)
    analysis = db.Column(db.String(64), index=True)
    label = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)
    degree = db.Column(db.String(64), index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'question': self.question,
            'ans_a': self.optionsA,
            'ans_b': self.optionsB,
            'ans_c': self.optionsC,
            'ans_d': self.optionsD,
            'answer': self.answer,
            'analysis': self.analysis,
            'label': self.label,
            'type': self.type,
            'degree': self.degree
        }
        return json_data



class Duoxuan(db.Model):
    __tablename__ = 'duoxuan'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    optionsA = db.Column(db.String(64), index=True)
    optionsB = db.Column(db.String(64), index=True)
    optionsC = db.Column(db.String(64), index=True)
    optionsD = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64), index=True)
    analysis = db.Column(db.String(64), index=True)
    label = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)
    degree = db.Column(db.String(64), index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'question': self.question,
            'ans_a': self.optionsA,
            'ans_b': self.optionsB,
            'ans_c': self.optionsC,
            'ans_d': self.optionsD,
            'answer': self.answer,
            'analysis': self.analysis,
            'label': self.label,
            'type': self.type,
            'degree': self.degree,
        }
        return json_data

    def get_ans(self):
        data = {
            'id': self.answer
        }
        return data


class Tiankong(db.Model):
    __tablename__ = 'tiankong'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64), index=True)
    analysis = db.Column(db.String(64), index=True)
    label = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)
    degree = db.Column(db.String(64), index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'analysis': self.analysis,
            'label': self.label,
            'type': self.type,
            'degree': self.degree,
        }
        return json_data

    def get_ans(self):
        data = {
            'id': self.answer
        }
        return data


class Jianda(db.Model):
    __tablename__ = 'jianda'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64), index=True)
    analysis = db.Column(db.String(64), index=True)
    label = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)
    degree = db.Column(db.String(64), index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'analysis': self.analysis,
            'label': self.label,
            'type': self.type,
            'degree': self.degree,
        }
        return json_data

    def get_ans(self):
        data = {
            'id': self.answer
        }
        return data


class Panduan(db.Model):
    __tablename__ = 'pandaun'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64), index=True)
    analysis = db.Column(db.String(64), index=True)
    label = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)
    degree = db.Column(db.String(64), index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'analysis': self.analysis,
            'label': self.label,
            'type': self.type,
            'degree': self.degree,
        }
        return json_data

    def get_ans(self):
        data = {
            'id': self.answer
        }
        return data


class Zonghe(db.Model):
    __tablename__ = 'zonghe'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(64), index=True)
    answer = db.Column(db.String(64), index=True)
    analysis = db.Column(db.String(64), index=True)
    label = db.Column(db.String(64), index=True)
    type = db.Column(db.String(64), index=True)
    degree = db.Column(db.String(64), index=True)

    def to_json(self):
        json_data = {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'analysis': self.analysis,
            'label': self.label,
            'type': self.type,
            'degree': self.degree,
        }
        return json_data

    def get_ans(self):
        data = {
            'id': self.answer
        }
        return data

# class Paper(db.Model):
#     __tablename__ = 'paper'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True, index=True)
#     timu_id = db.Column(db.String(255), index=True)
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'name': self.name,
#             'paper_id': self.timu_id
#         }
#         return json_data
#
#
# class Exam(db.Model):
#     __tablename__ = 'exam'
#
#     id = db.Column(db.Integer, primary_key=True)
#     exam_name = db.Column(db.String(255))
#     exam_paper = db.Column(db.ForeignKey('paper.name', ondelete='RESTRICT', onupdate='RESTRICT'), index=True,nullable=False)
#     s_time = db.Column(db.DateTime)
#     e_time = db.Column(db.DateTime)
#     paper = db.relationship('Paper', primaryjoin='Exam.exam_paper == Paper.name', backref='exam')
#
#     def __init__(self, id, exam_name, exam_paper, s_time, e_time):
#         self.id = id
#         self.exam_name = exam_name
#         self.exam_paper = exam_paper
#         self.s_time = s_time
#         self.e_time = e_time
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'exam_name': self.exam_name,
#             'exam_paper': self.exam_paper,
#             's_time': self.s_time.strftime('%Y-%m-%d %H:%M:%S'),
#             'e_time': self.e_time.strftime('%Y-%m-%d %H:%M:%S'),
#         }
#         return json_data
#
#
# class Score(db.Model):
#     __tablename__ = 'score'
#
#     id = db.Column(db.Integer, primary_key=True)
#     exam_name = db.Column(db.String(64), index=True)
#     uid = db.Column(db.String(64), index=True)
#     stu_name = db.Column(db.String(64), index=True)
#     score = db.Column(db.String(64), index=True)
#
#     def __init__(self, id, exam_name, uid, stu_name, score):
#         self.id = id
#         self.exam_name = exam_name
#         self.uid = uid
#         self.stu_name = stu_name
#         self.score = score
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'exam_name': self.exam_name,
#             'uid': self.uid,
#             'stu_name': self.stu_name,
#             'score': self.score
#         }
#         return json_data
#
#
# class Exam_Danxuan(db.Model):
#     __tablename__ = 'exam_danxuan'
#
#     id = db.Column(db.Integer, primary_key=True)
#     correct = db.Column(db.String(64), index=True)
#     error = db.Column(db.String(64), index=True)
#     stu_id = db.Column(db.String(64), index=True)
#     exam_id = db.Column(db.String(64), index=True)
#
#     def __init__(self, id, correct, error, stu_id, exam_id):
#         self.id = id
#         self.correct = correct
#         self.error = error
#         self.stu_id = stu_id
#         self.exam_id = exam_id
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'correct': self.correct,
#             'error': self.error,
#             'stu_id': self.stu_id,
#             'exam_id': self.exam_id
#         }
#         return json_data
#
#
# class Exam_Duoxuan(db.Model):
#     __tablename__ = 'exam_duoxuan'
#
#     id = db.Column(db.Integer, primary_key=True)
#     correct = db.Column(db.String(64), index=True)
#     error = db.Column(db.String(64), index=True)
#     stu_id = db.Column(db.String(64), index=True)
#     exam_id = db.Column(db.String(64), index=True)
#
#     def __init__(self, id, correct, error, stu_id, exam_id):
#         self.id = id
#         self.correct = correct
#         self.error = error
#         self.stu_id = stu_id
#         self.exam_id = exam_id
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'correct': self.correct,
#             'error': self.error,
#             'stu_id': self.stu_id,
#             'exam_id': self.exam_id
#         }
#         return json_data
#
#
# class Exam_Tiankong(db.Model):
#     __tablename__ = 'exam_tiankong'
#
#     id = db.Column(db.Integer, primary_key=True)
#     correct = db.Column(db.String(64), index=True)
#     error = db.Column(db.String(64), index=True)
#     stu_id = db.Column(db.String(64), index=True)
#     exam_id = db.Column(db.String(64), index=True)
#
#     def __init__(self, id, correct, error, stu_id, exam_id):
#         self.id = id
#         self.correct = correct
#         self.error = error
#         self.stu_id = stu_id
#         self.exam_id = exam_id
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'correct': self.correct,
#             'error': self.error,
#             'stu_id': self.stu_id,
#             'exam_id': self.exam_id
#         }
#         return json_data
#
# class Exam_Jianda(db.Model):
#     __tablename__ = 'exam_jianda'
#
#     id = db.Column(db.Integer, primary_key=True)
#     correct = db.Column(db.String(64), index=True)
#     error = db.Column(db.String(64), index=True)
#     stu_id = db.Column(db.String(64), index=True)
#     exam_id = db.Column(db.String(64), index=True)
#
#     def __init__(self, id, correct, error, stu_id, exam_id):
#         self.id = id
#         self.correct = correct
#         self.error = error
#         self.stu_id = stu_id
#         self.exam_id = exam_id
#
#     def to_json(self):
#         json_data = {
#             'id': self.id,
#             'correct': self.correct,
#             'error': self.error,
#             'stu_id': self.stu_id,
#             'exam_id': self.exam_id
#         }
#         return json_data


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
