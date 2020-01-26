# Endery Landing Page

The landing page for Endergy.

## Intro
The directory `endergy-landing-page/public/` contains all static website files.
The `Dockerfile.public` file builds and image that uses nginx to serve all `public` files on port 80.
The directory `endergy-landing-page/backend/` contains all files for the server, which handles customer inquiries.
The `Dockerfile.backend` file builds and image that runs the Flask server.
The `Makefile` defines some recipes for building and pushing the docker images.

## Template
The website bootstrapped a [template](https://github.com/BlackrockDigital/startbootstrap-creative).
