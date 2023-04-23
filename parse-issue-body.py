import sys
print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))



test_input = '### source-id\n\nREMO2023\n\n### What license do you choose?\n\nCC BY 4.0' 


def parse_issue_body(issue):
    lines = issue.splitlines()
    lines = [line for line in lines if line]
    keys = lines[::2]; values = lines[1::2]
    return {k.split()[1]: v for k,v in zip(keys, values)}    



if __name__ == "__main__":
    issue_body = test_input #sys.argv[1]
    entries = parse_issue_body(issue_body)
    print(entries)
