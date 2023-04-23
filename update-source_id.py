import sys
import json
print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))


if __name__ == "__main__":
    content = sys.argv[1]
    entries = json.loads(content) 
    print(entries)
