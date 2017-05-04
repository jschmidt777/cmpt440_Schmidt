# file: transition.py
# author: Joseph Schmidt
# course: CMPT 440
# assignment: semester project
# due date: 05MAY2017
# version: 1.0
#
# This file defines the method which 
# does the actual enforcement of the created dfa on a
# ip source stream specified by the user.
# Params: The dfa to enforce and the stream of addresses
# Returns: The list of addresses accepted by the dfa

def transition(dfa, stream):
    arr = []
    # The list to be returned.
    # The print out order in main.py will show if it's for deny or permit
    stateptr = dfa  # The start state
    if dfa.acceptedState is True and dfa.nodeId is None:
        # which means we must be dealing with a dfa which permits/denys any
        for i in range(len(stream)):
            arr.append(stream[i])
    else:
        for i in range(len(stream)):
            stateptr = dfa # Reset for recursion
            octets = stream[i].split('.')
            print("Looking at octets---", octets)
            for j in range(len(octets)):
                print("Looking at octet", octets[j], j)
                print(stateptr)
                for k in range(len(stateptr.transitionOn)):
                    print("Looking at node ",
                    stateptr.transitionOn[k].nodeId, " for processing")
                    if stateptr.transitionOn[k].nodeId == octets[j]:
                        foundnode = True
                        stateptr = stateptr.transitionOn[k]
                        print(stateptr.acceptedState)
                        if j == 3 and stateptr.acceptedState == True:
                            print("Added "+ stream[i]+ " to output list")
                            arr.append(stream[i])
                        break

    return arr
