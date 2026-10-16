import json
import os
import sys
from datetime import datetime


def set_output(ok: bool):
    path = os.environ.get('GITHUB_OUTPUT')
    if path:
        with open(path, 'a') as f:
            f.write(f"ok={'true' if ok else 'false'}\n")


try:
    from scholarly import scholarly

    author = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']: v for v in author['publications']}
except Exception as e:
    # Google Scholar often blocks CI IPs; keep the previous data instead of failing.
    print(f"Scholar fetch failed, keeping previous data: {e}", file=sys.stderr)
    set_output(False)
    sys.exit(0)

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump(author, f, ensure_ascii=False, default=str)

with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump({"schemaVersion": 1, "label": "citations", "message": f"{author['citedby']}"}, f)

print(f"citations: {author['citedby']}")
set_output(True)
