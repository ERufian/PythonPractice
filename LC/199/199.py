class Solution(object):
    def rightSideView(self, root):
        if 0 == len(root):
            return []
        currentlayer = [root[0]]
        edge = [root[0]]
        i = 1
        while i < len(root):
            oldlayer = currentlayer.copy()
            currentlayer = []
            for j in range(len(oldlayer)):
                if oldlayer[j] == None:
                    currentlayer += [None, None]
                else:
                    currentlayer += [None if i >= len(root) else root[i], None if i+1 >= len(root) else root[i+1]]
                    i += 2
            for j in range(len(currentlayer)-1, -1, -1):
                if not currentlayer[j] is None:
                    edge.append(currentlayer[j])
                    break
        return edge
    
    def completer(self, root):
        if 0 == len(root):
            return []
        complete = [root[0]]
        layer = {"start":0, "len":1}
        i = 1
        while i < len(root):
            for j in range(layer.len):
                if complete[layer["start"]+j] == None:
                    complete += [None, None]
                else:
                    complete += [None if i >= len(root) else root[i], None if i+1 >= len(root) else root[i+1]]
                    i += 2
            layer["start"] += layer["len"]
            layer["len"] *= 2
        return complete