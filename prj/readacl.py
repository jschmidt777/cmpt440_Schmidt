# read in an acl called 'acl(a number).txt' and go line by line
# this will check to see if the input is valid as well
# where next thing after a permit or deny is not x.x.x.x or any, errror
# if no deny any or permit any, add deny any to the end of the file
# is there a way to make this more secure?
# Only take a file from the acl folder as an argument when executing
import sys

with open('acl/acl0.txt') as acl:
    lines = acl.readlines()
lines = [x.strip('\n') for x in lines]
lines = list(filter(None, lines))  # gets rid of empty strings

if len(lines) == 0:
    sys.exit("Error: The ACL provided was empty! " +
             "Please provide a usable ACL (See rules.txt for ACL rules).")

permits = [x for x in lines if 'permit' in x]
denys = [x for x in lines if 'deny' in x]
# depending on the first line, if it's permit,
# check for deny at end and add if needed
