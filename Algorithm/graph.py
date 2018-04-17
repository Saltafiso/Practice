class node :
    def __init__(self,name,neighbour):
        self.name = name
        self.neighbour = neighbour
        self.visited = False;
        self.added = False;

class graph:
    def __init__(self,case,size):
        self.case = case
        self.size = size
        self.list = []

    def add(self,node):
        # add node to graph
        self.list.append(node)

    def bfs(self,v):
        # Q is queue
        Q = []
        res = 0
        # search the node with name v
        node= [i for i in self.list if i.name == v][0]
        Q.append(node)
        # set the added Boolean for v to True 
        node.added = True 
        while Q != []: 
            x = Q[0]
            # remove first
            Q = Q[1:] 
            # mark x visited
            x.visited = True
            
            
            for y in x.neighbour :
                # search the node with name y
                n_node = [i for i in self.list if i.name == y[0]][0]
                if (not n_node.visited) and (not n_node.added): 
                    Q.append(n_node)
                    # set the added Boolean for y to True
                    n_node.added = True
                    # add weight of edge to res
                    res += int(y[1])
        return res

    def Prim(self,v):
        chosen_edges = 0
        T = [v]
        # R is the rest of the vertices
        R = [i.name for i in self.list]
        R.remove(v)
        # take the set of all edges and sort them into ascending-weight order
        AllEdges = [k for i in [list(map((lambda x:x + (j.name,)),j.neighbour)) for j in self.list] for k in i]
        AllEdges.sort(key=lambda tup:int(tup[1]))
        # keep going until T contains all 
        while len(T) < int(self.size):
            # let e be the least-weight edge that has one end in T and one end in R
            for i in AllEdges:
                if (i[0] in R and i[2] in T) or (i[2] in R and i[0] in T):
                    e = i
                    break
#           edgeTR = [i for i in AllEdges if (i[0] in R and i[2] in T) or (i[2] in R and i[0] in T)]
#           e = edgeTR[0]
            # add e to chosen_edges
            chosen_edges += int(e[1])
            # find which to add/remove
            tmp = e[0] if e[0] in R else e[2]
            T.append(tmp)
            R.remove(tmp)
            # not necessary
            AllEdges.remove(e)
#           map((lambda x:AllEdges.remove(x)), edgeTR)
        return chosen_edges
