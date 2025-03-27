class SQL(object):
    def __init__(self, names, columns):
        self.tablenames = names
        self.tablecolcounts = {}
        self.tablecontent = {}
        self.id = {}
        for i in range(len(names)):
            self.tablecontent[names[i]] = []
            self.tablecolcounts[names[i]] = columns[i]
            self.id[names[i]] = []
    def ins(self, name, row):
        if not name in self.tablenames:
            return False
        if not len(row) == self.tablecolcounts[name]:
            return False
        self.tablecontent[name].append(row)
        nextid = 1 if 0 == len(self.id[name]) else 1 + self.id[name][-1]
        self.id[name].append(nextid)
        return True
    def rmv(self, name, rowId):
        if not name in self.tablenames:
            return False
        if rowId > self.id[name][-1]:
            return False
        ix = self.id[name].index(rowId)
        self.tablecontent[name] = self.tablecontent[name][:ix] + self.tablecontent[name][ix+1:]
        self.id[name] = self.id[name][:ix] + self.id[name][ix+1:]
    def sel(self, name, rowId, columnId):
        if not name in self.tablenames:
            return None
        if columnId > self.tablecolcounts[name]:
            return None
        try:
            ix = self.id[name].index(rowId)
        except:
            return None
        return self.tablecontent[name][ix][columnId - 1] # columnId's are 1-based
    def csv(self,values):
        r = ""
        for i in range(len(values)):
            r += f"{values[i]}, "
        return r[:-2]
    def exp(self, name):
        if not name in self.tablenames:
            return False
        rowstrings = []
        for i in range(len(self.id[name])):
            rowstrings.append(self.csv([self.id[name][i]]+self.tablecontent[name][i]))
        return rowstrings

# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)

t1f = ["SQL","ins","sel","ins","exp","rmv","sel","exp"]
t1a = [[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]