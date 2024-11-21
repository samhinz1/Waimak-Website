from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Disable this in production

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


if __name__ == '__main__':
    # In production, you can omit the debug flag
    app.run()
