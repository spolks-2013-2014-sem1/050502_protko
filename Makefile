all:
	virtualenv env
	./env/bin/python setup.py install
	/bin/sh ./env/bin/activate

clean:
	rm -rf env
	rm -rf build
	rm -rf dist
	rm -rf net.egg-info
