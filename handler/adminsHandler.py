from flask import jsonify, request
from dao.admin import AdminDAO

class AdminHandler:

    #User dictionary
    def mapToDict(self, row):
        result = {}
        result['id'] = row[0]
        result['uid'] = row[1]
        result['gid'] = row[2]
        return result

    def getAllAdmin(self):
        dao = AdminDAO()
        result = dao.getAllAdmin()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Admin=mapped_result)

    def getAdminById(self, id):
        dao = AdminDAO()
        result = dao.getAdminById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Admin=mapped)

    def getAdminByUserId(self, id):
        dao = AdminDAO()
        result = dao.getAdminByUserId(id)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Admin=mapped_result)

    def getAdminByGroupId(self, id):
        dao = AdminDAO()
        result = dao.getAdminByGroupId(id)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Admin=mapped_result)