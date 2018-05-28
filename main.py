#############################################
# Authors:                                  #
#   Yomaira Rivera Albarran                 #
#   Gustavo Hernandez Ortiz                 #
#   Abdias Santiago Lugo                    #
#                                           #
# Date: 3/28/2018                           #
# Updated: 5/1/2018                         #
# Distribution: phyton 3.6                  #
#                                           #
# This project P1 implements an application #
# used for messaging in a social context.   #
#############################################
from flask_cors import CORS, cross_origin
from flask import Flask, request
from handler.adminsHandler import AdminHandler
from handler.contactsHandler import ContactsHandler
from handler.credentialsHandler import CredentialsHandler
from handler.groupHandler import GroupHandler
from handler.isPartHandler import IsPartHandler
from handler.mediaHandler import MediaHandler
from handler.messagesHandler import MessagesHandler
from handler.participateInHandler import ParticipationHandler
from handler.reactionsHandler import ReactionHandler
from handler.replyHandler import ReplyHandler
from handler.usersHandler import UsersHandler
from handler.receivedMsgsHandler import ReceivedMsgHandler

app = Flask(__name__)

# Apply CORS to this app
CORS(app)


@app.route('/')
def home():
    return "Welcome to Social Messaging App"

@app.route('/login')
def login():
    return "No Login for you!!!"

@app.route('/MessagingAppP1/UserMessages')
def getUsersMessages():
   if request.args:
       return UsersHandler.getUserMessages(request.args)
   else:
       return UsersHandler().getUserMessages()

##################
#      USER      #
# ################

##SEARCH ALL USERS
@app.route('/MessagingAppP1/user')
def getAllUsers():
    if request.args:
        return UsersHandler.getAllUsers(request.args)
    else:
        handler = UsersHandler()
        return handler.getAllUsers()

#SEARCHING A USER BY ATRIBUTE
@app.route('/MessagingAppP1/user/<int:uid>')
def getUserById(uid):
    return UsersHandler().getUserById(uid)

@app.route('/MessagingAppP1/user/name/<string:name>')
def getUserByName(name):
    return UsersHandler().getUserByName(name)

@app.route('/MessagingAppP1/user/lastname/<string:lastname>')
def getUserByLastname(lastname):
    return UsersHandler().getUserByLastname(lastname)

@app.route('/MessagingAppP1/user/phone/<string:phone>')
def getUserByPhone(phone):
    return UsersHandler().getUserByPhone(phone)
@app.route('/MessagingAppP1/user/description/<string:udescription>')
def getUserByDescription(udescription):
    return UsersHandler().getUserByDescription(udescription)


#USER REACTIONS
@app.route('/MessagingAppP1/user/<int:uid>/reactions')
def getReactionByUserId(uid):
   return ReactionHandler().getByUserId(uid)

#USER CREDENTIALS

@app.route('/MessagingAppP1/user/username/<string:username>/credentials')
def getCredentialsByUsername(username):
    return CredentialsHandler().getCredentialsByUsername(username)

@app.route('/MessagingAppP1/user/email/<string:email>/credentials')
def getCredentialsByEmail(email):
    return CredentialsHandler().getCredentialsByEmail(email)

#USER SENT MESSAGES
@app.route('/MessagingAppP1/user/<int:sid>/messages')
def getAllMessageBySenderId(sid):
    return MessagesHandler().getAllMessageBySenderId(sid)

#USER RECEIVED MESSAGES
@app.route('/MessagingAppP1/user/<int:uid>/ReceivedMsgs')
def getReceivedMsgByUserId(uid):
    return ReceivedMsgHandler().getReceivedMsgByUserId(uid)

#USER GROUPS
@app.route('/MessagingAppP1/user/<int:uid>/groups')
def getUserGroups(uid):
   return UsersHandler().getUserGroupsByUserId(uid)

#USER PERSONAL INFORMATION
@app.route('/MessagingAppP1/user/<int:uid>/info')
def getUserInfo(uid):
   return UsersHandler().getUserInformation(uid)


##################
#   CREDENTIALS  #
# ################

#GENERAL CREDENTIALS
@app.route('/MessagingAppP1/credentials')
def getAllCredentials():
    return CredentialsHandler().getAllCredentials()

@app.route('/MessagingAppP1/credentials/<int:cid>')
def getCredentialsById(cid):
    return CredentialsHandler().getCredentialsById(cid)

#For sake of testing     ###########################################
@app.route('/MessagingAppP1/credentials/cpass/<string:cpassword>') #
def getCredentialsByPassword(cpassword):                           #
    return CredentialsHandler().getCredentialsByPassword(cpassword)#
                                                                   #
@app.route('/MessagingAppP1/credentials/cemail/<string:cemail>')   #
def getCredentialsByEmai(cemail):                                  #
    return CredentialsHandler().getCredentialsByEmail(cemail)      #
####################################################################


##################
#   MESSAGES     #
# ################

#SEARCHING BY MESSAGE ATTRIBUTE
@app.route('/MessagingAppP1/messages')
def getAllMessages():
    if request.args:
        return MessagesHandler.getAllMessages(request.args)
    else:
        handler = MessagesHandler()
        return handler.getAllMessages()

@app.route('/MessagingAppP1/messages/<int:mid>')
def getMessageById(mid):
    return MessagesHandler().getMessageById(mid)

@app.route('/MessagingAppP1/messages/date/<string:mdate>')
def getMessageByDate(mdate):
    return MessagesHandler().getMessageByDate(mdate)

#@app.route('/MessagingAppP1/messages/time/<string:mtime>')
#def getMessageByTime(mtime):
#    return MessagesHandler().getMessageByTime(mtime)

@app.route('/MessagingAppP1/messages/contains/<string:minfo>')
def getMessageByInfo(minfo):
    return MessagesHandler().getMessageByInfo(minfo)

#MESSAGE REACTIONS ******
@app.route('/MessagingAppP1/message/<int:mid>/reactions')
def getReactionByMessageId(mid):
   return ReactionHandler().getByMessageId(mid)

#PEOPLE WHO RATED A MESSAGE
@app.route('/MessagingAppP1/message/<int:mid>/users/')
def getPeopleWhoRatedMessageList(mid):
    return ReactionHandler().getPeopleWhoRatedMessageList(mid)

#A MESSAGE LIKES ***
@app.route('/MessagingAppP1/message/<int:mid>/likes/')
def getLikesByMessageId(mid):
    return ReactionHandler().getLikesByMessageId(mid)

#PEOPLE WHO LIKE A MESSAGE
@app.route('/MessagingAppP1/message/<int:mid>/wholikes')
def getMessageLikesPeopleList(mid):
   return ReactionHandler().getMessageLikesPeopleList(mid)

#A MESSAGE DISLIKES
@app.route('/MessagingAppP1/message/<int:mid>/dislikes/')
def getDislikesByMessageId(mid):
   return ReactionHandler().getDislikesByMessageId(mid)

#PEOPLE WHO DISLIKE A MESSAGE
@app.route('/MessagingAppP1/message/<int:mid>/whodislikes')
def getMessageDislikesPeopleList(mid):
   return ReactionHandler().getMessageDislikesPeopleList(mid)

#MESSAGE MEDIA
@app.route('/MessagingAppP1/message/<int:mid>/media')
def getMediaByMessageId(mid):
   return MediaHandler().getByMessageId(mid)

#MESSAGE REPLY
@app.route('/MessagingAppP1/message/<int:mid>/MessageReply')
def getReplyByMessageId(mid):
    return ReplyHandler().getReplyByMessageId(mid)

#MESSAGE WHICH WAS REPLY
@app.route('/MessagingAppP1/MessageReply/replymessage/<int:rid>')
def getReplayByReplyToId(rid): #Search by reply message id
    return ReplyHandler().getReplyByReplyToId(rid)


#MESSAGES FROM CHAT OF 2 USERS
@app.route('/MessagingAppP1/message/conversation/<int:uid1>/<int:uid2>')
def getConversation(uid1,uid2):
    return MessagesHandler().getConversation(uid1,uid2)

################
#     GROUPS   #
################

#ALL GROUPS
@app.route('/MessagingAppP1/groups')
def getAllGroups():
   if request.args:
       return GroupHandler.getAllGroups(request.args)
   else:
       handler = GroupHandler()
       return handler.getAllGroups()

#SEARCHING BY GROUP ATTRIBUTE
@app.route('/MessagingAppP1/groups/<int:gid>')
def getGroupsById(gid):
   return GroupHandler().getGroupsById(gid)

@app.route('/MessagingAppP1/groups/gname/<string:gname>')
def getGroupsByName(gname):
   return GroupHandler().getGroupsByName(gname)

@app.route('/MessagingAppP1/groups/gdesc/<string:gdesc>')
def getGroupsByDescription(gdesc):
   return GroupHandler().getGroupByDescription(gdesc)

@app.route('/MessagingAppP1/groups/gcreation/<string:gcreation>')
def getGroupByCreation(gcreation):
   return GroupHandler().getGroupByCreation(gcreation)

#GROUP PARTICIPANTS IDS
@app.route('/MessagingAppP1/group/<int:gid>/GroupParticipants')
def getPinByGroupId(gid):
    return ParticipationHandler().getParticipantsByGroupId(gid)

#GROUP PARTICIPANTS NAMES
@app.route('/MessagingAppP1/group/<int:gid>/Participants')
def getPinNamesByGroupId(gid):
    return ParticipationHandler().getParticipantsNameByGroupId(gid)

#GROUP ADMIN
@app.route('/MessagingAppP1/group/<int:gid>/Admin')
def getAdminByGroupId(gid):
    return AdminHandler().getAdminByGroupId(gid)

#GROUP MESSAGES
@app.route('/MessagingAppP1/group/<int:gid>/messages')
def getMessagesByGroupId(gid):
    return GroupHandler().getMessagesByGroupId(gid)

######################
#     Reaction       #
######################
#ALL REACTIONS
@app.route('/MessagingAppP1/reactions')
def getAllReactions():
   if request.args:
       return ReactionHandler.getAllReactions(request.args)
   else:
       handler = ReactionHandler()
       return handler.getAllReactions()

#SEARCH REACTION BY ATTRIBUTE
#Posible Removal
@app.route('/MessagingAppP1/reactions/<int:rid>')
def getAllReactionsById(rid):
   return ReactionHandler().getAllReactionsById(rid)

@app.route('/MessagingAppP1/reactions/rating/<string:rating>')
def getLikesDislikes(rating):
   return ReactionHandler().getByLikesDislikes(rating)


########################
#  Group Participation #
# ######################
@app.route('/MessagingAppP1/GroupParticipants')
def getAllPinRelation():
    handler = ParticipationHandler()
    return handler.getAllParticipants()

@app.route('/MessagingAppP1/GroupParticipants/<int:pid>')
def getPinById(pid):
    return ParticipationHandler().getParticipantsByPId(pid)


##################
#  Administrator #
# ################
@app.route('/MessagingAppP1/Admins')
def getAllAdmin():
    return AdminHandler().getAllAdmin()

#Posible Removal
@app.route('/MessagingAppP1/Admin/<int:aid>')
def getAdminById(aid):
    return AdminHandler().getAdminById(aid)

@app.route('/MessagingAppP1/Admin/user/<int:uid>')
def getAdminByUserId(uid):
    return AdminHandler().getAdminByUserId(uid)


##################
#  Received Msg  #
# ################
@app.route('/MessagingAppP1/ReceivedMsgs')
def getAllReceivedMessages():
    return ReceivedMsgHandler().getAllReceivedMsg()

#Posible Removal
@app.route('/MessagingAppP1/ReceivedMsgs/<int:id>')
def getReceivedById(id):
    return ReceivedMsgHandler().getReceivedMsgById(id)

@app.route('/MessagingAppP1/ReceivedMsgs/message/<int:mid>')
def getReceivedMsgByMessageId(mid):
    return ReceivedMsgHandler().getReceivedMsgByMessageId(mid)


##################
#    Is Part     #
# ################

@app.route('/MessagingAppP1/PartOfGroup')
def getAllIsPart():
    return IsPartHandler().getAllIsPart()
#Posible Removal
@app.route('/MessagingAppP1/PartOfGroup/<int:pid>')
def getIsPartById(pid):
    return IsPartHandler().getIsPartById(pid)

@app.route('/MessagingAppP1/PartOfGroup/message/<int:mid>')
def getIsPartByMessageId(mid):
    return IsPartHandler().getIsPartByMessageId(mid)

@app.route('/MessagingAppP1/PartOfGroup/group/<int:gid>')
def getIsPartByGroupId(gid):
    return IsPartHandler().getIsPartByGroupId(gid)



##################
#       Reply    #
# ################

#ALL MESSAGES REPLIES
@app.route('/MessagingAppP1/MessageReply')
def getAllReply():
    return ReplyHandler().getAllReply()

@app.route('/MessagingAppP1/MessageReply/rid/<int:pid>')
def getReplyById(pid):
    return ReplyHandler().getReplyById(pid)


###################
# TEST FOR MEDIA  #
###################

@app.route('/MessagingAppP1/media')
def getAllMedia():
   if request.args:
       return MediaHandler.getAllMedia(request.args)
   else:
       handler = MediaHandler()
       return handler.getAllMedia()

@app.route('/MessagingAppP1/media/<int:meid>')
def getAllMediaById(meid):
   return MediaHandler().getAllMediaById(meid)

@app.route('/MessagingAppP1/media/name/<string:mename>')
def getMediaByName(mename):
   return MediaHandler().getMediaByName(mename)

@app.route('/MessagingAppP1/media/address/<string:meaddress>')
def getMediaByAddress(meaddress):
   return MediaHandler().getMediaByAddress(meaddress)


@app.route('/MessagingAppP1/media/type/<string:metype>')
def getMediaByType(metype):
   return MediaHandler().getMediaByType(metype)


###################
#     CONTACTS    #
###################
#All user contacts
@app.route('/MessagingAppP1/user/<int:uid>/contacts')
def getUserContacts(uid):
   return ContactsHandler().getUserContacts(uid)

#A user's contact info
@app.route('/MessagingAppP1/user/<int:uid>/contact/<int:cid>')
def getUserContactById(uid, cid):
   return ContactsHandler().getUserContactsById(uid, cid)

if __name__ == '__main__':
    app.run()
