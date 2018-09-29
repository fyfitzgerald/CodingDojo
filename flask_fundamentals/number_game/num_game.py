import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = 'ThisIsSecret'


@app.route('/')         
def index():
    if 'number' not in session:
        session['number'] = random.randrange(0,101)
        session['output'] = ""
    print(session['number'])
    return render_template("num_game.html")

@app.route('/guess', methods=["Post"])         
def guess():
    print("in guess method")
    print(request.form)
    guess = int(request.form['guess'])
    if int(request.form['guess']) == session['number']:
        print("option 1")
        session['output'] = "Great Job!"
    elif int(request.form['guess']) < session['number']:
        print("option 2")
        session['output'] = "Too Low"
    elif int(request.form['guess']) > session['number']:
        print("option 3")
        session['output'] = "Too High"
    return redirect('/')


@app.route("/reset", methods =['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    