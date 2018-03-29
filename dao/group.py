class groupDAO:
    def __init__(self):
        G1 = [100, 'Data Bosses', 'Masters in the art of data', '02/15/2018', 74]
        G2 = [200, 'Rojo, Negro y Algo Mas', 'Los Leones de Ponce', '01/25/2018', 155]
        G3 = [300, 'Arquis Picasso', 'Brindando belleza a los circuitos', '02/16/2018', 122]
        G4 = [400, 'Los Pericos', '', '04/26/2018', 757]
        G5 = [500, 'Data Bosses', 'Masters of Procrastanition', '02/15/2018', 74]

        self.data = []
        self.data.append(G1)
        self.data.append(G2)
        self.data.append(G3)
        self.data.append(G4)
        self.data.append(G5)

    def getAllGroups(self):
        return self.data

    def getGroupsById(self, gid):
        result = []
        for r in self.data:
            if gid == r[0]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getGroupsByName(self, groupname):
        result = []
        for r in self.data:
            if groupname == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getGroupsByDescription(self, gdescription):
        result = []
        for r in self.data:
            if gdescription == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getGroupByCreation(self, gdate):
        result = []
        for r in self.data:
            if gdate == r[3]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getByUserId(self, uid):
        result = []
        for r in self.data:
            if uid == r[4]:
                result.append(r)
        if len(result) == 0:
            return None
        return result



