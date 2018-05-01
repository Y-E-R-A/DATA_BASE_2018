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
            pname = form['pname']
            pprice = form['pprice']
            pmaterial = form['pmaterial']
            pcolor = form['pcolor']
            if pcolor and pprice and pmaterial and pname:
                dao = PartsDAO()
                pid = dao.insert(pname, pcolor, pmaterial, pprice)
                result = self.build_part_attributes(pid, pname, pcolor, pmaterial, pprice)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400