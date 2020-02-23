import datetime
from profile import profile
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home_page():
    year = datetime.datetime.now().year
    return render_template('./index.html', year=year, profile=profile)

@app.route('/<username>/<int:post_id>')
def user_page(username, post_id):
    return render_template('./index.html', 
        name=username, 
        post_id=post_id)

@app.route('/blog')
def blog_page():
    return 'Welcome to my blog!'


# @app.route('/static/favicon.ico')
# def favicon():
#     print(url_for('static', filename='favicon.ico'))

# if __name__ == '__main__':
    # app.debug = True
    # app.run(port=8080)   