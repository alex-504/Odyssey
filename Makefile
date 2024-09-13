start:
	heroku local web
test:
	pytest tests
build:
	docker build -t odyssey-app .
deploy:
	git push heroku main
start-local:
	gunicorn run:app
start-flask-local:
	FLASK_APP=run.py FLASK_ENV=development flask run