from readacl import permits, denys
from node import Node
# TODO: Verbose mode for running pcap file src ips against dfa(s)
# from automata.fa.dfa import DFA
# DFA which matches 192.168.1.x addresses or word 'any' based on acl
# This is based off of the diagram in my report for this project
# (reference as needed)
if len(permits) is not 0:
    statecount = 0  # Used to add states to the DFA
    q0 = Node(acceptedState=False, nodeId=0)  # The start state
    stateptr = q0

    def createpermits():
        for i in range(len(permits)):
            if permits[i] == 'any':
                # Only create this state; we're accepting everything
                q4 = Node(acceptedState=True, nodeId=4)
                q0.transitionOn.append('any')
                break
        else:
            q0.transitionOn.append('192.')
            q1 = Node(acceptedState=False, nodeId=1, transitionOn=['168.'])
            q2 = Node(acceptedState=False, nodeId=2, transitionOn=['1.'])
            q3 = Node(acceptedState=False, nodeId=3)
            q4 = Node(acceptedState=True, nodeId=4)
            # Transitions added here as we look at what addresses are accepted
        for i in range(len(permits)):
            # Split on 192.168.1. to just get end number
            # Append to q3.transitionOn
            # This will be what is read when we transition
    def transition():
        if
# Else do nothing. Do not create a dfa for permits.
