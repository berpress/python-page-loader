install:
	@poetry install

lint:
	@poetry run flake8 page_loader


pytest:
	@poetry run pytest

build:
	@poetry build

publish:
	@poetry publish -r pypi_test

coverage:
	@poetry coverage run -m pytest
