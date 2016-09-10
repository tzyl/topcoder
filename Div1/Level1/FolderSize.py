class FolderSize(object):
    def calculateWaste(self, files, folderCount, clusterSize):
        waste = [0] * folderCount
        for file in files:
            folder, size = map(int, file.split())
            if size % clusterSize:
                waste[folder] += clusterSize - (size % clusterSize)
        return waste

print FolderSize().calculateWaste(["0 93842", "1 493784", "2 43212", "3 99327", "4 456209", "5 947243", "6 59348", "7 58237", "8 5834", "9 492384", "0 58342", "3 538432", "6 1432", "9 453983", "2 4321", "4 583729", "6 6974", "8 9864", "4 43211", "8 38437"], 10, 22485)
