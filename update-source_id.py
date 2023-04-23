import sys
import json
print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))


table = "CORDEX_source_id.json"


def update_table(entry):
    with open(table, "r") as f:
        current = json.load(f)
    current["source_id"].update(entry)
    print(current)
    with open(table, 'w') as f:
       json.dump(current, f)

def get_entries(content):
    entries = json.loads(content) 


if __name__ == "__main__":
    content = sys.argv[1]
    entries = get_entries(content)
    update_table(entry)
