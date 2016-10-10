from collections import defaultdict


class PermissionTree(object):
    def findHome(self, folders, users):
        # folder_tree will hold Folder objects which point to the parent folder
        # and which users have access to that folder.
        folder_tree = [Folder(i) for i in xrange(len(folders))]
        # user_folders contains users as keys and a list of which folders that
        # user has access to as its value.
        user_folders = defaultdict(list)
        # Initialize the Folder object fields and the lists of which folders
        # each user can access.
        for i, folder in enumerate(folders):
            folder = folder.split()
            p_idx, allowed_users = int(folder[0]), folder[1].split(",")
            folder_tree[i].parent = folder_tree[p_idx]
            folder_tree[i].users = allowed_users
            for user in allowed_users:
                user_folders[user].append(folder_tree[i])
        # Now go through the users and calculate their home folder.
        home_folders = []
        for user in users:
            if not user_folders[user]:
                # This user has no access to any folders.
                home_folders.append(-1)
            else:
                home_folder = user_folders[user][0]
                for f in user_folders[user][1:]:
                    home_folder = lowest_common_ancestor(home_folder, f)
                home_folders.append(home_folder.index)
        return home_folders


class Folder(object):
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.users = []


def lowest_common_ancestor(f1, f2):
    # First traverse up from f1 to root.
    seen = set()
    while f1 not in seen:
        seen.add(f1)
        f1 = f1.parent
    # Now traverse up from f2 to root and return the first common ancestor.
    while f2 not in seen and f2.parent is not f2:
        f2 = f2.parent
    return f2 if f2 in seen else None
