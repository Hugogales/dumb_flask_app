from flask import Flask, render_template, request, redirect, url_for, session
import time
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

name = None
age = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.clear()  # Clear the session data
        session['name'] = request.form['name']
        name = request.form['name']
        session['age'] = int(request.form['age'])
        age = request.form['age']
        session['nationality'] = request.form['nationality']
        session['weight'] = float(request.form['weight'])
        session['star_sign'] = request.form['star_sign']
        session['poo_quality'] = int(request.form['poo_quality'])
        print(f"Session data set: {session}")  # Debugging line
        return redirect(url_for('processing'))
    return render_template('index.html')

@app.route('/processing', methods=['POST', 'GET'])
def processing():
    time.sleep(5)  # Fake processing delay
    session['predicted_age'] = random.randint(session['age'], 110)
    print(f"Processing session data: {session}")  # Debugging line
    return redirect(url_for('result'))

@app.route('/result')
def result():
    print(f"Result session data: {session}")  # Debugging line
    return render_template('result.html', name=session.get('name'), predicted_age=session.get('predicted_age'))

if __name__ == '__main__':
    app.run(debug=True)