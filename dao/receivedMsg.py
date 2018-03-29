class ReceivedMsgDAO:
    def __init__(self):
        # = [pid,uid, mid]
        # = [primaryId,UserId,messageId]
        U1 = [1221, 122, 1]
        U2 = [742, 74, 2]
        U3 = [1223, 122, 3]
        U4 = [744, 74, 4]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)


    def getAllReceivedMsg(self):
        return self.data

    def getReceivedMsgById(self, msgSid):
        for r in self.data:
            if msgSid == r[0]:
                return r
        return None


    def getReceivedMsgByUserId(self, id):
        result = []
        for r in self.data:
            if id == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getReceivedMsgByMessageId(self, id):
        result = []
        for r in self.data:
            if id == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result