from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = 'ThisIsSecret'

@app.route('/')         
def index():
    print(session)
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("counter.html")

@app.route('/destroy_session')         
def clear_session():
    print(request.form)
    session.clear()
    return redirect('/')

@app.route('/addtwo')         
def addtwo():
    session['count'] += 1
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    