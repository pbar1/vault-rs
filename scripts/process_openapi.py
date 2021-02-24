import json
import re
import sys

data = json.load(sys.stdin)

for p in data['paths']:
    # create clean, title-cased name from the path
    opid_im = re.sub(r'{.+?}', '', p).replace('/', ' ').replace('-', ' ').replace('_', ' ')
    opid_cln = ''.join(x for x in opid_im.title() if not x.isspace())
    title_im = re.sub(r'[^a-zA-Z0-9]', ' ', p)
    title_cln = ''.join(x for x in title_im.title() if not x.isspace())

    # set operation ids to cleaner names
    for op in ['get', 'delete', 'post']:
        if op in data['paths'][p]:
            data['paths'][p][op]['operationId'] = op + title_cln

            # add titles to request body schemas so generated models have proper names
            if op == 'post' \
                    and 'requestBody' in data['paths'][p][op] \
                    and 'content' in data['paths'][p][op]['requestBody'] \
                    and 'application/json' in data['paths'][p][op]['requestBody']['content'] \
                    and 'schema' in data['paths'][p][op]['requestBody']['content']['application/json']:
                data['paths'][p][op]['requestBody']['content']['application/json']['schema']['title'] = op + opid_cln + 'Input'

print(json.dumps(data))
