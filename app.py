import datetime
#from profile import profile
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


profile = {
    'firstName': 'Davis',
    'lastname': 'Bickford',
    'name': 'Davis Bickford',
    'jobTitle': 'Software Engineer',
    'aboutme': 'I am a software engineer passionate about solving complex challenges through technical experience, effective communication, collaboration, and a growth mindset.',
    'linkedin': 'in/davisbickford/',
    'linkedinURL': 'https://www.linkedin.com/in/davisbickford/',
    'resumeURL': 'https://drive.google.com/open?id=1rIftYRApheSlJFM68FOvzGL_yvoqHN6B',
    'email': 'davis.bickford@gmail.com',
    'phone': '(303) 947-4291',
    'projects': [
        {
            'title': 'PlayBound',
            'image': 'playbound.png',
            'description': "PlayBound is a video game currently in development. I am the sole developer and artist.",
            'description2': "PlayBound tells the story of Kelvin, a boy whose parents have become fatally boring. Strap on your velcro light-up kicks and equip your POG slammers, because it's time to save the world from certain lameness!",
            'techList': 'game development, c#, digital art, unity engine'.split(', '),
            'website': 'http://steam.studiosploot.com/',
            'codeURL': ''
        },
        {
            'title': 'Pug or Not Pug',
            'image': 'pug-or-not-pug.png',
            'description': "Pug or Not Pug is a web application that will determine whether a pug is in a provided image.",
            'description2': "",
            'techList': 'react, machine learning, rest api, node.js, express.js, postgreSQL, sql, html, css, javascript'.split(', '),
            'website': 'https://darnvisages.github.io/pug-or-not-pug/',
            'codeURL': 'https://github.com/darnvisages/pug-or-not-pug'
        },
        {
            'title': 'Parma',
            'image': 'parma.png',
            'description': "Parma is my favorite Italian restaurant, located in Superior, CO. I built their website using React.",
            'description2': "The site features a searchable menu.",
            'techList': 'react, html, css, javascript'.split(', '),
            'website': 'http://www.parmamozzarellabar.com/',
            'codeURL': ''
         },
        {
            'title': 'Portfolio Website',
            'image': 'portfoliosite.png',
            'description': "You're looking at it right now! This portfolio site was built using Flask and Bootstrap.",
            'description2': "",
            'techList': 'python, flask, bootstrap, html, css, javascript'.split(', '),
            'website': 'http://www.davisbickford.com/',
            'codeURL': 'https://github.com/darnvisages/davisbickford-flask-portfolio'
         }
        # {
        #     'title': '',
        #     'image': '',
        #     'description': "",
        #     'description2': "",
        #     'techList': ''.split(', '),
        #     'website': '',
        #     'codeURL': ''
        # ,
    ]
}

profile['project_count'] = len(profile['projects'])
