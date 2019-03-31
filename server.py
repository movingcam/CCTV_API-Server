from flask import Flask, request
from modules import MovingCAM, WebStreaming

app = Flask(__name__)
car = MovingCAM()

@app.route('/')
def index():
    print(request.args.get('user'))
    print(request.args.get('age'))
    return "Hello Flask"

@app.route('/forward', methods=['POST'])
def forward():
    result = car.forward()
    return result

@app.route('/backward', methods=['POST'])
def backward():
    result = car.backward()
    return result

@app.route('/go_right', methods=['POST'])
def go_right():
    result = car.right()
    return result

@app.route('/go_left', methods=['POST'])
def go_left():
    result = car.left()
    return result

@app.route('/streaming', methods=['POST'])
def streaming():
    pass

'''
@app.route('/turn_on', methods=['POST'])
def turn_on():
    pass

@app.route('/turn_off', methods=['POST'])
def turn_off():
    pass
'''

if __name__ == "__main__":
    app.run()