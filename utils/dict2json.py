import json

def dict2json(info:dict):
    with open("repo_sync.json", "w") as f:
        f.write(json.dumps(info, ensure_ascii=False, indent=4, separators=(',', ':')))
