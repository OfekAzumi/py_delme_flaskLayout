from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"}
]

@app.route("/", methods = ["get","post"])
def login():
    uname = request.form.get('username')
    pswd = request.form.get('password')
    slc_user = ''
    for usr in users:
        if uname == usr["username"]:
            if pswd == usr["password"]: slc_user = usr
    print(slc_user)
    if(slc_user):
        return render_template('main.html', username = uname)
    else:
        if (uname != None and pswd != None):
            return render_template('login.html', msg = 'password or username is incorrect.')
        else: 
            return render_template('login.html', msg = '')

@app.route("/home")
def home():
    return render_template('main.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/products")
def products():
    return render_template('product.html')

if __name__=='__main__':
    app.run(debug=True)