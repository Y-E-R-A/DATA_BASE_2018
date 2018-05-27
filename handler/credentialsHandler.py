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

    def mapToDict(self, row):
        result = {}
        result['cid'] = row[0]
        result['password'] = row[1]
        result['username'] = row[2]
        result['email'] = row[3]
        result['uid'] = row[4]
        return result

    def buildUserDict(self, cid,cuser_name,cpassword,cemail):
        result = {}
        result['cid'] = cid
        result['password'] = cpassword
        result['username'] = cuser_name
        result['email'] = cemail
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

    def getUserByCredentials(self, args):
        print ("HANDLER")
        cuser = args.get("cuser")
        cpassword = args.get("cpassword")
        print (cuser)
        print(cpassword)
        #cuser = json['cuser']
        #cpassword = json['cpassword']
        if cuser and cpassword:
            result = CredentialsDAO().getUserByCredentials(cpassword,cuser)
            mapped_result = []
            if not result:
                return jsonify(Error="NOT FOUND"), 404
            else:
                for r in result:
                    mapped_result.append(self.mapToDict(r))
                return jsonify(User=mapped_result), 201
        else:
            return jsonify(Error = "Unexpected attributes in post request"), 404

    def insertCredentialsJSON(self,json):
        ufirst_name = json.get('ufirst_name')

        ulast_name = json.get('ulast_name');

        cuser_name = json.get('cuser_name');

        cpassword = json.get('cpassword');

        cemail = json.get('cemail');

        #cphone = json.get('cphone');

        #udescription = json.get('udescription');

        if cuser_name and cpassword and cemail:
            cid = CredentialsDAO().insert(cuser_name,cpassword,cemail)
            mapped_result = self.buildUserDict(cid,cuser_name,cpassword,cemail)
            return jsonify(User=mapped_result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 404