from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hiya!'

if __name__ == '__main__':
  host = '127.0.0.1'
  port = 5000
  app.run(host=host, port=port)
