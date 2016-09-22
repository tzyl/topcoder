class Library(object):
    def documentAccess(self, records, userGroups, roomRights):
        documents = set()
        for record in records:
            document, room, group = record.split()
            if room in roomRights and group in userGroups:
                documents.add(document)
        return len(documents)
