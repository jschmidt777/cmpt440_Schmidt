class Node:  # class, if, loops (everything is now underneath this)
    def __init__(self,
                 acceptedState=False,
                 nodeId=0,
                 transitionOn=[]):
        self.acceptedState = acceptedState
        self.nodeId = nodeId
        self.transitionOn = transitionOn

    def __repr__(self):
        return "Node %d (%r)" % (self.nodeId, self.acceptedState)
