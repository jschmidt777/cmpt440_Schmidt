

def transition(dfa, stream):
    arr = []
    # The list to be returned.
    # The print out order will show if it's for deny or permit
    # The start state
    stateptr = dfa  # first node in the dfa that just gives the q0 node
    if dfa.acceptedState is True and dfa.nodeId is None:
        # which means we must be dealing with a dfa which permits/denys any
        for i in range(len(stream)):
            arr.append(stream[i])
        return arr
#     else:
#         for i in range(len(stream)):
#             stateptr = dfa # Reset for recursion
#             octets = stream[i].split('.')
#             print("Looking at octets---", octets)
#             for j in range(len(octets)):
#                 print("Looking at octet", octets[j], j)
#                 print(stateptr)
#                 if len(stateptr.transitionOn) == 0:
#                     print("Length is 0")
#                     newNode = Node(acceptedState=False, nodeId=octets[j])
#                     print('stateptr children', stateptr.transitionOn)
#                     print('newNode children', newNode.transitionOn)
#                     stateptr.transitionOn.append(newNode)
#                     print('newNode children', newNode.transitionOn)
#                     print('stateptr children', stateptr.transitionOn)
#                     stateptr = newNode
#                     print('stateptr children', stateptr.transitionOn)
#                     print('newNode children', newNode.transitionOn)
#                 else:
#                     foundnode = False
#                     # found a node that represents the octet we're looking at
#                     for k in range(len(stateptr.transitionOn)):
#                         print("Looking at node",
#                               stateptr.transitionOn[k].nodeId)
#                         if stateptr.transitionOn[k].nodeId == octets[j]:
#                             foundnode = True
#                             stateptr = stateptr.transitionOn[k]
#                             break
# # If we don't need to create a new node here it must be the last octet so
# # make it an accepting state...we're at the last octet so make node accepting
#                     if not foundnode:
#                         if j == 3:
#                             newNode = Node(acceptedState=True,
#                                            nodeId=octets[j])
#                             stateptr.transitionOn.append(newNode)
#                             stateptr = newNode
#                             print("Accepted state created", stateptr)
#                         else:
#                             print("Non-Accepted state created")
#                             newNode = Node(acceptedState=False,
#                                            nodeId=octets[j])
#                             stateptr.transitionOn.append(newNode)
#                             stateptr = newNode
#     return q0
