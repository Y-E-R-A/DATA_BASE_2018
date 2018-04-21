from flask import jsonify, request
from dao.group import groupDAO

class GroupHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['gdesc'] = row[2]
        result['gcreation'] = row[3]
        result['uid'] = row[4]

        return result


    def getAllGroups(self):
        dao = groupDAO()
        result = dao.getAllGroups()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)


    def getGroupsById(self, gid):
        dao = groupDAO()
        result = dao.getGroupsById(gid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getGroupsByName(self, gname):
        dao = groupDAO()
        result = dao.getGroupsByName(gname)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getGroupByDescription(self, gdescription):
        dao = groupDAO()
        result = dao.getGroupsByDescription(gdescription)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getGroupByCreation(self, gcreation):
        dao = groupDAO()
        result = dao.getGroupByCreation(gcreation)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getByUserId(self, uid):

        dao = groupDAO()
        result = dao.getByUserId(uid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

