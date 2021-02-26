import yaml
import json
import sys
import re
from urllib.parse import quote
from copy import deepcopy

def eprint(*args, **kwargs):
    # prints to stderr
    print(*args, file=sys.stderr, **kwargs)


def pascal(s: str) -> str:
    # converts string to PascalCase
    return ''.join(x for x in s.title() if not x.isspace())


def uniqopid(s: str) -> str:
    # converts string like:
    #   /auth/token/lookup-self -> AuthTokenLookupSelf
    #   /auth/token/roles/{role_name} -> AuthTokenRoles
    # NOTE: there will be duplicates under this scheme. use nameoverride for those paths
    return pascal(re.sub(r'{.+?}', '', s).replace('/', ' ').replace('-', ' ').replace('_', ' '))


def jpesc(s: str) -> str:
    # escapes a string for use in a json pointer
    return s.replace('~', '~0').replace('/', '~1')


def pctencode(s: str) -> str:
    return quote(s).replace('%23', '#', 1)


def respcontent(data: dict):
    return {
        "application/json": {
            "schema": {
                "type": "object",
                "title": "VaultResponse",
                "properties": {
                    "request_id": {
                        "type": "string"
                    },
                    "lease_id": {
                        "type": "string"
                    },
                    "renewable": {
                        "type": "boolean"
                    },
                    "lease_duration": {
                        "type": "integer"
                    },
                    "data": data,
                    "wrap_info": {
                        "type": "object"
                    },
                    "warnings": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "auth": {
                        "type": "object"
                    },
                }
            }
        }
    }


# read patch configuration
with open('patchcfg.yaml') as f:
    patchcfg = yaml.full_load(f)

# load openapi spec from stdin
spec = json.load(sys.stdin)

# remove any paths from the spec marked for removal
for p in spec['paths'].copy():
    for prefix in patchcfg['remove']:
        if p.startswith(prefix):
            # eprint(f'{p} => removing')
            del spec['paths'][p]

# enrich spec with overrides
for p in spec['paths']:

    # build operation id and request body schema title
    overridden = False
    if p in patchcfg['nameoverride'].keys():
        overridden = True
        opid = patchcfg['nameoverride'][p]
    else:
        opid = uniqopid(p)
    # title = opid+'Input'
    eprint(f'{p},{opid},{overridden}')

    # set operation ids to cleaner names
    for op in ['get', 'delete', 'post']:
        if op in spec['paths'][p]:
            spec['paths'][p][op]['operationId'] = op+opid

            # add titles to request body schemas so generated models have proper names
            if op == 'post' \
                    and 'requestBody' in spec['paths'][p][op] \
                    and 'content' in spec['paths'][p][op]['requestBody'] \
                    and 'application/json' in spec['paths'][p][op]['requestBody']['content'] \
                    and 'schema' in spec['paths'][p][op]['requestBody']['content']['application/json']:
                spec['paths'][p][op]['requestBody']['content']['application/json']['schema']['title'] = f'{opid}Input'
                if 'get' in spec['paths'][p]:
                    spec['paths'][p]['get']['responses']['200']['content'] = \
                        deepcopy(spec['paths'][p]['post']['requestBody']['content'])
                    spec['paths'][p]['get']['responses']['200']['content']['application/json']['schema']['title'] = opid

# pretty-print processed spec to sdout
print(json.dumps(spec, indent=2))
