class msgsPerDayHandler:

    def mapToDict(self, row):
        result = {}
        result['User msg per day'] = row[0]
        return result


    def getAllMedia(self):
        dao = mediaDAO()
        result = dao.getAllMedia()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(User=mapped_result)

