# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#


class Node(object):

    def __init__(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()


class Edge(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class WeightedEdge(Edge):

    def __init__(self, src, dest, distance, outdoors):
        Edge.__init__(self, Node(src), Node(dest))
        self.distance = distance
        self.outdoors = outdoors

    def getTotalDistance(self):
        return self.distance

    def getOutdoorDistance(self):
        return self.outdoors

    def __str__(self):
        return '%s->%s(%d, %d)' % (self.src, self.dest, self.distance, self.outdoors)


class Digraph(object):

    """
    A directed graph
    """

    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See
        # http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges
            # list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]


class WeightedDigraph(Digraph):

    def __init__(self):
        Digraph.__init__(self)
        self.distances = {}
        self.outdoors = {}
        self.edgelst = []

    def addNode(self, node):
        Digraph.addNode(self, Node(node))

    def childrenOf(self, node):
        return Digraph.childrenOf(self, Node(node))

    def addEdge(self, edge):
        src = Node(edge.getSource())
        dest = Node(edge.getDestination())
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')

        if src in self.edges.keys():
            self.edges[src].append(
                [dest, (float(edge.getTotalDistance()), float(edge.getOutdoorDistance()))])
        else:
            self.edges[src] = [
                [dest, (float(edge.getTotalDistance()), float(edge.getOutdoorDistance()))]]

        self.edgelst.append(edge)
        '''
        if not self.distances.get(src.getName()+dest.getName()):
            self.distances[
                src.getName()+dest.getName()] = [float(edge.getTotalDistance())]
        else:
            self.distances[src.getName()+dest.getName()].append(float(edge.getTotalDistance()))
        
        if not self.outdoors.get(src.getName()+dest.getName()):
            self.outdoors[
                src.getName()+dest.getName()] = [float(edge.getOutdoorDistance())]
        else:
            self.outdoors[src.getName()+dest.getName()].append(float(edge.getOutdoorDistance()))
        '''

    def __str__(self):
        res = ''
        for e in self.edgelst:
            res = '{0}{1}->{2}({3}, {4})\n'.format(res, e.getSource(), e.getDestination(
            ), float(e.getTotalDistance()), float(e.getOutdoorDistance()))
        return res[:-1]
