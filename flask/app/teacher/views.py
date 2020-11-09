import json

import random

import xlrd
from flask import render_template, request, jsonify

from . import teacher
from .. import db
from ..extension import str2datetime
from ..models import Danxuan, Duoxuan, Tiankong, Jianda, Panduan, Zonghe#, Score, Exam, User, Paper


@teacher.route('/tiku_add', methods=['POST'])
def tiku_add():
    question = request.json.get('Question')
    optionA = request.json.get('Option_1')
    optionB = request.json.get('Option_2')
    optionC = request.json.get('Option_3')
    optionD = request.json.get('Option_4')
    answer = request.json.get('Answer')
    analysis = request.json.get('analysis')
    type = request.json.get('type')
    label = request.json.get('label')
    degree = request.json.get('Degree')
    if type == 1:
        t = Danxuan(question=question, optionsA=optionA, optionsB=optionB, optionsC=optionC, optionsD=optionD, answer=answer, analysis=analysis, label=label, type='单选', degree=degree)
    elif type == 2:
        x = ''
        for i in answer:
            x += i
        t = Duoxuan(question=question, optionsA=optionA, optionsB=optionB, optionsC=optionC, optionsD=optionD, answer=x, analysis=analysis, label=label, type='多选', degree=degree)
    elif type == 3:
        t = Tiankong(question=question, answer=answer, analysis=analysis, label=label, type='填空', degree=degree)
    elif type == 4:
        t = Panduan(question=question, answer=answer, analysis=analysis, label=label, type='判断', degree=degree)
    elif type == 5:
        t = Jianda(question=question, answer=answer, analysis=analysis, label=label, type='简答', degree=degree)
    elif type == 6:
        t = Zonghe(question=question, answer=answer, analysis=analysis, label=label, type='复合', degree=degree)
    db.session.add(t)
    db.session.commit()
    return jsonify({'code': 200})


@teacher.route('/tiku_data/', methods=['GET'])
def tiku_data():
    user_tiku_list1 = Danxuan.query.all()
    user_tiku_list2 = Duoxuan.query.all()
    user_tiku_list3 = Tiankong.query.all()
    user_tiku_list4 = Panduan.query.all()
    user_tiku_list5 = Jianda.query.all()
    user_tiku_list6 = Zonghe.query.all()
    data = []
    for i in user_tiku_list1:  # type:Tiku
        data.append(i.to_json())
    for i in user_tiku_list2:  # type:Tiku
        data.append(i.to_json())
    for i in user_tiku_list3:  # type:Tiku
        data.append(i.to_json())
    for i in user_tiku_list4:  # type:Tiku
        data.append(i.to_json())
    for i in user_tiku_list5:  # type:Tiku
        data.append(i.to_json())
    for i in user_tiku_list6:  # type:Tiku
        data.append(i.to_json())
    return jsonify({'code': 200, 'data' : data})


@teacher.route('/tiku_upload/', methods=['GET', 'POST'])
def tiku_upload():
    f = request.files.get('txt_file')
    f.save('./files/{}'.format('upload.xlsx'))
    f = xlrd.open_workbook('./files/upload.xlsx')
    table = f.sheet_by_index(0)
    nrows = table.nrows
    l = []
    for i in range(1, nrows):
        ti_l = table.row_values(i)  # type:list
        if ti_l[0] != '':
            while len(ti_l) > 10:
                ti_l.pop(-1)
            l.append(ti_l)
    for ll in l:
        if ll[8] == '单选':
            t = Danxuan(*ll)
        elif ll[8] == '多选':
            t = Danxuan(*ll)
        elif ll[4] == '填空':
            t = Danxuan(*ll)
        elif ll[4] == '判断':
            t = Danxuan(*ll)
        elif ll[4] == '简答':
            t = Danxuan(*ll)
        elif ll[4] == '复合':
            t = Danxuan(*ll)
        db.session.add(t)
        db.session.commit()
        return jsonify({'code': 200})


# @teacher.route('/exam/')
# def tea_exam():
#     paper_list = [i.name for i in Paper.query.all()]
#     return render_template('teacher/tea_exam.html', paper_list=paper_list)
#
#
# @teacher.route('/exam_data/')
# def exam_data():
#     exam_list = Exam.query.all()
#     data = []
#     for i in exam_list:  # type:Exam
#         data.append(i.to_json())
#     return jsonify(data)
#
#
# @teacher.route('/exam_add', methods=['GET', 'POST'])
# def exam_add():
#     exam_name = request.values.get('exam_name')
#     exam_paper = request.values.get('exam_paper')
#     s_time = str2datetime(request.values.get('s_time'), '%Y年%m月%d日 %H:%M:%S')
#     e_time = str2datetime(request.values.get('e_time'), '%Y年%m月%d日 %H:%M:%S')
#     e = Exam(id=0, exam_name=exam_name, exam_paper=exam_paper, s_time=s_time, e_time=e_time)
#     try:
#         db.session.add(e)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('考试增加出错 %s' % e)
#         db.session.rollback()
#         return 'error'
#
#
# @teacher.route('/exam_edit', methods=['GET', 'POST'])
# def exam_edit():
#     exam_id = request.values.get('edit_exam_id')
#     exam_name = request.values.get('edit_exam_name')
#     exam_paper = request.values.get('edit_exam_paper')
#     s_time = str2datetime(request.values.get('edit_s_time'))
#     e_time = str2datetime(request.values.get('edit_e_time'))
#     e = Exam.query.get(exam_id)  # type:Exam
#     e.exam_name = exam_name
#     e.exam_paper = exam_paper
#     e.s_time = s_time
#     e.e_time = e_time
#     try:
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('考试修改出错%s' % e)
#         return 'error'
#
#
# @teacher.route('/exam_del', methods=['GET', 'POST'])
# def exam_del():
#     # 一旦视图函数内涉及db.session的操纵，在函数内进行 from models import db即正常
#     id = request.values.get('id')
#     e = Exam.query.get(id)
#     try:
#         db.session.delete(e)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('考试删除出错%s' % e)
#         return 'error'
#
#
# @teacher.route('/paper/')
# def tea_paper():
#     return render_template('teacher/tea_paper.html')
#
#
# @teacher.route('/paper_data/')
# def paper_data():
#     paper_list = Paper.query.all()
#     data = []
#     for i in paper_list:  # type:Paper
#         data.append(i.to_json())
#     return jsonify(data)
#
#
# @teacher.route('/paper_add', methods=['GET', 'POST'])
# def paper_add():
#     papername = request.values.get('papername')
#     timu_leixing = request.values.get('timu_leixing')
#     timu_id = {}
#     print(timu_leixing)
#     tm_l = timu_leixing.split(',')
#     print(tm_l)
#     for tixing in tm_l:
#         if tixing == '单选':
#             l = Danxuan.query.filter().all()
#             l = [str(i.id) for i in l]
#             ll = random.sample(l, 3)
#         elif tixing == '多选':
#             l = Duoxuan.query.filter().all()
#             l = [str(i.id) for i in l]
#             ll = random.sample(l, 3)
#         elif tixing == '填空':
#             l = Tiankong.query.filter().all()
#             l = [str(i.id) for i in l]
#             ll = random.sample(l, 3)
#         elif tixing == '简答':
#             l = Jianda.query.filter().all()
#             l = [str(i.id) for i in l]
#             ll = random.sample(l, 1)
#         timu_id[tixing] = ll
#     p = Paper(id=0, name=papername, timu_id=str(timu_id))
#     try:
#         db.session.add(p)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('试卷增加出错 %s' % e)
#         db.session.rollback()
#         return 'error'
#
#
# @teacher.route('/paper_del', methods=['GET', 'POST'])
# def paper_del():
#     # 一旦视图函数内涉及db.session的操纵，在函数内进行 from models import db即正常
#     id = request.values.get('id')
#     p = Paper.query.get(id)
#     try:
#         db.session.delete(p)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('试卷删除出错%s' % e)
#         return 'error'
#
#
#
#
#
# @teacher.route('/tiku_del', methods=['GET', 'POST'])
# def tiku_del():
#     # 一旦视图函数内涉及db.session的操纵，在函数内进行 from models import db即正常
#     id = request.values.get('id')
#     fenlei = request.values.get('fenlei')
#     if fenlei =='单选':
#         p_timu_id = str(Paper.query.with_entities(Paper.timu_id).all())
#         t = Danxuan.query.get(id)
#     elif fenlei == '多选':
#         p_timu_id = str(Paper.query.with_entities(Paper.timu_id).all())
#         t = Duoxuan.query.get(id)
#     elif fenlei == '填空':
#         p_timu_id = str(Paper.query.with_entities(Paper.timu_id).all())
#         t = Tiankong.query.get(id)
#     elif fenlei == '简答':
#         p_timu_id = str(Paper.query.with_entities(Paper.timu_id).all())
#         t = Jianda.query.get(id)
#     if str(t.id) in p_timu_id:
#         return 'error'
#     try:
#         db.session.delete(t)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('题库删除出错%s' % e)
#         return 'error'
#
#
# @teacher.route('/tiku_edit', methods=['GET', 'POST'])
# def tiku_edit():
#     id = request.values.get('id')
#     question = request.values.get('question')
#     ans_a = request.values.get('ans_a')
#     ans_b = request.values.get('ans_b')
#     ans_c = request.values.get('ans_c')
#     ans_d = request.values.get('ans_d')
#     ans_e = request.values.get('ans_e')
#     answer = request.values.get('answer')
#     fenlei = request.values.get('fenlei')
#     kaodian = request.values.get('kaodian')
#     score = request.values.get('score')
#     if fenlei == '单选':
#         t = Danxuan.query.get(id)  # type:Tiku
#         t.question = question
#         t.ans_a = ans_a
#         t.ans_b = ans_b
#         t.ans_c = ans_c
#         t.ans_d = ans_d
#         t.answer = answer
#         t.fenlei = fenlei
#         t.kaodian = kaodian
#         t.score = score
#     elif fenlei == '多选':
#         t = Duoxuan.query.get(id)  # type:Tiku
#         t.question = question
#         t.ans_a = ans_a
#         t.ans_b = ans_b
#         t.ans_c = ans_c
#         t.ans_d = ans_d
#         t.ans_e = ans_e
#         t.answer = answer
#         t.fenlei = fenlei
#         t.kaodian = kaodian
#         t.score = score
#     elif fenlei == '填空':
#         t = Tiankong.query.get(id)  # type:Tiku
#         t.question = question
#         t.answer = answer
#         t.fenlei = fenlei
#         t.kaodian = kaodian
#         t.score = score
#     elif fenlei == '简答':
#         t = Jianda.query.get(id)  # type:Tiku
#         t.question = question
#         t.answer = answer
#         t.fenlei = fenlei
#         t.kaodian = kaodian
#         t.score = score
#     try:
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('题库修改出错%s' % e)
#         return 'error'
#
#
# @teacher.route('/score/')
# def tea_score():
#     return render_template('teacher/tea_score.html')
#
#
# @teacher.route('/score_data/')
# def score_data():
#     score_list = Score.query.all()
#     data = []
#     for i in score_list:  # type:Score
#         data.append(i.to_json())
#     return jsonify(data)
#
#
# @teacher.route('/score_del')
# def score_del():
#     uid = request.values.get('id')
#     s = Score.query.get(uid)
#     try:
#         db.session.delete(s)
#         db.session.commit()
#         return 'success'
#     except BaseException as e:
#         print('成绩删除出错%s' % e)
#         return 'error'


