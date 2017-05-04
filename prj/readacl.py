# Only take a file from the acl folder as an argument when executing
# if not exist: error, if not .txt: error
# file: readacl.py
# author: Joseph Schmidt
# course: CMPT 440
# assignment: semester project
# due date: 05MAY2017
# version: 1.0

# This file reads-in and processes the ACL inputted.
# It does with the following process:
# -Ensures it is a valid ACL (in accordance with rules.txt)
# -Ensures no repeated statments
# -Returns two lists, one for the pemitted addresses, and one for denied
# -Outputs the ip addressess permitted or denied based on the ACL
# It will output this processes verbosely to show it's validity.


import sys
import re
# TODO: Accept arguments

# s for sigma or the alphabet allowed
# (permit me this one line being too long please)
s = r"(?i)^((permit|deny)( *)((any)|(\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b))$)"

permit = r"(?i)(permit)"
deny = r"(?i)(deny)"

with open('acl/aclpermitany.txt') as acl:
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
# The ensuring of no repeat statements
else:  # create two arrays for the creation of dfas
    permits = [x for x in lines if re.match(permit, x)]
    permits = list(set(permits))  # ensures no repeat statements
    denys = [x for x in lines if re.match(deny, x)]
    denys = list(set(denys))  # ensures no repeat statements

# Removes  the word 'permit' so statments can be processed into a dfa
for i in range(len(permits)):
    permits[i] = permits[i].split(' ', 1)[1]
# Removes  the word 'permit' so statments can be processed into a dfa
for i in range(len(denys)):
    denys[i] = denys[i].split(' ', 1)[1]
