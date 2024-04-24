import subprocess
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/swlab', methods=['POST'])
def swlab():
    subprocess.run(['python3', '/Users/LFR/Documents/python/flask/switch.py'])
    return 'Script has been executed successfully!'

if __name__ == '__main__':
    app.run(host='192.168.4.33',port=8888,debug=True)