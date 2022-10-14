env = . .venv/bin/activate;
python = $(env) python
requirements_path = ./.devops/requirements

run:
	$(env) flask run

init_db:
	$(env) flask db init

migrate:
	$(env) flask db stamp head 
	$(env) flask db migrate

upgrade:
	$(env) flask db upgrade

setup_server_db: 
	flask db stamp head
	flask db migrate
	flask db upgrade

setup_db: init_db migrate upgrade

setup_env:
	rm ./.env || echo "Nenhum arquivo .env encontrado"
	cat ./.devops/.env.example >> ./.env

setup_dev: setup_env
	# setting python depencies
	python3.8 -m pip install virtualenv
	python3.8 -m virtualenv .venv
	$(python) -m pip install -r ./.devops/requirements/dev-requirements.txt

setup: setup_dev setup_db

clean_db:
	rm dev-storage.db || echo "arquivo dev .db nao encontrado"
	rm storage.db || echo "arquivo .db nao encontrado"
	rm -rf migrations || echo "migrations nao encontrada"

clean: clean_db
	rm -rf .pytest_cache
	rm -rf __pycache__
	rm -rf .venv
