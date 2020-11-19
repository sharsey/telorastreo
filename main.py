from flask import Flask, render_template

app = Flask(__name__)
#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=80)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
