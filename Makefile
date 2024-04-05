APP = restapi

compose:
	@docker-compose build
	@docker-compose up

att-req:
	@pip3 freeze > requirements.txt

test:
	@pytest -v --disable-warnings
