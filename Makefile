APP = restapi

flake:
	@flake8 . --exclude .venv

compose:
	@docker-compose build
	@docker-compose up

att-pip:
	@pip3 freeze > requirements.txt

test:
	@pytest -v --disable-warnings
