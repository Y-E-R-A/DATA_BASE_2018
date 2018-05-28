from flask import jsonify, request
from dao.messageDAO import messageDAO

class MessagesHandler:

    #User dictionary
    def mapToMsgDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['date'] = row[1]
        result['info'] = row[2]
        result['uid']= row[3]
        return result

    def build_messages_attributes(self, mid, mdate, minfo, uid):
        result = {}
        result['mid'] = mid
        result['mdate'] = mdate
        result['minfo'] = minfo
        result['uid'] = uid
        return result

    def buildMsgDict(self, mid, mdate, minfo, uid):
        result = {}
        result['mid'] = mid
        result['mdate'] = mdate
        result['minfo'] = minfo
        result['uid'] = uid
        return result

    def getAllMessages(self):
        result = messageDAO().getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))

        return jsonify(Messages=mapped_result)


    def getMessageById(self, mid):
        print (mid)
        result = messageDAO().getMessageById(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))

            return jsonify(Messages=mapped_result)

    def getAllMessageBySenderId(self, uid):

            result = messageDAO().getAllMessageByUserId(uid)
            mapped_result = []
            if not result:
                return jsonify(Error="NOT FOUND"), 404
            else:
                for r in result:
                    mapped_result.append(self.mapToMsgDict(r))

                return jsonify(Messages=mapped_result)

    def getMessageByDate(self, date):
        result = messageDAO().getMessageByDate(date)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))

            return jsonify(Messages=mapped_result)

    def getMessageByInfo(self, minfo):
        result = messageDAO().getMessageByInfo(minfo)
        mapped_result = []

        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))

            return jsonify(Messages=mapped_result)

    def insert(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            mdate = form['mdate']
            minfo = form['minfo']
            uid = form['uid']
            if mdate and minfo and uid:
                dao = messageDAO()
                mid = dao.insert(mdate, minfo, uid)
                result = self.build_messages_attributes(mid, mdate, minfo, uid)
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateMessages(self, uid, form):
        dao = messageDAO()
        if not dao.getAllMessageByUserId(uid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                mid = form['mid']
                mdate = form['mdate']
                minfo = form['minfo']
                uid = form['uid']
                if mid and mdate and minfo and uid:
                    dao.update(mid, mdate, minfo, uid)
                    result = self.build_messages_attributes(mid, mdate, minfo, uid)
                    return jsonify(Message=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
    def insertCredentialsJSON(self, json):

        uid = json.get('uid')

        mdate = json.get('mdate')

        minfo = json.get('minfo')

        if uid and mdate  and minfo:
            mid = messageDAO().insert(mdate,minfo,uid)
            mapped_result = self.buildMsgDict(mid,mdate,minfo,uid)
            return jsonify(User=mapped_result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 404


    def getConversation(self,uid1, uid2):
        result = messageDAO().getConversation(uid1,uid2)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))
            return jsonify(Messages=mapped_result)
