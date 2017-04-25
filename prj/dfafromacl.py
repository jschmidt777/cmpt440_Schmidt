from node import Node
# TODO: Verbose mode for running pcap file src ips against dfa(s)
# from automata.fa.dfa import DFA
# DFA which matches 192.168.1.x addresses or word 'any' based on acl
# This is based off of the diagram in my report for this project
# (reference as needed)
# Takes in the list of either permit or deny statments


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
                print("Looking at octet", octets[j])
                print(stateptr)
                if len(stateptr.transitionOn) == 0:
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
                    if not foundnode:
                        newNode = Node(acceptedState=False, nodeId=octets[j])
                        stateptr.transitionOn.append(newNode)
                        stateptr = newNode
    return q0
