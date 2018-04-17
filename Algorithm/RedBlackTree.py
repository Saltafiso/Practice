class RBTreeVertex():
    def __init__(self,value):
       self.value =value
       self.left = None
       self.right = None
       self.parent = None
       self.color = "R"


class RBTree():

    def __init__(self):
        self.root = None
    # to fix tree after inserting
    def fixtree(self,a):
        # base case, color root black
        if (a.parent == None):
            self.root = a
            a.color = "B"
            return
        # do fix
        if (a.parent.color == "R"):
            g = a.parent.parent
            p = a.parent
            s = g.right if g.left == p else g.left
            # changing color and do the recursion for grand parents
            if (s != None and s.color == "R"):
                p.color = "B"
                s.color = "B"
                g.color = "R"
                self.fixtree(g)
            # rotation
            else:
                # double rotations, rotate to left first, wait for second rotation
                if (a == p.right and p == g.left):
                    self.rl(a)
                    a = p
                    
                # double rotations, rotate to right first, wait for second rotation
                elif (a == p.left and p == g.right):
                    self.rr(a)
                    a = p
                # update grandparents, parents, changing color of parent and grandparent
                g = a.parent.parent
                p = a.parent
                p.color = "B"
                g.color = "R"
                # do single rotation, rotate to rihgt
                if (a == p.left and p == g.left):
                    self.rr(p)
                # do single rotation, rotate to left
                else:
                    self.rl(p)


    def rl(self,n):
        # if n have no parent, n is root
        if (n.parent == None):
            self.root  = n
            return
        g = n.parent.parent
        p = n.parent
        tmp=n.left
        # give current's child to parent
        p.right = tmp
        # changing parent pointer
        if (tmp != None):
            tmp.parent = p
        # give parent to current's child
        n.left = p
        # changing parent pointer
        p.parent = n
        # if parent is root, change root to chrrent
        if(self.root == p):
            self.root = n
            n.parent = None
        n.parent = g
        # if grandparent exist, give n to grandparent's child 
        if (g != None):
            if(g.left == p):
                g.left = n
            else:
                g.right = n

    def rr(self,n):
        # same as rl, but change left to right 
        if (n.parent == None):
            self.root  = n
            return
        g = n.parent.parent
        p = n.parent
        tmp=n.right
        p.left = tmp
        if (tmp != None):
            tmp.parent = p
        n.right = p
        p.parent = n
        if(self.root == p):
            self.root = n
            n.parent = None
        n.parent = g
        if (g != None):
            if(g.left == p):
                g.left = n
            else:
                g.right = n



    def Insert(self,v):
        a = RBTreeVertex(v)
        # if tree is empty
        if self.root is None:
            a.color = "B"
            self.root = a
        else: 
            ptr = self.root
            # go to insert point
            while(ptr):
                if (v<ptr.value):
                    # found insert point
                    if ptr.left is None:
                        a.parent = ptr
                        ptr.left = a
                        self.fixtree(a);
                        break;
                    else:
                        ptr = ptr.left
                else:
                    # found insert point
                    if ptr.right is None:
                        a.parent = ptr
                        ptr.right = a
                        self.fixtree(a);
                        break;

                    else:
                        ptr = ptr.right
            self.root.color = "B"


    def SearchPath(self,v):
        if self.root == None:
            return []
        else:
            res = []
            ptr = self.root
            while(ptr != None):
                # append current value to result
                res.append((ptr.value,ptr.color))
                # if found, return result
                if (v==ptr.value):
                    return res
                # if not, go to branches
                elif (v<ptr.value):
                    ptr = ptr.left
                else:
                    ptr = ptr.right
            # if Not found, return res
            return res

    def hf(self, ptr, height):
        if ptr is None:
            return 0
        # add the current height and the height of their child
        return height + self.hf((ptr.right), (height+1)) + self.hf((ptr.left), (height+1))

    def Total_Depth (self):
        ptr = self.root
        return self.hf(ptr, 1)
        


    def Max_Depth (self):
        ptr = self.root
        if not ptr:
            return 0
        depth = 0
        stack = []
        tag = []
        # start iteration go though all path
        while (ptr or stack):
            # go to bottom left
            while ptr:
                stack.append(ptr)
                tag.append(0)
                ptr = ptr.left
            # if path ends, find the max depth and go back to the last node that have left child, and go to their right child
            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                ptr = None
            # go to right child and set the tag
            else:
                ptr = stack[-1]
                ptr = ptr.right
                tag.pop()
                tag.append(1)
        return depth

