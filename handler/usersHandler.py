from flask import jsonify, request
from dao.users import UserDAO

class UsersHandler:

    #User dictionary
    def mapToUserDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['cid'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['description'] = row[5]
        return result


    def getAllUsers(self):
        result = UserDAO().getAllUsers()
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserDict(r))

            return jsonify(User=mapped_result)


    def getUserById(self, uid):
        result = UserDAO().getUserById(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                 mapped_result.append(self.mapToUserDict(r))

            return jsonify(User= mapped_result)

    def getUserByName(self, name):
        result = UserDAO().getUserByName(name)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(User= mapped_result)

    def getUserByLastname(self, lastname):
        result = UserDAO().getUserByLastname(lastname)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(User= mapped_result)

    def getUserByPhone(self, phone):
        # The first user with 'phone' will be the mapped result
        result = UserDAO().getUserByPhone(phone)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapToUserDict(result)
            return jsonify(User=mapped_result)

    def getUserByDescription(self, udescription):
        # The first user with 'phone' will be the mapped result
        result = UserDAO().getUserByDescription(udescription)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapToUserDict(result)
            return jsonify(User=mapped_result)

    #def insert(self, uid, cid, ufirst_name, ulast_name,phone,udescription):
        #cursor = self.conn.cursor()
        #query = "insert into Users(uid, cid, ufirst_name, ulast_name,phone,udescription) values (%s, %s, %s, %s, %s, %s) returning uid;"
        #cursor.execute(query, (uid, cid, ufirst_name, ulast_name,phone,udescription))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()
        #return sid
