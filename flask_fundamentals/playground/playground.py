from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.

@app.route('/play')                       # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def play():
    return render_template('index_f.html', num=3)

@app.route('/play/<num>')                          
                                        
def playground(num):
    return render_template('index_f.html', num=int(num))  


@app.route('/play/<num>/<usercolor>')                          
                                          
def playcolor(num, usercolor):
    return render_template('index_f.html', color = usercolor, num=int(num))


if __name__=="__main__":
    app.run(debug=True)