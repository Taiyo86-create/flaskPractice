from flask import Flask

# Flaskを立ち上げるためのインスタンス
app = Flask(__name__)

# /でアクセスした際に<h1>Hello World</h1>を返す
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

# / or /somethingでアクセスした際に<h2>my hello</h2>を返す
@app.route('/hello')
@app.route('/something')
def hello():
    return '<h2>my hello</h2>'

# /post/post_id/post_nameでアクセスする
# post_idは数値型、post_nameは文字列型
@app.route('/post/<int:post_id>/<post_name>')
def show_post(post_id, post_name):
    # print(type(post_id))
    return '{}: {}'.format(post_name, post_id)

# /user/user_name/user_no
# user_noは数値型、user_nameは文字列型
@app.route('/user/<string:user_name>/<int:user_no>')
def show_user(user_name, user_no):
    user_name_no = user_name + str(user_no)
    return '<h1>{}</h1>'.format(user_name_no)

# このファイルを直で実行した際にFlaskアプリケーションを立ち上げる
if __name__ == '__main__':
    app.run()
