class PinDAO:
    def __init__(self):
        U1 = [122100, 122, 100]
        U2 = [74100, 74, 100]
        U3 = [849100, 849, 100]
        U4 = [122200, 122, 200]
        U5 = [74200, 74, 200]
        U6 = [849200, 849, 200]
        U7 = [757300, 757, 300]
        U8 = [74400, 74, 400]
        U9 = [849400, 849, 400]
        U10 = [757400, 757, 400]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)
        self.data.append(U6)
        self.data.append(U7)
        self.data.append(U8)
        self.data.append(U9)
        self.data.append(U10)

    def getAllPin(self):
        return self.data

    def getPinById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getPinByUserId(self, id):
        result = []
        for r in self.data:
            if id == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getPinByGroupId(self, id):
        result = []
        for r in self.data:
            if id == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result