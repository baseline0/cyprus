
.PHONY: run 

install_deps:
	pip install funcparserlib

lexertest: 
	python3 ./test/lexertest.py

test1: 
	python3 cyprus.py ./test/test1.cyp

test2: 
	python3 cyprus.py ./test/test2.cyp

hello:
	python3 cyprus.py ./test/hello.cyp
