class CredentialsDAO:
    def __init__(self):

        # Credentials:[credential id, user id (foreign key), username, email, password]
        U1 = [1, 122, 'yomi', 'yomaira.rivera1@gmail.edu', 'YERA1234']
        U2 = [2, 74, 'silverKey', 'gus.hernandez@upr.edu', 'G1002AA']
        U3 = [3, 849, 'goldenChampion', 'gold71@hotmail.com', 'perros178']
        U4 = [4, 757, 'blueBird', 'sexygirl@hotmail.com', 'TNT900']
        U5 = [5, 800, 'ponytail', 'guzman.maria@yahoo.es', 'AbCdEf']
        U6 = [6, 87, 'rockstar', 'lola@yahoo.com', 'AbCdEf']

        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)
        self.data.append(U5)
        self.data.append(U6)

    def getAllCredentials(self):
        return self.data

    def getCredentialsById(self, id):
        result = []
        for r in self.data:
            if id == r[0]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getCredentialsByUserId(self, uid):
        result = []
        for r in self.data:
            if uid == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result


    def getCredentialsByUsername(self, username):
        result = []
        for r in self.data:
            if username == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getCredentialsByEmail(self, email):
        # Email is unique in a user instance
        for r in self.data:
            if email == r[3]:
                return r
        return None

