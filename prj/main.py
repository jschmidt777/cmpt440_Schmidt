# Nullifies circular dependencies when loaded in packages.
# from node import Node
# newNode = Node()
# print(newNode)
# newNode1 = Node(acceptedState=True, nodeId=5)
# print(newNode1)
from readacl import lines, permits, denys
print(lines)
print("Any repeat statements were removed.")
print(permits)
print(denys)
