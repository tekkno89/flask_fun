from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to the Index'

@app.route('/hey/<name>')
def say_hey(name):
  return 'Hey {!s}'.format(name)

@app.route('/number/<int:num>')
def find_num(num):
  if num == 42:
    return 'You got my number!'
  else:
    return 'nope, keep guessing'

@app.route('/hiya')
def hello_world():
  return 'Hiya!'

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 5000
  app.run(host=host, port=port)
