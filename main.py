from flask import Flask,render_template

app = Flask(__name__)

#main index file
@app.route('/')
def index():
    return render_template('index.html', title="")

#admin login
@app.route('/admin/')
def adminIndex():
    return render_template('admin/index.html', title="Admin Login")

#-------------user area------------

#main index file
@app.route('/user/')
def userIndex():
    return render_template('user/index.html', title="user login")



if __name__ == '__main__':
    app.run(debug=True)