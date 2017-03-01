# read in an acl called 'acl(a number).txt' and go line by line
# this will check to see if the input is valid as well
# where next thing after a permit or deny is not x.x.x.x or any, errror
# if no deny any or permit any, add deny any to the end of the file
with open('acl/acl0.txt') as acl:
    lines = acl.readlines()
lines = [x.strip('\n') for x in lines]
