class mediaDAO:
    def __init__(self):
        ME1 = [15, 'Avengers', 'Youtube','Video', 74]
        ME2 = [30, 'Simple Men', 'Vevo','Video', 155]
        ME3 = [45, 'Club Salsa', 'Android Disc','Photo',  122]
        ME4 = [60, 'El Yunque', 'Iphone Disc','Photo', 757]
        ME5 = [575,'Run for Cover', 'Vevo','Video',  74]

        self.data = []
        self.data.append(ME1)
        self.data.append(ME2)
        self.data.append(ME3)
        self.data.append(ME4)
        self.data.append(ME5)

    def getAllMedia(self):
        return self.data

    def getMediaByID(self, meid):
        result = []
        for r in self.data:
            if meid == r[0]:
                result.append(r)
        if len(result) == 0:
            return None
        return result


    def getMediaByName(self, mename):
        result = []
        for r in self.data:
            if mename == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getMediaByAddress(self, meaddress):
        result = []
        for r in self.data:
            if meaddress == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getMediaByType(self, metype):
        result = []
        for r in self.data:
            if metype == r[3]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getByMessageId(self, mid):
        result = []
        for r in self.data:
            if mid == r[4]:
                result.append(r)
        if len(result) == 0:
            return None
        return result


