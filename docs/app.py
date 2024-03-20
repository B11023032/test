from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = request.form.get('textbox', '')  # 使用 get 方法获取字段值，如果字段不存在，则返回空字符串
        print(text)
        return 'Received: ' + text

if __name__ == '__main__':
    app.run(debug=True)
