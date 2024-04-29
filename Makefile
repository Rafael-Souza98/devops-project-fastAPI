APP = restapi

test:
	@pytest -v --disable-warnings

compose:
	@docker compose build --no-cache
	@docker compose up

att-req:
	@pip3 freeze > requirements.txt
	@pip3 install -r requirements.txt