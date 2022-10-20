from flask import Flask, request

from jobcan_auto_login import jobcan_automation

app = Flask(__name__)


@app.route('/jobcan_auto', methods=["POST"])
def index():
    method = request.form["method"]
    email = request.form["email"]
    password = request.form["password"]
    if email == "" or password == "":
        return "メールアドレス、パスワードが不正です。"
    is_success = jobcan_automation(method, email, password)
    return handle_message(method, is_success)


def handle_message(method, is_success):
    if method == 0:
        if is_success == 1:
            return "出勤しました"
        else:
            return "エラーが発生しました"

    if method == 1:
        if is_success == 1:
            return "退勤しました"
        else:
            return "エラーが発生しました"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=334,
            threaded=True,
            debug=True)
