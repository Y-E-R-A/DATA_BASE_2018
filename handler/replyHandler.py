from flask import jsonify, request
from dao.replyDAO import ReplyDAO

class ReplyHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['id'] = row[0]
        result['mid'] = row[1]
        result['rid'] = row[2]
        return result

    def getAllReply(self):
        dao = ReplyDAO()
        result = dao.getAllReply()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Reply=mapped_result)

    def getReplyById(self, id):
        dao = ReplyDAO()
        result = dao.getReplyById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Reply=mapped)

    def getReplyByMessageId(self, id):
        dao = ReplyDAO()
        result = dao.getReplyByMessageId(id)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reply=mapped_result)

    def getReplyByReplyToId(self, id):
        dao = ReplyDAO()
        result = dao.getReplyByReplyToId(id)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reply=mapped_result)