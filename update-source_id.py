import sys
import json
import pprint
print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))


table = "CORDEX_source_id.json"
table_name = "source_id"

def update_table(entry):
    with open(table, "r") as f:
        current = json.load(f)
    source_id = entry["source_id"]
    if source_id not in current[table_name]:
        current[table_name][source_id] = entry
    pprint.pprint(current)
    with open(table, 'w') as f:
       json.dump(current, f)

def get_entries(content):
    return json.loads(content) 


if __name__ == "__main__":
    content = sys.argv[1]
    entry = get_entries(content)
    print(entry)
    update_table(entry)
