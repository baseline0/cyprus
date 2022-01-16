.PHONY: run clean

install_deps:
	pip install funcparserlib

lexertest: 
	python3 ./test/lexertest.py

example1: 
	python3 -v cyprus.py -V ./examples/example1.cyp  >out.txt 2>&1


example2: 
	python3 cyprus.py -V ./examples/example2.cyp

hello:
	python3 -v cyprus.py -V ./examples/hello.cyp >out.txt 2>&1

clean: 
	echo "clean up cyprus.log"