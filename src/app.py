from flask import Flask

app = Flask(__name__)


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
def post():
    return 'post'


# 설문 페이지
@app.route('/survey')
def survey():
    return 'survey'


# 결과 페이지
@app.route('/result')
def result():
    return 'result'