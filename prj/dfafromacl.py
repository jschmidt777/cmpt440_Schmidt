# file: dfafromacl.py
# author: Joseph Schmidt
# course: CMPT 440
# assignment: semester project
# due date: 05MAY2017
# version: 1.0

# This file converts the acl into a dfa,
# taking in the list of either permit or deny statments.
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


from node import Node

def createdfa(statements):
    q0 = Node(acceptedState=False, nodeId=None)  # The start state
    stateptr = q0
    foundany = False  # found 'any' keyword in the statements list
    for i in range(len(statements)):
        if statements[i] == 'any':
            # Only create this state; we're accepting everything
            foundany = True
            q0.acceptedState = True
            break
    if not foundany:
        for i in range(len(statements)):
            stateptr = q0   # Reset for recursion
            octets = statements[i].split('.')
            print("Looking at octets---", octets)
            for j in range(len(octets)):
                print("Looking at octet", octets[j], j)
                print(stateptr)
                if len(stateptr.transitionOn) == 0:
                    if j == 3:
                        newNode = Node(acceptedState=True,
                                       nodeId=octets[j])
                        stateptr.transitionOn.append(newNode)
                        stateptr = newNode
                        print("Accepted state created", stateptr)
                    else:
                        print("Length is 0")
                        newNode = Node(acceptedState=False, nodeId=octets[j])
                        print('stateptr children', stateptr.transitionOn)
                        print('newNode children', newNode.transitionOn)
                        stateptr.transitionOn.append(newNode)
                        print('newNode children', newNode.transitionOn)
                        print('stateptr children', stateptr.transitionOn)
                        stateptr = newNode
                        print('stateptr children', stateptr.transitionOn)
                        print('newNode children', newNode.transitionOn)
                else:
                    foundnode = False
                    # found a node that represents the octet we're looking at
                    for k in range(len(stateptr.transitionOn)):
                        print("Looking at node",
                              stateptr.transitionOn[k].nodeId)
                        if stateptr.transitionOn[k].nodeId == octets[j]:
                            foundnode = True
                            stateptr = stateptr.transitionOn[k]
                            break
                # If we don't need to create a new node here it must be the last octet so
                # make it an accepting state...we're at the last octet so make node accepting
                    if not foundnode:
                        if j == 3:
                            newNode = Node(acceptedState=True,
                                           nodeId=octets[j])
                            stateptr.transitionOn.append(newNode)
                            stateptr = newNode
                            print("Accepted state created", stateptr)
                        else:
                            print("Non-Accepted state created")
                            newNode = Node(acceptedState=False,
                                           nodeId=octets[j])
                            stateptr.transitionOn.append(newNode)
                            stateptr = newNode
    return q0
