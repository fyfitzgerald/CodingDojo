from flask import Flask, render_template, request, redirect, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-copy9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# import the function connectToMySQL from the file mysqlconnection.py
from users import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('cr_friends')
# now, we may invoke the query_db method

app.secret_key = 'KeepItSecretKeepItSafe'

print("all the friends", mysql.query_db("SELECT * FROM friends;"))


@app.route('/users')         
def index():
    mysql = connectToMySQL("cr_friends")
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched all friends", all_friends)
    return render_template('index.html', friends = all_friends)




@app.route('/users/new')
def new():
    mysql = connectToMySQL("cr_friends")
    return render_template('/new.html')




@app.route('/users/<id>/edit')
def edit(id):
    query = 'SELECT * FROM friends WHERE id = %(id)s'
    mysql = connectToMySQL("cr_friends")
    data = {
            'id': id
            }
    friend = mysql.query_db(query, data)
    return render_template('/edit.html', friend = friend[0])




@app.route('/users/<id>')
def show(id):
    query = 'SELECT * FROM friends WHERE id = %(id)s'
    mysql = connectToMySQL("cr_friends")
    data = {
            'id': id
            }
    friend = mysql.query_db(query, data)
    return render_template('show.html', friend = friend[0])




@app.route('/users/create', methods=['POST'])
def create():
    number_of_errors = 0
    if request.method == 'POST':
        if len(request.form['first_name']) < 2: 
            flash("Please enter a first name.")
            number_of_errors += 1
        
        if len(request.form['last_name']) < 2: 
            flash("Please enter a last name.")
            number_of_errors += 1

        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
            number_of_errors += 1

    if number_of_errors > 0:
        return redirect('/users/new')

    mysql = connectToMySQL("cr_friends")
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    print(data)
    new_friend_id = mysql.query_db(query, data)
    return redirect('/users')




@app.route('/users/<id>/destroy')
def destroy(id):
    query = 'DELETE FROM friends WHERE id = %(id)s'
    mysql = connectToMySQL("cr_friends")
    data = {
            'id': id
            }
    friend = mysql.query_db(query, data)
    return redirect('/users')




@app.route('/users/<id>/update', methods=['POST'])
def update(id):
    number_of_errors = 0
    if request.method == 'POST':
        if len(request.form['first_name']) < 2: 
            flash("Please enter a first name.")
            number_of_errors += 1
        
        if len(request.form['last_name']) < 2: 
            flash("Please enter a last name.")
            number_of_errors += 1

        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
            number_of_errors += 1

    if number_of_errors > 0:
        return redirect(f'/users/{id}/edit')

    query = 'UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s'
    mysql = connectToMySQL("cr_friends")
    data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'email': request.form['email'],
            'id': id
            }
    friend = mysql.query_db(query, data)
    return redirect(f'/users/{id}')



if __name__ == "__main__":
    app.run(debug=True)