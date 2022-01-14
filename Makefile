
.PHONY: run 

install_deps:
	pip install funcparserlib

lexertest: 
	python3 ./test/lexertest.py

example1: 
	python3 cyprus.py -p ./examples/example1.cyp

example2: 
	python3 cyprus.py ./examples/example2.cyp

hello:
	python3 cyprus.py ./examples/hello.cyp
