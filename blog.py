from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # выдуманный пользователь
    posts = [  # список выдуманных постов
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Poland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title='home',
                           user=user,
                           posts=posts)



app.run(debug=True)
