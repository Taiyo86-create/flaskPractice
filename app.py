from flask import Flask, render_template

app = Flask(__name__, template_folder='templates2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<string;user_name>')
def home(user_name):
    login_user = user_name
    return render_template('home.html', login_user=login_user)


if __name__ == '__main__':
    app.run(debug=True)