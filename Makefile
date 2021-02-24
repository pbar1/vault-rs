codegen: process
	sh scripts/codegen.sh

patch:
	cat vault-openapi.json | json-patch -p patch.json | jq > vault-openapi-patched.json

process: patch
	cat vault-openapi-patched.json | python scripts/process_openapi.py | jq > vault-openapi-processed.json
