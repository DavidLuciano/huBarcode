default: check

build:
	python setup.py build

upload: build
	python setup.py sdist

publish: upload
	# remove development tag
	python setup.py build sdist upload

install: build
	sudo python setup.py install

check:
	# PEP8 scheitert and den QR-code Tabellen.
	pyflakes hubarcode/datamatrix/ examples/
	pep8 -r --ignore=E501 hubarcode/datamatrix/ examples/
	-pylint --max-line-length=110 -d E1101 hubarcode/datamatrix/ examples/

testenv:
	virtualenv testenv
	testenv/bin/pip install coverage

test:
	PYTHONPATH=.:./hubarcode python test/test_coverage.py

.PHONY: test testenv
