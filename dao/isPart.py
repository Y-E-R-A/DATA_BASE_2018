class IsPartDAO:
    def __init__(self):
        # = [pid,mid, gid]
        # = [primaryId,messageId,groupId]
        U1 = [5100, 5, 100]
        U2 = [4100, 4, 100]
        U3 = [2200, 2, 300]
        U4 = [3200, 3, 200]
        U5 = [1200, 1, 200]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)

    def getAllIsPart(self):
        return self.data

    def getIsPartById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getIsPartByMessageId(self, id):
        result = []
        for r in self.data:
            if id == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getIsPartByGroupId(self, id):
        result = []
        for r in self.data:
            if id == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result