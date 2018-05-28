from flask import jsonify, request
from dao.groupsDAO import groupDAO

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

    def mapGroupMessagesToDict(self, row):
        result = {}
        #result['gname'] = row[0]
        #result['minfo'] = row[1]
        #result['uid'] = row[2]
        result['gid'] = row[0]
        result['mid'] = row[1]
        result['minfo'] = row[2]
        result['mdate'] = row[3]
        result['uid'] = row[4]
        result['cusername'] = row[5]
        return result

    def getAllGroups(self):
        dao = groupDAO()
        result = dao.getAllGroups()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Group =mapped_result)


    def getGroupsById(self, gid):
        dao = groupDAO()
        result = dao.getGroupsById(gid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Group =mapped_result)

    def getGroupsByName(self, gname):
        dao = groupDAO()
        result = dao.getGroupsByName(gname)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Group =mapped_result)

    def getGroupByDescription(self, gdescription):
        dao = groupDAO()
        result = dao.getGroupsByDescription(gdescription)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Group =mapped_result)

    def getGroupByCreation(self, gcreation):
        dao = groupDAO()
        result = dao.getGroupByCreation(gcreation)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Group =mapped_result)

    def getByUserId(self, uid):

        dao = groupDAO()
        result = dao.getByUserId(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Group =mapped_result)

    def getMessagesByGroupId(self, uid):

        dao = groupDAO()
        result = dao.getMessagesByGroupId(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapGroupMessagesToDict(r))
            return jsonify(GroupMessages =mapped_result)

