from flask import jsonify, request
from dao.isPart import IsPartDAO

class IsPartHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['id'] = row[0]
        result['mid'] = row[1]
        result['gid'] = row[2]
        return result

    def getAllIsPart(self):
        dao = IsPartDAO()
        result = dao.getAllIsPart()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(PartOfGroup=mapped_result)

    def getIsPartById(self, id):
        dao = IsPartDAO()
        result = dao.getIsPartById(id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(PartOfGroup=mapped)

    def getIsPartByMessageId(self, id):
        dao = IsPartDAO()
        result = dao.getIsPartByMessageId(id)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(PartOfGroup=mapped_result)

    def getIsPartByGroupId(self, id):
        dao = IsPartDAO()
        result = dao.getIsPartByGroupId(id)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(PartOfGroup=mapped_result)