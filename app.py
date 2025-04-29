from flask import Flask, render_template
import os
import sys
import shutil

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

def build_static_site():
    """Build static HTML files for GitHub Pages"""
    # Create build directory
    build_dir = '_build/html'
    os.makedirs(build_dir, exist_ok=True)
    
    # Copy static files
    shutil.copytree(static_path, os.path.join(build_dir, 'static'), dirs_exist_ok=True)
    
    # Create HTML files
    with app.test_request_context():
        # Home page
        with open(os.path.join(build_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(home())
        
        # Other pages
        pages = ['about', 'approach', 'contact', 'partners', 'faq']
        for page in pages:
            os.makedirs(os.path.join(build_dir, page), exist_ok=True)
            with open(os.path.join(build_dir, page, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(globals()[page]())

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        build_static_site()
    else:
        app.run()
