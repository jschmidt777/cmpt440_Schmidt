# Nullifies circular dependencies when loaded in packages.
# from node import Node
# newNode = Node()
# print(newNode)
# newNode1 = Node(acceptedState=True, nodeId=5)
# print(newNode1)
from readacl import lines, permits, denys
from dfafromacl import createdfa
print(lines)
print("Any repeat statements were removed.")
print(permits)
print(len(permits))
print(denys)
print("DFA being created for permit statements.")
# show the nodes for this dfa
print("DFA being created for deny statements.")
# show the nodes for this dfa
permitdfa = createdfa(permits)
denydfa = createdfa(denys)
nodetoprint = True

def printdfa(dfa, lvl=0):
	if dfa.nodeId is not None:
		stringtoprint = ""  # Identifies the indentation level/depth of the node in the dfa
		for i in range(lvl):
			stringtoprint += "-"
		print(stringtoprint + dfa.nodeId)
		if len(dfa.transitionOn) > 0:  # If there are childern to the node
			# print("Found children ", dfa )
			# print("Children ", dfa.transitionOn)
			for i in range(len(dfa.transitionOn)):
				# print("Looking at node: ", dfa.transitionOn[i])
				printdfa(dfa.transitionOn[i], lvl+1)
	else:
		for i in range(len(dfa.transitionOn)):
			printdfa(dfa.transitionOn[i], 0)

printdfa(permitdfa)
#print(permitdfa.transitionOn)