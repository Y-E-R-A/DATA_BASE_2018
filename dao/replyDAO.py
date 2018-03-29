class ReplyDAO:
    def __init__(self):
        # mid: is the id of the reply message
        # rid: is the id of the message that is being replied to
        # = [pid,mid, rid]
        # = [primaryId,messageId,replyToId]
        U1 = [54, 5, 4]
        U2 = [31, 3, 1]

        self.data = []
        self.data.append(U1)
        self.data.append(U2)

    def getAllReply(self):
        return self.data

    def getReplyById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getReplyByMessageId(self, id):
        result = []
        for r in self.data:
            if id == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getReplyByReplyToId(self, id):
        result = []
        for r in self.data:
            if id == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result