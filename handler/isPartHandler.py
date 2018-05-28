from flask import jsonify, request
from dao.isPartDAO import IsPartDAO

class IsPartHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['gid'] = row[1]
        #result['gid'] = row[2]
        return result

    def buildDict(self, mid,gid):
        result = {}
        result['mid'] = mid
        result['gid'] = gid
        #result['gid'] = row[2]
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

    def insertCredentialsJSON(self, json):
        mid = json.get('mid')
        gid = json.get('gid')

        if mid and gid:
            IsPartDAO().insert(mid,gid)
            mapped_result = self.buildDict(mid,gid)
            return jsonify(User=mapped_result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 404