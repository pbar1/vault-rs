#!/usr/bin/env sh

docker run --rm \
  -v $PWD:/local openapitools/openapi-generator-cli generate \
  -i /local/vault_1.6.0_openapi.json \
  -g rust \
  -o /local/out/rust
