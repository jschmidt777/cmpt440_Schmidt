# Nullifies circular dependencies when loaded in packages.
from node import Node
from readacl import lines
newNode = Node()
print(newNode)
newNode1 = Node(acceptedState=True, nodeId=5)
print(newNode1)
print(lines)
