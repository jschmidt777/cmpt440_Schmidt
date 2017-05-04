# Nullifies circular dependencies when loaded in packages.
# from node import Node
# newNode = Node()
# print(newNode)
# newNode1 = Node(acceptedState=True, nodeId=5)
# print(newNode1)
from readacl import lines, permits, denys
from dfafromacl import createdfa
from transition import transition

print(lines)
print("Any repeat statements were removed.")
print(permits)
print(len(permits))
print(denys)

permitdfa = createdfa(permits)
denydfa = createdfa(denys)


def printdfa(dfa, lvl=0):
    if dfa.nodeId is not None:
        stringtoprint = ""
        # Identifies the indentation level/depth of the node in the dfa
        for i in range(lvl):
            stringtoprint += "-"
        print(stringtoprint + dfa.nodeId)
        if len(dfa.transitionOn) > 0:  # If there are childern to the node
            # print("Found children ", dfa )
            # print("Children ", dfa.transitionOn)
            for i in range(len(dfa.transitionOn)):
                # print("Looking at node: ", dfa.transitionOn[i])
                printdfa(dfa.transitionOn[i], lvl + 1)
    else:
        if len(dfa.transitionOn) == 0 and dfa.acceptedState == True:
            print("All addresses permitted/denied")  #Depends on what is printed (know that permit is first, then deny)
        else:
            for i in range(len(dfa.transitionOn)):
                printdfa(dfa.transitionOn[i], 0)


with open('streams/stream0.txt') as addresses:
	stream = addresses.readlines()
	stream = [x.strip('\n') for x in stream]

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
# print(permitdfa.transitionOn)
