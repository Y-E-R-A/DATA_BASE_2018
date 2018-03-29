class messageDAO:
    def __init__(self):
        mes1 = [1,'04-26-2018', '12:00 pm', 'Haciendo el proyecto de db', 122];
        mes2 = [2,'04-26-2018', '12:10 pm', 'Dale, me reuno pronto', 74];
        mes3 = [3,'04-26-2018', '1:25 pm', 'Ya sali de clase, voy por ahi', 122];
        mes4 = [4,'04-26-2018', '12:10 pm', 'Esto se termina hoy amanecido', 74];

        self.data = []
        self.data.append(mes1)
        self.data.append(mes2)
        self.data.append(mes3)
        self.data.append(mes4)


    def getAllMessages(self):
        return self.data

    def getMessageById(self, mid):
        result = []
        for r in self.data:
            if mid == r[0]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getAllMessageBySenderId(self, sid):
        result = []
        for r in self.data:
            if sid == r[4]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getMessageByDate(self, date):
        result = []
        for r in self.data:
            if date == r[1]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getMessageByTime(self, time):
        result = []
        for r in self.data:
            if time == r[2]:
                result.append(r)
        if len(result) == 0:
            return None
        return result

    def getMessageByBody(self, body):
        result = []
        for r in self.data:
            if body == r[3]:
                result.append(r)
        if len(result) == 0:
            return None
        return result