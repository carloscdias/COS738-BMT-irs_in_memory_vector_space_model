run: run_pc run_gli run_index run_busca

run_pc:
	python3 src/pc.py

run_gli:
	python3 src/gli.py

run_index:
	python3 src/index.py

run_busca:
	python3 src/busca.py

run_avalia:
	python3 src/avalia.py

requirements:
	pip3 install -r requirements.txt
