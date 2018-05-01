from flask import jsonify, request
from dao.credentialDAO import CredentialsDAO

class CredentialsHandler:

    #Credentials dictionary
    def mapToUserDict(self, row):
        result = {}
        result['cid'] = row[0]
        result['password'] = row[1]
        result['username'] = row[2]
        result['email'] = row[3]
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

    def getCredentialsByPassword(self, cpassword):
        result = CredentialsDAO().getCredentialsByPassword(cpassword)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                 mapped_result.append(self.mapToUserDict(r))

            return jsonify(User= mapped_result)
    #Does not exist in Credentials
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

    def getCredentialsByEmail(self, cemail):
        result = CredentialsDAO().getCredentialsByEmail(cemail)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(User=mapped_result)
