#!/usr/bin/env sh

# config options: https://openapi-generator.tech/docs/generators/rust

docker run --rm --volume="${PWD}:/local" \
  openapitools/openapi-generator-cli:latest generate \
  --generator-name rust \
  --package-name vault \
  --additional-properties packageVersion=0.1.0 \
  --input-spec /local/vault-openapi-processed.json \
  --output /local/vault
