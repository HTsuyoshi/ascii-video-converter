.PHONY: 'build clean'

build:
	@echo 'Building image...'
	@docker build -f Dockerfile.create --tag ascii-create-video:1.0 .
	@docker build -f Dockerfile.run --tag ascii-run-video:1.0 .

clean:
	@echo 'Deleting image...'
	@docker image rm ascii--create-video:1.0
	@docker image rm ascii--run-video:1.0
