class Node:  # class, if, loops (everything is now underneath this)
    def __init__(self,
                 acceptedState=False,
                 nodeId=0):
        self.acceptedState = acceptedState
        self.nodeId = nodeId

    def __repr__(self):
        return "Node %d (%r)" % (self.nodeId, self.acceptedState)
