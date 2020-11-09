# import datetime
#
# from flask import render_template, request, jsonify
# from flask_login import current_user
#
# from . import student
# from .. import db
# from ..models import Danxuan, Duoxuan, Tiankong, Jianda, Score, Exam, User, Paper, Question
#
#
# @student.route('/index/')
# def index():
#     return render_template('student/index.html')
#
#
# @student.route('/exam/')
# def stu_myexam():
#     return render_template('student/stu_MyExam.html')
#
#
# @student.route('/exam_data/')
# def exam_data():
#     uid = current_user.get_id()
#     p = User.query.get(uid)  # type:Profile
#     exam_list = Exam.query.filter().all()
#     data = []
#     for i in exam_list:
#         data.append(i.to_json())
#     return jsonify(data)
#
#
# @student.route('/examing/<int:id>')
# def examing(id):
#     e = Exam.query.get(id)  # type:Exam
#     now_time = datetime.datetime.now()
#     if now_time < e.s_time:
#         return render_template('error_time.html', error_info='考试还未开始')
#     elif now_time > e.e_time:
#         return render_template('error_time.html', error_info='考试已结束')
#     timu_dict = eval(e.paper.timu_id)
#     timu = ''
#     if '单选' in timu_dict.keys():
#         danxuanl = Danxuan.query.filter(Danxuan.id.in_(timu_dict['单选'])).all()
#         if '多选'in timu_dict.keys():
#             duoxuanl = Duoxuan.query.filter(Duoxuan.id.in_(timu_dict['多选'])).all()
#             if '填空'in timu_dict.keys():
#                 tiankongl = Tiankong.query.filter(Tiankong.id.in_(timu_dict['填空'])).all()
#                 if '简答' in timu_dict.keys():
#                     jiandal = Jianda.query.filter(Jianda.id.in_(timu_dict['简答'])).all()
#                     return render_template('student/stu_examing.html', timu=timu, exam=e, danxuanl=danxuanl,duoxuanl=duoxuanl, tiankongl=tiankongl,jiandal=jiandal)
#                 return render_template('student/stu_examing.html', timu=timu, exam=e, danxuanl=danxuanl, duoxuanl=duoxuanl, tiankongl=tiankongl)
#             return render_template('student/stu_examing.html', timu=timu, exam=e, danxuanl=danxuanl, duoxuanl=duoxuanl)
#         return render_template('student/stu_examing.html', timu=timu, exam=e,danxuanl=danxuanl)
#
#
# @student.route('/examing_data/<string:exam_name>', methods=['GET', 'POST'])
# def examing_data(exam_name):
#     form = request.form
#     print(form)
#     tl = [i for i in form]
#     print(tl)
#     tikul = Question.query.filter(Question.id.in_(tl)).all()
#     # 获取题目答案
#     ans_dict = {str(t.id): {'answer': t.answer, 'fenlei': t.fenlei, 'score': t.score} for t in tikul}
#     stu_dict = {i: ','.join(form.getlist(i)) for i in tl}
#     stu_dict = dict(sorted(stu_dict.items(), key=lambda x: x[0]))
#     stu_score = 0.0
#     error_lst = []
#     for k, v in stu_dict.items():
#         timu = ans_dict[k]
#         if timu['answer'].lower().strip() == stu_dict[k].lower().strip():
#             stu_score += int(timu['score'])
#         else:
#             # 将错题记录
#             error_lst.append(k)
#     s = Score(id=0, exam_name=exam_name, uid=current_user.get_id(), stu_name=current_user.get_name(), score=stu_score)
#     try:
#         db.session.add(s)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('成绩添加或错题添加出错 %s' % e)
#         return 'error'
#
#
# @student.route('/score/')
# def stu_score():
#     return render_template('student/stu_MyScore.html')
#
#
# @student.route('/score_data/')
# def score_data():
#     score_list = Score.query.filter_by(uid=current_user.id).all()
#     data = []
#     for i in score_list:  # type:Score
#         data.append(i.to_json())
#     return jsonify(data)
#
#
#
