from flask import jsonify, request
from dao.reactionDAO import ReactionDAO

class ReactionHandler:
    def mapToDict(self, row):
        result = {}
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
        result['ufirstname'] = row[3]
        result['ulastname'] = row[4]
        result['rating'] = row[5]
        return result

    def mapToMessageReactionFromPeopleDict(self, row):
        result = {}
        result['firstname'] = row[0]
        result['lastname'] = row[1]
        result['rating'] = row[2]
        return result

    def build_Reaction_attributes(self, mid, uid, rating):
        result = {}
        result['mid'] = mid
        result['uid'] = uid
        result['rating'] = rating
        return result

    def buildToDict(self, mid,uid,rating):
        result = {}
        result['mid'] = mid
        result['uid'] = uid
        result['rating'] = rating
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

    def getPeopleWhoRatedMessageList(self, mid):
        result = ReactionDAO().getPeopleWhoRateMessage(mid)
        mapped_result = []
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        else:
            for r in result:
                mapped_result.append(self.mapToMessageReactionFromPeopleDict(r))
            return jsonify(Reaction=mapped_result)

    def getDislikesByMessageId(self, mid):
        result = ReactionDAO().getDislikesByMessageId(mid)
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
                mapped_result.append(self.mapMessageReactionToPeopleDict(r))
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

    def updateMessages(self, uid, form):
        dao = ReactionDAO()
        if not dao.getAllReactions(uid):
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

        mid = json.get('mid')

        uid = json.get('uid')

        rating = json.get('rating')
        print(mid)
        print(uid)
        print(rating)
        if uid and rating  and mid:
            ReactionDAO().insert(mid,uid,rating)
            mapped_result = self.buildToDict(mid,uid,rating)
            return jsonify(User=mapped_result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 404

