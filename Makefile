docker-user=jaredhanson11
name=${docker-user}/endergy-landing-page

.PHONY: set-tag

set-tag:
	$(eval TAG=`git rev-parse --short HEAD`)

build-client:
	docker build . -f Dockerfile.public -t ${name}-client:latest
build-server:
	docker build . -f Dockerfile.backend -t ${name}-server:latest
build-tagged: set-tag
	docker build . -f Dockerfile.public -t ${name}-client:${TAG}
	docker build . -f Dockerfile.backend -t ${name}-server:${TAG}
build-images: build-server build-client

push-client: build-client
	docker push ${name}-client:latest
push-server: build-server
	docker push ${name}-server:latest
push-tagged: build-tagged
	docker push ${name}-client:${TAG}
	docker push ${name}-server:${TAG}
push-images: push-client push-server
