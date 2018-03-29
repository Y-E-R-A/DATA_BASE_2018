from flask import jsonify, request
from dao.reaction import ReactionDAO

class ReactionHandler:
    def mapToDict(self, row):
        result = {}
        result['rid'] = row[0]
        result['mid'] = row[1]
        result['uid'] = row[2]
        result['rating'] = row[3]

        return result


    def getAllReactions(self):
        dao = ReactionDAO()
        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)


    def getAllReactionsById(self, rid):
        dao = ReactionDAO()
        result = dao.getByReactionId(rid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getByMessageId(self, mid):
        dao = ReactionDAO()
        result = dao.getByMessageID(mid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getByUserId(self, uid):
        dao = ReactionDAO()
        result = dao.getByUserId(uid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)

    def getByLikesDislikes(self, rating):
        dao = ReactionDAO()
        result = dao.getByLikeDislike(rating)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(User=mapped_result)


