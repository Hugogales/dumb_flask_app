from flask import Flask, render_template, request, redirect, url_for, session
import time
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['age'] = int(request.form['age'])
        session['nationality'] = request.form['nationality']
        session['weight'] = float(request.form['weight'])
        session['star_sign'] = request.form['star_sign']
        session['poo_quality'] = int(request.form['poo_quality'])
        return redirect(url_for('processing'))
    return render_template('index.html')

@app.route('/processing')
def processing():
    time.sleep(5)  # Fake processing delay
    predicted_age = random.randint(session['age'], 110)
    return render_template('result.html', name=session['name'], predicted_age=predicted_age)

if __name__ == '__main__':
    app.run(debug=True)
