from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index_ds.html")

@app.route('/result', methods=['POST'])

def create_user():
    print("Got Post Info")
    return render_template("index_ds2.html", data = request.form)

@app.route('/')

def get_redirect_target():
    for target in request.form.get('submit'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target

@app.route('/danger')

def danger():
    print("A User Tried To Visit /danger. We have redirected the user to /.")
    return redirect ('/')



if __name__=="__main__":
    app.run(debug=True)