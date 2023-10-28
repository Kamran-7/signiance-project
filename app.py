# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         first_name = request.form['firstname']
#         last_name = request.form['lastname']
#         print(f'First Name: {first_name}, Last Name: {last_name}')
#         return f'First Name: {first_name}, Last Name: {last_name}'
#     return '''
#         <form method="post">
#             <input type="text" name="firstname" placeholder="Enter First Name"><br>
#             <input type="text" name="lastname" placeholder="Enter Last Name"><br>
#             <input type="submit" value="Submit"><br>
#         </form>
#     '''

# if __name__ == '__main__':
#     app.run(debug=True)

# -------------------------------------------------------------------------------
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        return f"First Name: {first_name}<br>Last Name: {last_name}"
    return open('index.html').read()

if __name__ == '__main__':
    app.run(debug=True)
#---------------------------------------------------------------------------


# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         full_name = f"{first_name} {last_name}"
#         return f"Full Name: {full_name}"
#     return open('index.html').read()

# if __name__ == '__main__':
#     app.run(debug=True)
