import sys
import json
import pprint

table = "CORDEX_source_id.json"
table_name = "source_id"

def update_table(entry):
    with open(table, "r") as f:
        current = json.load(f)
    source_id = entry["source_id"]
    if source_id not in current[table_name]:
        current[table_name][source_id] = entry
    with open(table, 'w') as f:
       json.dump(current, f, indent=4)
    print(source_id)

def get_entries(content):
    return json.loads(content) 


if __name__ == "__main__":
    content = sys.argv[1]
    entry = get_entries(content)
    update_table(entry)
