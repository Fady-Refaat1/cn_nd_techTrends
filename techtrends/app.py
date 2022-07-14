from cgitb import text
from datetime import datetime
import logging
import sqlite3  

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    posts = connection.execute('SELECT * FROM posts').fetchall()
    metricsObj['db_connection_count'] += 1
    metricsObj['post_count'] = len(posts)
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# health check function
def health_check():
    try:
        connection = get_db_connection()
        connection.close()
        return "OK - healthy"
    except:
        return "Not - healthy"

# get time and date 
def getTimeDate():
    now = datetime.now()
    return  now.strftime("%d/%m/%Y , %H:%M:%S")
# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Health check endpoint
@app.route("/healthz")
def healthz():
    status = health_check()
    response = app.response_class(
        response=json.dumps({"result": status}),
        status=200,
        mimetype='application/json'
    )
    return response

# metrics endpoint
@app.route("/metrics")
def metricsEndPoint():
    response = app.response_class(
        response=json.dumps(metricsObj),
        status=200,
        mimetype='application/json'
    )
    return response

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      app.logger.info(f'{getTimeDate()}, Article not existing!')
      return render_template('404.html'), 404
    else:
      title = post['title']
      app.logger.info(f'{getTimeDate()}, Article {title} retrieved!')
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.info(f'{getTimeDate()}, About Us page retrieved successfully !')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()
            app.logger.info(f'{getTimeDate()}, Article {title} created successfully !')

            return redirect(url_for('index'))

    return render_template('create.html')

# start the application on port 3111
if __name__ == "__main__":
   metricsObj = {"db_connection_count": 0,"post_count": 0}
   logging.basicConfig(level = logging.DEBUG, filename = 'application.log')
   app.run(host='0.0.0.0', port='3111')
