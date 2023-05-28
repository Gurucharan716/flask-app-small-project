from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sqrt', methods=['POST'])
def sqrt():
    number = float(request.form['number'])
    result = number ** 0.5
    return render_template('index.html', number=number, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
