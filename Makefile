run: run_pc run_gli run_index

run_pc:
	python3 src/pc.py

run_gli:
	python3 src/gli.py

run_index:
	python3 src/index.py

requirements:
	pip3 install -r requirements.txt
