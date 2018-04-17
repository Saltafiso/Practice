class BinaryTreeVertex():
    def __init__(self,value):
       self.value =value
       self.left = None
       self.right = None


class BinarySearchTree():

    def __init__(self):
        self.root = None
    def Insert(self,v):
        a = BinaryTreeVertex(v)
        # if tree is empty
        if self.root is None:
            self.root = a
        else:
            ptr = self.root
            # go to insert point
            while(ptr):
                if (v<ptr.value):
                    # found insert point
                    if ptr.left is None:
                        ptr.left = a
                        break;
                    else:
                        ptr = ptr.left
                else:
                    # found insert point
                    if ptr.right is None:
                        ptr.right = a
                        break;
                    else:
                        ptr = ptr.right
    # every thing below is as same as rbt
    def SearchPath(self,v):
        if self.root == None:
            return []
        else:
            res = []
            ptr = self.root
            while(ptr != None):
                res.append(ptr.value)
                if (v==ptr.value):
                    return res
                elif (v<ptr.value):
                    ptr = ptr.left
                else:
                    ptr = ptr.right
            return res
        
    def hf(self, ptr, height):
        if ptr is None:
            return 0
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
        while (ptr or stack):
            while ptr:
                stack.append(ptr)
                tag.append(0)
                ptr = ptr.left
            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                ptr = None
            else:
                ptr = stack[-1]
                ptr = ptr.right
                tag.pop()
                tag.append(1)
        return depth

