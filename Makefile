.PHONY: upgrade test lint clean

upgrade:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt

test:	clean
	pytest -vv --durations=0 --cov . --cov-config .coveragerc --cov-report=term-missing --capture=no

lint:
	flake8 . --config .flake8

clean:
	rm -rf __pycache__
	rm -f .coverage .coverage.* coverage.xml
	rm -rf .pytest_cache/
