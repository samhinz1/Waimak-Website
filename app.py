from flask import Flask, render_template
import os

# Get the absolute path to the static folder
static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public_html', 'static')

app = Flask(__name__, 
           static_folder=static_path,  # Use absolute path
           static_url_path='/static')  # Keep the URL path as /static
app.config['TEMPLATES_AUTO_RELOAD'] = False  # Disable auto-reload in production

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/approach')
def approach():
    return render_template('approach.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/partners')
def partners():
    return render_template('partners.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')



if __name__ == '__main__':
    app.run()
