install:
	@poetry install

lint:
	@poetry run flake8 page_loader

build:
	@poetry build

publish:
	@poetry publish -r pypi_test

pytest:
	poetry run pytest --cov=tests/ --log-cli-level=10 --cov-report xml
