class Node:  # class, if, loops (everything is now underneath this)
    def __init__(self,
                 acceptedState=False,
                 nodeId=0):
        self.acceptedState = acceptedState
        self.nodeId = nodeId
        self.transitionOn = []

    def __repr__(self):
        return "Node %s (%r)" % (self.nodeId, self.acceptedState)
