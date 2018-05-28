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
    def buildGroupDict(self,gid, gname, gdescription, gcreation, adminId ):
        result = {}
        result['gid'] = gid
        result['gname'] = gname
        result['gdesc'] = gdescription
        result['gcreation'] = gcreation
        result['uid'] = adminId
        return result
    def mapGroupMessagesToDict(self, row):
        result = {}
        #result['gname'] = row[0]
        #result['minfo'] = row[1]
        #result['uid'] = row[2]
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['mid'] = row[2]
        result['minfo'] = row[3]
        result['mdate'] = row[4]
        result['uid'] = row[5]
        result['cusername'] = row[6]
        result['likes'] = row[7]
        result['dislikes'] = row[8]
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


    def insertCredentialsJSON(self,json):

        gname = json.get('gName')
        gdescription = json.get('gdescription');
        gcreation = json.get('gcreation');
        adminId = json.get('gadminID');
        print("GroupHandler")
        print(gname)
        print(gdescription)
        print(gcreation)
        print(adminId)


        if gname and gcreation and gdescription and adminId :
            gid = groupDAO().insert(gname, gdescription, gcreation,adminId)
            mapped_result = self.buildGroupDict(gid, gname, gdescription, gcreation, adminId)
            return jsonify(Group=mapped_result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 404