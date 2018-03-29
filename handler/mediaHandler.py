from flask import jsonify, request
from dao.media import mediaDAO

class MediaHandler:
    def mapToDict(self, row):
        result = {}
        result['meid'] = row[0]
        result['mename'] = row[1]
        result['meaddress'] = row[2]
        result['metype'] = row[3]
        result['mid'] = row[4]

        return result


    def getAllMedia(self):
        dao = mediaDAO()
        result = dao.getAllMedia()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)


    def getAllMediaById(self, meid):
        dao = mediaDAO()
        result = dao.getMediaByID(meid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getMediaByName(self, mename):
        dao = mediaDAO()
        result = dao.getMediaByName(mename)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getMediaByAddress(self, meaddress):
        dao = mediaDAO()
        result = dao.getMediaByAddress(meaddress)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getMediaByType(self, metype):
        dao = mediaDAO()
        result = dao.getMediaByType(metype)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getByMessageId(self, mid):
        dao = mediaDAO()
        result = dao.getByMessageId(mid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)


