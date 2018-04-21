from flask import jsonify, request
from dao.participateInDAO import PinDAO

class ParticipationHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['id'] = row[0]
        result['uid'] = row[1]
        result['gid'] = row[2]
        return result

    def getAllParticipants(self):
        dao = PinDAO()
        result = dao.getAllPin()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(ParticipateInRelation=mapped_result)

    def getParticipantsByPId(self, id):
        dao = PinDAO()
        result = dao.getPinById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(ParticipateInRelation=mapped)

    def getPinByUserId(self, id):
        dao = PinDAO()
        result = dao.getPinByUserId(id)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(ParticipateInRelation=mapped_result)

    def getParticipantsByGroupId(self, id):
        dao = PinDAO()
        result = dao.getPinByGroupId(id)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(ParticipateInRelation=mapped_result)