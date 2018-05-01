from flask import jsonify, request
from dao.contactsDAO import ContactsDAO

class ContactsHandler:

    #User dictionary
    def mapContactsToDict(self, row):
        result = {}
        result['uid'] = row[0]
        result['contactid'] = row[1]
        result['contact_firstname'] = row[2]
        result['contact_lastname'] = row[3]
        result['contact_email'] = row[4]
        result['contact_phone'] = row[5]
        return result

    def getUserContacts(self, uid):
        dao = ContactsDAO()
        result = dao.getUserContacts(uid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapContactsToDict(r))
        return jsonify(ContactsBook =mapped_result)

    def getUserContactsById(self, uid, cid):
        dao = ContactsDAO()
        result = dao.getUserContactByID(uid, cid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapContactsToDict(r))
        return jsonify(ContactsBook =mapped_result)