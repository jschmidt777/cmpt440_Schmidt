# file: main.py
# author: Joseph Schmidt
# course: CMPT 440
# assignment: semester project
# due date: 05MAY2017
# version: 1.0

# This file is the main driver for this application.
# It shows how an ACL is converted to a DFA using a graph/tree like data structure
# and then enforeced on an ip address stream.
# It does with the following process:
# -Take an arugment for the ACL wished to be enforced
# -Converts the ACL to DFA
# -Takes an arugment for the source ip address stream 
# -Outputs the ip addressess permitted or denied based on the ACL
# It will output this processes verbosely to show it's validity.
# It nullifies circular dependencies when loaded in packages
# and is ran in the terminal using python 3.5.0.

from readacl import lines, permits, denys
from dfafromacl import createdfa
from transition import transition
import sys

print(lines)
print("Any repeat statements were removed.")
print(permits)
print(len(permits))
print(denys)

permitdfa = createdfa(permits)
denydfa = createdfa(denys)


# This allows the dfas created above to be printed to the output terminal
# Params: the dfa created
# Returns: a printed representation of the dfa with a tree like fashion

def printdfa(dfa, lvl=0):
    if dfa.nodeId is not None:
        stringtoprint = ""
        # Identifies the indentation level/depth of the node in the dfa
        for i in range(lvl):
            stringtoprint += "-"
        print(stringtoprint + dfa.nodeId)
        if len(dfa.transitionOn) > 0:  # If there are childern to the node
            for i in range(len(dfa.transitionOn)):
                printdfa(dfa.transitionOn[i], lvl + 1)
    else:
        if len(dfa.transitionOn) == 0 and dfa.acceptedState == True:
            if dfa == "permitdfa":
                print("All addresses permitted") 
            elif dfa == "denydfa":
                print("All addresses denied")
        else:
            for i in range(len(dfa.transitionOn)):
                printdfa(dfa.transitionOn[i], 0)

inputstream = sys.argv[2]
with open('streams/'+inputstream+'.txt') as addresses:
	stream = addresses.readlines()
	stream = [x.strip('\n') for x in stream]


# This enforces the order of what statements are processed
# Params: N/A
# Returns: The result of enforcing the ACL on the inputted stream of ip addresses

def permitthendeny():
	print("DFA created for permit statements.")
	# show the nodes for this dfa
	printdfa(permitdfa)
	permitaddresses = transition(permitdfa,stream)
	print("Permitted addresses:", permitaddresses)
	print("DFA created for deny statements.")
	# show the nodes for this dfa
	printdfa(denydfa)
	denyaddresses = transition(denydfa,stream)
	#checkdenys = list(set(denyaddresses)^set(permitaddresses))
    # ensures no unecessary addresses in the deny list
	print("Denied addresses:", denyaddresses)

permitthendeny()

