from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/cal/<int:num1>/<string:op>/<int:num2>')
def calculator(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    #slash is not supported in route
    elif op == 'div':
        result = num1 / num2
    elif op == '%':
        result = num1 % num2
    else:
        return 'Invalid operator'

    return f'The result is {result}'


if __name__ == '__main__':
    app.run(debug=True)