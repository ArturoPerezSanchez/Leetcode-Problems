# https://leetcode.com/problems/design-in-memory-file-system

class FileSystem:

    def __init__(self):
        self.d = {"/": set()}
        self.d2 = {}
        

    def ls(self, path: str) -> List[str]:
        if(path in self.d2): return [path.split("/")[-1]]
        if(path in self.d): return sorted(self.d[path])
        return []

    def mkdir(self, path: str) -> None:
        pathlist = path.split("/")
        currentdir = ""
        self.d["/"].add(pathlist[1])
        for i in range(1,len(pathlist) -1):
            currentdir+= "/" +  pathlist[i]
            if(currentdir not in self.d):
                self.d[currentdir] = set([pathlist[i+1]])
            else:
                self.d[currentdir].add(pathlist[i+1])
        
        currentdir += pathlist[-1]
        if(currentdir not in self.d):
            self.d[currentdir] = set()
        print(self.d)


    def addContentToFile(self, filePath: str, content: str) -> None:
        if(filePath in self.d2):
            self.d2[filePath] += content
        else:
            self.mkdir(filePath)
            self.d2[filePath] = content
        

    def readContentFromFile(self, filePath: str) -> str:
        return self.d2[filePath]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)