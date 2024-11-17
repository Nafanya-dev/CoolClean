MANAGE := poetry run python manage.py

.PHONY: install
install:
	@poetry install

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	@$(MANAGE) makemigrations

.PHONY: start
start:
	@$(MANAGE) runserver

.PHONY: lint
lint:
	@poetry run flake8 CoolClean
