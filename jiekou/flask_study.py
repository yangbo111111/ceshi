from flask import  Flask
from flask import  request
import json
app = Flask(__name__)
@app.route('/passport/user/login',methods=['GET'])
def home():
    user=request.args.get('user')
    psw=request.args.get('psw')
    data = json.dumps({
        'user': user,
        'psw': psw
    })
    return data
@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method=request.method
    if request_method == 'POST':
        user=request.form.get('user')
        psw=request.form.get('psw')
        data = json.dumps({
            'user': user,
            'psw': psw
        })
    else:
        data = json.dumps({
            'message': '请求不合法'
        })
    return data
if __name__ == '__main__':
    app.run()