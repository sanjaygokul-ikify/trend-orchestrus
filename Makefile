build:
	cargo build --release

fmt:
	poetry run black .
	poetry run isort .

docker: build
	docker-compose up -d

ci:
	make test
	python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. protos/*.proto

test:
	coverage run -m pytest tests/
	coverage report

clean:
	rm -rf __pycache__/.tox/ *.egg-info/