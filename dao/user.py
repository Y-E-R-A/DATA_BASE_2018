class UserDAO:
    def __init__(self):
        U1 = [122, 'Yomaira', 'Rivera', '17875556666', 'Hi everyone']
        U2 = [74, 'Gustavo', 'Hernandez', '17875788907', 'Today is a good day']
        U3 = [849, 'Abdias', 'Santiago', '19394786626', 'Im busy']
        U4 = [757, 'Maria', 'Rivera', '18002557899', 'Im single']
        U5 = [800, 'Maria', 'Guzman', '17875546666', 'Available']
        U6 = [87, 'Liza', 'Rivera', '19392333117', 'Available']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)
        self.data.append(U6)

    def getAllUsers(self):
        return self.data

    def getUserById(self, uid):
        result = []
        for r in self.data:
            if uid == r[0]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getUserByName(self, name):
        result = []
        for r in self.data:
            if name == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getUserByLastname(self, lastname):
        result = []
        for r in self.data:
            if lastname == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getUserByPhone(self, phone):
        # Phone is unique in a user instance
        for r in self.data:
            if phone == r[3]:
                return r
        return None