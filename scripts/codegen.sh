#!/usr/bin/env sh

docker run --rm --volume="${PWD}:/local" \
  openapitools/openapi-generator-cli generate \
  -g rust \
  -i /local/vault-openapi-processed.json \
  -o /local/generated
