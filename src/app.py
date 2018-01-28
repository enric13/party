from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html', msg='WELCOME')

@app.route('/info')
def info():
    return render_template('info.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
