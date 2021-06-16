test:
	python3 cube_test.py

format:
	black ./*.py --line-length 80
	black ./cuber --line-length 80