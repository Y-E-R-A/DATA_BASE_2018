from flask import jsonify, request
from dao.usersDAO import UserDAO

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

    #User dictionary
    def mapToUsertoGroupDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['gid'] = row[1]
        result['gname'] = row[2]
        result['gdescription'] = row[3]
        result['gdate'] = row[4]
        return result

    def mapToUserInfoDict(self, row):
        result = {}
        result['cid'] = row[0]
        result['uid'] = row[1]
        result['firstname'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['description'] = row[5]
        result['username'] = row[6]
        result['email'] = row[7]
        return result

    def buildUserDict(self, uid,cid,firstname,lastname,phone,description):
        result = {}
        result['uid'] = uid
        result['cid'] = cid
        result['firstname'] = firstname
        result['lastname'] = lastname
        result['phone'] = phone
        result['description'] = description
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

    def getUserGroupsByUserId(self, uid):
        result = UserDAO().getUserGroupsById(uid)
        mapped_result = []

        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUsertoGroupDict(r))
            return jsonify(User= mapped_result)

    def getUserInformation(self, uid):
        result = UserDAO().getUserInformationByUserId(uid)
        mapped_result = []

        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserInfoDict(r))
            return jsonify(User= mapped_result)

    #def insert(self, uid, cid, ufirst_name, ulast_name,phone,udescription):
        #cursor = self.conn.cursor()
        #query = "insert into Users(uid, cid, ufirst_name, ulast_name,phone,udescription) values (%s, %s, %s, %s, %s, %s) returning uid;"
        #cursor.execute(query, (uid, cid, ufirst_name, ulast_name,phone,udescription))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()
        #return sid

    def mapToUserMessageDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['mid'] = row[1]
        result['uName'] = row[2]
        result['uLame'] = row[3]
        result['mInfo'] = row[4]
        result['mDate'] = row[5]
        result['like'] = row[6]
        result['dislike'] = row[7]
        return result

    def getUserMessages(self):
        result = UserDAO().getUserMessages()
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserMessageDict(r))

            return jsonify(User=mapped_result)

    def insertCredentialsJSON(self,json):
        cid = json.get('cid')

        ufirst_name = json.get('ufirst_name')

        ulast_name = json.get('ulast_name');

        udescription = json.get('udescription');

        phone = json.get('uphone');

        if ufirst_name and ulast_name and udescription and phone:
            uid = UserDAO().insert(cid,ufirst_name,ulast_name,phone,udescription)
            mapped_result = self.buildUserDict(uid,cid,ufirst_name,ulast_name,phone,udescription)
            return jsonify(User = mapped_result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 404

