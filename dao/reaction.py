class ReactionDAO:
    def __init__(self):
        r1 = [1122,1,122,'Like']
        r2 = [274,2, 74,'Dislike']
        r3 = [3849,3, 849,'Like']
        r4 = [4757,4, 757,'Like']
        r5 = [5800,5, 800,'Dislike']

        self.data = []
        self.data.append(r1)
        self.data.append(r2)
        self.data.append(r3)
        self.data.append(r4)
        self.data.append(r5)

    def getAllReactions(self):
        return self.data

    def getByReactionId(self, rid):
        result = []
        for r in self.data:
            if rid == r[0]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getByMessageID(self, mid):
        result = []
        for r in self.data:
            if mid == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getByUserId(self, uid):
        result = []
        for r in self.data:
            if uid == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getByLikeDislike(self,rating):
        result = []
        for r in self.data:
            if rating == r[3]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

