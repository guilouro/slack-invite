sass:
	sass --watch static/sass/style.sass:static/css/style.css --style compressed

test:
	python test_app.py

clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete