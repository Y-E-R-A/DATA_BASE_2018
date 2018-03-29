from flask import Flask, request
from handler.admins import AdminHandler
from handler.credentials import CredentialsHandler
from handler.groups import GroupHandler
from handler.isPartHandler import IsPartHandler
from handler.messages import MessagesHandler
from handler.participateInHandler import PinHandler
from handler.reactions import ReactionHandler
from handler.replyHandler import ReplyHandler
from handler.users import UsersHandler
from handler.receivedMsgs import ReceivedMsgHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Social Messaging App"

@app.route('/login')
def login():
    return "No Login for you!!!"



##################
#      USER      #
# ################

@app.route('/MessagingAppP1/user')
def getAllUsers():
    if request.args:
        return UsersHandler.getAllUsers(request.args)
    else:
        handler = UsersHandler()
        return handler.getAllUsers()
@app.route('/MessagingAppP1/user/id=<int:uid>')
def getUserById(uid):
    return UsersHandler().getUserById(uid)

@app.route('/MessagingAppP1/user/name=<string:name>')
def getUserByName(name):
    return UsersHandler().getUserByName(name)

@app.route('/MessagingAppP1/user/lastname=<string:lastname>')
def getUserByLastname(lastname):
    return UsersHandler().getUserByLastname(lastname)

@app.route('/MessagingAppP1/user/phone=<string:phone>')
def getUserByPhone(phone):
    return UsersHandler().getUserByPhone(phone)



##################
#   CREDENTIALS  #
# ################

@app.route('/MessagingAppP1/credentials')
def getAllCredentials():
    return CredentialsHandler().getAllCredentials()

@app.route('/MessagingAppP1/credentials/username=<string:username>')
def getCredentialsByUsername(username):
    return CredentialsHandler().getCredentialsByUsername(username)

@app.route('/MessagingAppP1/credentials/email=<string:email>')
def getCredentialsByEmail(email):
    return CredentialsHandler().getCredentialsByEmail(email)

@app.route('/MessagingAppP1/credentials/cid=<int:cid>')
def getCredentialsById(cid):
    return CredentialsHandler().getCredentialsById(cid)

@app.route('/MessagingAppP1/credentials/uid=<int:uid>')
def getCredentialsByUserId(uid):
    return CredentialsHandler().getCredentialsByUserId(uid)


##################
#   MESSAGES     #
# ################

@app.route('/MessagingAppP1/messages')
def getAllMessages():
    if request.args:
        return MessagesHandler.getAllMessages(request.args)
    else:
        handler = MessagesHandler()
        return handler.getAllMessages()

@app.route('/MessagingAppP1/messages/mid=<int:mid>')
def getMessageById(mid):
    return MessagesHandler().getMessageById(mid)

@app.route('/MessagingAppP1/messages/sid=<int:sid>')
def getAllMessageBySenderId(sid):
    return MessagesHandler().getAllMessageBySenderId(sid)

@app.route('/MessagingAppP1/messages/date=<string:date>')
def getMessageByDate(date):
    return MessagesHandler().getMessageByDate(date)

@app.route('/MessagingAppP1/messages/time=<string:time>')
def getMessageByTime(time):
    return MessagesHandler().getMessageByTime(time)

@app.route('/MessagingAppP1/messages/body=<string:body>')
def getMessageByBody(body):
    return MessagesHandler().getMessageByBody(body)




################
#TEST FOR GROUP#
################

@app.route('/MessagingAppP1/group')
def getAllGroups():
   if request.args:
       return GroupHandler.getAllGroups(request.args)
   else:
       handler = GroupHandler()
       return handler.getAllGroups()

@app.route('/MessagingAppP1/group/gid=<int:gid>')
def getGroupsById(gid):
   return GroupHandler().getGroupsById(gid)

@app.route('/MessagingAppP1/group/gname=<string:gname>')
def getGroupsByName(gname):
   return GroupHandler().getGroupsByName(gname)

@app.route('/MessagingAppP1/group/gdesc=<string:gdesc>')
def getGroupsByDescription(gdesc):
   return GroupHandler().getGroupByDescription(gdesc)

@app.route('/MessagingAppP1/group/gusername=<string:gusername>')
def getGroupByCreation(gcreation):
   return GroupHandler().getGroupByCreation(gcreation)

@app.route('/MessagingAppP1/group/uid=<int:uid>')
def getByUserId(uid):
   return GroupHandler().getByUserId(uid)


######################
#  TEST FOR Reaction #
######################
@app.route('/MessagingAppP1/reactions')
def getAllReactions():
   if request.args:
       return ReactionHandler.getAllReactions(request.args)
   else:
       handler = ReactionHandler()
       return handler.getAllReactions()

@app.route('/MessagingAppP1/reactions/rid=<int:rid>')
def getAllReactionsById(rid):
   return ReactionHandler().getAllReactionsById(rid)

@app.route('/MessagingAppP1/reactions/mid=<int:mid>')
def getByMessageId(mid):
   return ReactionHandler().getByMessageId(mid)

@app.route('/MessagingAppP1/reactions/uid=<int:uid>')
def getBySMUserId(uid):
   return ReactionHandler().getByUserId(uid)

@app.route('/MessagingAppP1/reactions/rating=<string:rating>')
def getLikesDislikes(rating):
   return ReactionHandler().getByLikesDislikes(rating)


##################
#  Participation #
# ################
@app.route('/MessagingAppP1/PinRelation')
def getAllPinRelation():
    handler = PinHandler()
    return handler.getAllPin()

@app.route('/MessagingAppP1/PinRelation/id=<int:pid>')
def getPinById(pid):
    return PinHandler().getPinById(pid)

@app.route('/MessagingAppP1/PinRelation/uid=<int:uid>')
def getPinByUserId(uid):
    return PinHandler().getPinByUserId(uid)

@app.route('/MessagingAppP1/PinRelation/gid=<int:gid>')
def getPinByGroupId(gid):
    return PinHandler().getPinByGroupId(gid)


##################
#  Administrator #
# ################
@app.route('/MessagingAppP1/Admin')
def getAllAdmin():
    return AdminHandler().getAllAdmin()

@app.route('/MessagingAppP1/Admin/id=<int:pid>')
def getAdminById(pid):
    return AdminHandler().getAdminById(pid)

@app.route('/MessagingAppP1/Admin/uid=<int:uid>')
def getAdminByUserId(uid):
    return AdminHandler().getAdminByUserId(uid)

@app.route('/MessagingAppP1/Admin/gid=<int:gid>')
def getAdminByGroupId(gid):
    return AdminHandler().getAdminByGroupId(gid)



##################
#  Received Msg  #
# ################
@app.route('/MessagingAppP1/ReceivedMsg')
def getAllReceivedMessages():
    return ReceivedMsgHandler().getAllReceivedMsg()

@app.route('/MessagingAppP1/ReceivedMsg/id=<int:id>')
def getReceivedById(id):
    return ReceivedMsgHandler().getReceivedMsgById(id)

@app.route('/MessagingAppP1/ReceivedMsg/uid=<int:uid>')
def getReceivedMsgByUserId(uid):
    return ReceivedMsgHandler().getReceivedMsgByUserId(uid)

@app.route('/MessagingAppP1/ReceivedMsg/mid=<int:mid>')
def getReceivedMsgByMessageId(mid):
    return ReceivedMsgHandler().getReceivedMsgByMessageId(mid)


##################
#    Is Part     #
# ################

@app.route('/MessagingAppP1/PartOfGroup')
def getAllIsPart():
    return IsPartHandler().getAllIsPart()

@app.route('/MessagingAppP1/PartOfGroup/id=<int:pid>')
def getIsPartById(pid):
    return IsPartHandler().getIsPartById(pid)

@app.route('/MessagingAppP1/PartOfGroup/mid=<int:mid>')
def getIsPartByMessageId(mid):
    return IsPartHandler().getIsPartByMessageId(mid)

@app.route('/MessagingAppP1/PartOfGroup/gid=<int:gid>')
def getIsPartByGroupId(gid):
    return IsPartHandler().getIsPartByGroupId(gid)



##################
#    Is Part     #
# ################

@app.route('/MessagingAppP1/Reply')
def getAllReply():
    return ReplyHandler().getAllReply()

@app.route('/MessagingAppP1/Reply/id=<int:pid>')
def getReplyById(pid):
    return ReplyHandler().getReplyById(pid)

@app.route('/MessagingAppP1/Reply/mid=<int:mid>')
def getReplyByMessageId(mid):
    return ReplyHandler().getReplyByMessageId(mid)

@app.route('/MessagingAppP1/Reply/rid=<int:rid>')
def getReplayByGroupId(rid):
    return ReplyHandler().getReplyByReplyToId(rid)





if __name__ == '__main__':
    app.run()
