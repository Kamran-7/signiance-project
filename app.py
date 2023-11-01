from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        full_name = f"{first_name} {last_name}"
        return full_name
    return open('index.html').read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

