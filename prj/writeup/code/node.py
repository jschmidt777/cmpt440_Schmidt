# file: node.py
# author: Joseph Schmidt
# course: CMPT 440
# assignment: semester project
# due date: 05MAY2017
# version: 1.0
#
# This file defines the Node class so dfa can be constructed
# It will output the processes verbosely as nodes are created
# to show it's validity. Used in dfafromacl.py.


class Node:  # class, if, loops (everything is now underneath this)
    def __init__(self,
                 acceptedState=False,
                 nodeId=0):
        self.acceptedState = acceptedState
        self.nodeId = nodeId
        self.transitionOn = []

    def __repr__(self):
        return "Node %s (%r)" % (self.nodeId, self.acceptedState)
