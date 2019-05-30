lint:
	find . -iname "*.py" | grep -v migrations | xargs pipenv run pylint --load-plugins pylint_django --disable=C0111,W0401,W0611,W0614,R0901,R0201

test:
	PIPENV_DOTENV_LOCATION=test.env pipenv run test
