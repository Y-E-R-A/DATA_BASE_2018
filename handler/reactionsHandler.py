from flask import jsonify, request
from dao.reactionDAO import ReactionDAO

class ReactionHandler:
    def mapToDict(self, row):
        result = {}
        #result['rid'] = row[0]
        result['mid'] = row[0]
        result['uid'] = row[1]
        result['rating'] = row[2]

        return result
    def mapToMessageReactionDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['minfo'] = row[1]
        result['reaction count'] = row[2]
        return result

    def mapMessageReactionToPeopleDict(self, row):
        result = {}
        result['mid'] = row[0]
        result['minfo'] = row[1]
        result['userid'] = row[2]
        return result

    def getAllReactions(self):
        dao = ReactionDAO()
        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Reaction=mapped_result)


    def getAllReactionsById(self, rid):
        dao = ReactionDAO()
        result = dao.getByReactionId(rid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)

    def getLikesByMessageId(self, mid):
        result = ReactionDAO().getLikesOfMessageById(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMessageReactionDict(r))
            return jsonify(Reaction=mapped_result)

    def getMessageLikesPeopleList(self, mid):
        result = ReactionDAO().getPeopleWhoLikesMessageId(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapMessageReactionToPeopleDict(r))
            return jsonify(Reaction=mapped_result)

    def getDislikesByMessageId(self, mid):
        result = ReactionDAO().getDislikesByMessageId(mid)
        print(result)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMessageReactionDict(r))
            return jsonify(Reaction=mapped_result)

    def getMessageDislikesPeopleList(self, mid):
        result = ReactionDAO().getPeopleWhoDislikesMessageId(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapMessageReactionToPeopleDict(r))
            return jsonify(Reaction=mapped_result)

    def getByMessageId(self, mid):
        dao = ReactionDAO()
        result = dao.getByMessageID(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)

    def getByUserId(self, uid):
        dao = ReactionDAO()
        result = dao.getByUserId(uid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)

    def getByLikesDislikes(self, rating):
        dao = ReactionDAO()
        result = dao.getByLikeDislike(rating)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)




