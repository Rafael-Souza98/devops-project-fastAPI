APP = restapi

test:
	@pytest -v --disable-warnings

compose:
	@docker compose build --no-cache
	@docker compose up

att-req:
	@pip3 freeze > requirements.txt
	@pip3 install -r requirements.txt

setup-dev:
	@kind create cluster --config k8s/config/config.yaml
	@kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	@kubectl wait --namespace ingress-nginx \
	--for=condition=ready pod \
	--selector=app.kubernetes.io/component=controller \
	--timeout=270s

	@helm upgrade \
	--install \
	--set image.tag=5.0.8 \
	--set auth.rootPassword="root" \
	mongodb k8s/charts/mongodb

	@kubectl wait \
	--for=condition=ready pod \
	--selector=app.kubernetes.io/component=mongodb \
	--timeout=270s


destroy-dev:
	@kind delete clusters kind

helm-setup:
