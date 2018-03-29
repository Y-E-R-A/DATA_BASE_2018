class AdminDAO:
    def __init__(self):
        # = [pid,uid, gid]
        # = [primaryId,userId,groupId]
        U1 = [122100, 122, 100]
        U2 = [122200, 122, 200]
        U3 = [74200, 74, 200]
        U4 = [757300, 757, 300]
        U5 = [849400, 849, 400]
        U6 = [757400, 757, 400]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)
        self.data.append(U6)

    def getAllAdmin(self):
        return self.data

    def getAdminById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getAdminByUserId(self, id):
        result = []
        for r in self.data:
            if id == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getAdminByGroupId(self, id):
        result = []
        for r in self.data:
            if id == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result