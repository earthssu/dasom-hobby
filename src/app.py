from src import app, post_coll
from flask import request, url_for, redirect, render_template
import time


# 메인 페이지
@app.route('/')
def index():
    return 'hello world'


# 추천 콘텐츠
@app.route('/recommend')
def recommend():
    return 'recommend'


# 취미 게시물 목록 페이지
@app.route('/hobbylist')
def hobby_list():
    return 'hobby list'


# 취미 게시물 작성 페이지
@app.route('/write')
def write():
    return 'write'


# 취미 게시물 목록 페이지
@app.route('/post', methods=['GET'])
def save_post():
    name = request.form['name']
    email = request.form['email']
    category = request.form['category']
    content = request.form['content']
    img = request.form['img']

    date_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))

    post_coll.insert(
        {'name': name, 'email': email, 'category': category, 'content': content, 'img': img, 'time': date_time})

    return redirect(url_for('hobby_list'))


# 설문 페이지
@app.route('/survey')
def survey():
    return render_template('test1.html')


# 결과 계산
@app.route('/result-statistic', methods=['POST'])
def outcome_cal():
    result = request.form
    print(result)

    return 'OK'


# 결과 페이지 (총 8개)

# 호랑이 (ESTP / ENTP)
@app.route('/tiger')
def tiger():
    return render_template('resultTiger.html')


# 기린 (ESFP / ENFP)
@app.route('/giraffe')
def giraffe():
    return render_template('resultGiraffe.html')


# 판다 (ENFJ / ESFJ)
@app.route('/panda')
def panda():
    return render_template('resultPanda.html')


# 악어 (ESTJ / ENTJ)
@app.route('/crocodile')
def crocodile():
    return render_template('resultCrocodile.html')


# 양 (INFJ / INTJ)
@app.route('/sheep')
def sheep():
    return render_template('resultSheep.html')


# 펭귄 (INFP / INTP)
@app.route('/penguin')
def penguin():
    return render_template('resultPenguin.html')


# 고양이 (ISTP / ISFP)
@app.route('/cat')
def cat():
    return render_template('resultCat.html')


# 토끼 (ISFJ / ISTJ)
@app.route('/rabbit')
def rabbit():
    return render_template('resultRabbit.html')