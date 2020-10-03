from src import app, post_coll
from flask import request, url_for, redirect, render_template
import time


# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')


# 추천 콘텐츠
@app.route('/recommend')
def recommend():
    return render_template('generic2.html')

@app.route('/type')
def type():
    return render_template('generic1.html')

# 취미 게시물 목록 페이지
@app.route('/elements')
def elements():
    post_list = post_coll.find({})
    return render_template('elements.html', post=post_list)


# 취미 게시물 작성 페이지
@app.route('/write')
def write():
    return render_template('elements1.html')


# 취미 게시물 업로드 페이지
@app.route('/post', methods=['POST'])
def save_post():
    name = request.form['name']
    email = request.form['email']
    category = request.form['category']
    content = request.form['content']

    date_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))

    post_coll.insert(
        {'name': name, 'email': email, 'category': category, 'content': content, 'time': date_time})

    return redirect(url_for('elements'))


# 취미 게시물 자세히 보기
@app.route('/content', methods=['POST'])
def content():
    email = request.form['email']
    user_post = post_coll.find_one({'email': email})
    return render_template('elements2.html', post=user_post)

# 설문 페이지
@app.route('/survey')
def survey():
    return render_template('test1.html')

'''
I 내향 / E 내향
N 직관 / S 감각.현실주의
T 사고형 / F 감정형
J 계획 / P 탐색

1. 적응을 잘하는 것보다 체계적인 것이 중요합니다. 4
2. 본인이 창의적이기보다 현실적인 사람이라고 생각합니다. 2
3. 친구가 어떤 일로 슬퍼할 경우, 문제를 처리하는 방법을 제시하기보다 정신적인 지지를 제공하곤 합니다. 3
4. 보통 여행 계획은 철저하게 세우는 편입니다. 4
5. 항상 책, 예술 또는 영화 등 색다르고 다양한 해석이 가능한 것에 관심이 있습니다. 2
6. 금방 새로운 직장 사람들과 어울리기 시작합니다. 1
7. 재미있는 책이나 비디오 게임이 종종 사교 모임보다 더 낫습니다. 1
8. 주의깊게 미리 계획하기 보다는 즉흥적으로 움직입니다. 4
9. 다소 내성적이고 조용한 성격입니다. 1
10. 중요한 결정을 내려야 할 때 일반적으로 가슴보다 논리가 더 중요합니다. 3
11. 감정의 기복이 심할 때가 있습니다. 3
12. 많은 사람들과 시간을 보낸 후에 에너지가 넘친다고 느낍니다. 1
13. 공상과 아이디어 때문에 흥분하는 일은 없습니다. 2
14. 대체로 상상보다는 경험에 더 의존하는 편입니다. 2
15. 종종 사회적 상황에서 주도적으로 행동합니다. 1
'''
# 결과 계산
@app.route('/result-statistic', methods=['POST'])
def outcome_cal():
    mbti_dic = {"I": 0, "E": 0, "N": 0, "S": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    q_dic = {"q1": "J", "q2": "S", "q3": "F", "q4": "J", "q5": "N", "q6": "E", "q7": "I", "q8": "P",
             "q9": "I", "q10": "T", "q11": "F", "q12": "E", "q13": "S", "q14": "S", "q15": "E"}
    count = {"never": 0, "hardly": 10, "sometimes": 20, "usually": 30, "always": 40}
    mbti = ''

    result = request.form
    print(result)

    for i in range(1, 16):
        question = 'q'+str(i)
        mbti_dic[q_dic[question]] += count[result[question]]

    print(mbti_dic)

    if mbti_dic['I'] > mbti_dic['E']:
        mbti += 'I'
    else:
        mbti += 'E'
    if mbti_dic['N'] > mbti_dic['S']:
        mbti += 'N'
    else:
        mbti += 'S'
    if mbti_dic['T'] > mbti_dic['F']:
        mbti += 'T'
    else:
        mbti += 'F'
    if mbti_dic['J'] > mbti_dic['P']:
        mbti += 'J'
    else:
        mbti += 'P'

    print(mbti)

    if mbti == 'ESTP' or mbti == 'ENTP':
        return redirect(url_for('tiger'))
    elif mbti == 'ESFP' or mbti == 'ENFP':
        return redirect(url_for('giraffe'))
    elif mbti == 'ENFJ' or mbti == 'ESFJ':
        return redirect(url_for('panda'))
    elif mbti == 'ESTJ' or mbti == 'ENTJ':
        return redirect(url_for('crocodile'))
    elif mbti == 'INFJ' or mbti == 'INTJ':
        return redirect(url_for('sheep'))
    elif mbti == 'INFP' or mbti == 'INTP':
        return redirect(url_for('penguin'))
    elif mbti == 'ISTP' or mbti == 'ISFP':
        return redirect(url_for('cat'))
    elif mbti == 'ISFJ' or mbti == 'ISTJ':
        return redirect(url_for('rabbit'))


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