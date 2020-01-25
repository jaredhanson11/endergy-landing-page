docker-user=jaredhanson11
name=${docker-user}/endergy-landing-page

.PHONY: set-tag

set-tag:
	$(eval TAG=`git rev-parse --short HEAD`)
build:
	docker build . -t ${name}:latest
build-tagged: set-tag
	docker build . -t ${name}:${TAG}
push:
	docker push ${name}:latest
push-tagged: build-tagged
	docker push ${name}:${TAG}