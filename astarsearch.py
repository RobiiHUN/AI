class AStarNodeSelector:
    def nextNode(self, search, openList, closedList):
        if not openList:
            return None
        return min(openList, key=lambda node: search.heur(node.location) + node.cost)