from flask import Flask, render_template, url_for
from flask import request
app = Flask(__name__, static_url_path='')

class nav:
		def __init__(self, href, caption):
				self.href = href
				self.caption = caption

@app.route('/show')
def show():
	organ = request.args.get('organ')
	
	if(organ == 'eyes'):
		name = "eyes"
		model = "eyes.stl"
	elif(organ == 'foot'):
		name = "foot"
		model = "footm.stl"
	elif(organ == 'skin'):
		name = "skin"
		model = "skins.stl"
	else:
		name = "octocat"
		model = "Octocat-v1.stl"
	return render_template('viewer.html', model=model, name=name)

@app.route('/')
def search():
	return render_template('search.html')

@app.route('/buy')
def buy():
	return render_template('buy.html')

if __name__ == '__main__':
		app.run(debug=True)