from flask import jsonify, request
from dao.message import messageDAO

class MessagesHandler:

    #User dictionary
    def mapToMsgDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['date'] = row[1]
        result['body'] = row[2]
        result['sid']= row[3]
        return result


    def getAllMessages(self):
        result = messageDAO().getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))

        return jsonify(Messages=mapped_result)


    def getMessageById(self, mid):
        result = messageDAO().getMessageById(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))

            return jsonify(Messages=mapped_result)

    def getAllMessageBySenderId(self, sid):
            result = messageDAO().getAllMessageBySenderId(sid)
            mapped_result = []
            if not result:
                return jsonify(Error="NOT FOUND"), 404
            else:
                for r in result:
                    mapped_result.append(self.mapToMsgDict(r))

                return jsonify(Messages=mapped_result)

    def getMessageByDate(self, date):
        result = messageDAO().getMessageByDate(date)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))

            return jsonify(Messages=mapped_result)

    def getMessageByInfo(self, info):
        result = messageDAO().getMessageByInfo(info)
        mapped_result = []

        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))

            return jsonify(Messages=mapped_result)
