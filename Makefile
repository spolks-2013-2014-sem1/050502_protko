SHELL:=/bin/bash

install:
	virtualenv env
	./env/bin/pip install pyrg
	./env/bin/python setup.py install
	/bin/sh ./env/bin/activate

clean:
	rm -rf env
	rm -rf build
	rm -rf dist
	rm -rf net.egg-info

test: clean install
	./env/bin/python tests/protocol_test.py |& ./env/bin/pyrg