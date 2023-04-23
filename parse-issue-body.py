import sys
print ("Number of arguments:", len(sys.argv), "arguments")
print ("Argument List:", str(sys.argv))





def parse_issue_body(issue):
    lines = issue.splitlines()
    print(lines)



if __name__ == "__main__":
    issue_body = sys.argv[1]
    parse_issue_body(issue_body)
