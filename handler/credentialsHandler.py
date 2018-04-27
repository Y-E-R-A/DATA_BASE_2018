from flask import jsonify, request
from dao.credential import CredentialsDAO

class CredentialsHandler:

    #Credentials dictionary
    def mapToUserDict(self, row):
        result = {}
        result['cid'] = row[0]
        result['uid'] = row[1]
        result['username'] = row[2]
        result['email'] = row[3]
        result['password'] = row[4]
        return result

    def getAllCredentials(self):
        result = CredentialsDAO().getAllCredentials()
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserDict(r))

            return jsonify(User=mapped_result)


    def getCredentialsById(self, cid):
        result = CredentialsDAO().getCredentialsById(cid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                 mapped_result.append(self.mapToUserDict(r))

            return jsonify(User= mapped_result)

    def getCredentialsByUserId(self, uid):
        result = CredentialsDAO().getCredentialsByUserId(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                 mapped_result.append(self.mapToUserDict(r))

            return jsonify(User= mapped_result)
    def getCredentialsByUsername(self, username):
        result = CredentialsDAO().getCredentialsByUsername(username)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(User=mapped_result)

    def getCredentialsByEmail(self, email):
        # The first user with 'email' will be the mapped result
        result = CredentialsDAO().getCredentialsByEmail(email)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapToUserDict(result)
            return jsonify(User= mapped_result)
