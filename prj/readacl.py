# read in an acl called 'acl(a number).txt' and go line by line
# this will check to see if the input is valid as well
# where next thing after a permit or deny is not x.x.x.x or any, error
# if no deny any or permit any, add deny any to the end of the file
# is there a way to make this more secure?
# Only take a file from the acl folder as an argument when executing
# if not exist: error, if not .txt: error
import sys
import re
# TODO: Accept arguments

# s for sigma or the alphabet allowed
# (permit me this one line being too long please)
s = r"(?i)^((permit|deny)( *)((any)|(\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b))$)"

permit = r"(?i)(permit)"
deny = r"(?i)(deny)"

with open('acl/acl0.txt') as acl:
    lines = acl.readlines()
lines = [x.strip('\n') for x in lines]
lines = list(filter(None, lines))  # gets rid of empty strings

if len(lines) == 0:
    sys.exit("Error: The ACL provided was empty! " +
             "Please provide a usable ACL (See rules.txt for ACL rules).")


def invalidinput():
    for i in range(len(lines)):
        if not re.match(s, lines[i]):
            return i
    else:
        return None


if invalidinput() is not None:
    sys.exit("Error on line " + str(invalidinput()) +
             " of the ACL. Invalid input!")
else:  # create two arrays for the creation of dfas
    permits = [x for x in lines if re.match(permit, x)]
    denys = [x for x in lines if re.match(deny, x)]
# depending on the first line, if it's permit,
# check for deny at end and add if needed
