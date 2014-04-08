from flask import Flask, render_template, url_for
#from flask_db import Organ
app = Flask(__name__, static_url_path='')

class nav:
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption

@app.route('/show')
def show():
	return render_template('viewer.html')

@app.route('/')
def search():
  return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)