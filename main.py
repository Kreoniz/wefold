from flask import Flask, render_template, url_for, redirect
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL', 'в текущий момент почта недоступна :(')


@app.route('/')
@app.route('/index')
def main_page():
    params = {}
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    params['css_dest'] = url_for('static', filename='css/style.css')
    return render_template('index.html', **params)

@app.route('/roadmap')
def roadmap():
    params = {}
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    params['css_dest'] = url_for('static', filename='css/roadmap.css')
    return render_template('roadmap.html', **params)

# * <--------------------------- All roadmap-associated files --------------------------->

@app.route('/roadmap/stage-0/a/whats_immersion')
def whats_immersion():
    params = {}
    params['css_dest'] = url_for('static', filename='css/article.css')
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    return render_template('stage-0/a/whats_immersion.html', **params)

@app.route('/roadmap/stage-0/a/activities_explained')
def activities_explained():
    params = {}
    params['css_dest'] = url_for('static', filename='css/article.css')
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    return render_template('stage-0/a/activities_explained.html', **params)

@app.route('/roadmap/stage-0/a/whats_my_level')
def whats_my_level():
    params = {}
    params['css_dest'] = url_for('static', filename='css/article.css')
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    return render_template('stage-0/a/whats_my_level.html', **params)

@app.route('/roadmap/stage-1/a/immersion')
def immersion():
    params = {}
    params['css_dest'] = url_for('static', filename='css/article.css')
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    return render_template('stage-1/a/immersion.html', **params)

@app.route('/roadmap/stage-1/a/language_basics')
def language_basics():
    params = {}
    params['css_dest'] = url_for('static', filename='css/article.css')
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    return render_template('stage-1/a/language_basics.html', **params)

@app.route('/roadmap/stage-1/a/vocabulary')
def vocabulary():
    params = {}
    params['css_dest'] = url_for('static', filename='css/article.css')
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    params['vocabulary_card_front'] = url_for('static', filename='img/vocabulary-card-front.png')
    params['vocabulary_card_back'] = url_for('static', filename='img/vocabulary-card-back.png')
    return render_template('stage-1/a/vocabulary.html', **params)

# * <--------------------------- All roadmap-associated files --------------------------->

@app.route('/about')
def about():
    params = {}
    params['crane_logo'] = url_for('static', filename='img/icons/symbol-contrast.svg')
    params['css_dest'] = url_for('static', filename='css/about.css')
    params['email'] = CONTACT_EMAIL
    return render_template('about.html', **params)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)