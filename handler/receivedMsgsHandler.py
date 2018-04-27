from flask import jsonify, request
from dao.receivedMsg import ReceivedMsgDAO

class ReceivedMsgHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['id'] = row[0]
        result['uid'] = row[1]
        result['mid'] = row[2]
        return result

    def getAllReceivedMsg(self):
        dao = ReceivedMsgDAO()
        result = dao.getAllReceivedMsg()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(ReceivedMsg=mapped_result)

    def getReceivedMsgById(self, id):
        dao = ReceivedMsgDAO()
        result = dao.getReceivedMsgById(id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(ReceivedMsg=mapped)

    def getReceivedMsgByUserId(self, uid):
        dao = ReceivedMsgDAO()
        result = dao.getReceivedMsgByUserId(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(ReceivedMsg=mapped_result)

    def getReceivedMsgByMessageId(self, mid):
        dao = ReceivedMsgDAO()
        result = dao.getReceivedMsgByMessageId(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(ReceivedMsg=mapped_result)