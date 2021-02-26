codegen: clean process
	sh scripts/codegen.sh

process:
	cat vault-openapi.json | python scripts/process-spec.py | jq > vault-openapi-processed.json

clean:
	rm -rf vault
