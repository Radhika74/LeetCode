from sortedcontainers import SortedList

class TaskManager(object):
    def __init__(self,tasks):
        self.st=SortedList()
        self.mp={}
        for uId,tId,p in tasks:
            self.st.add((p,tId,uId))
            self.mp[tId]=(uId,p)

    def add(self,userId,taskId,priority):
        self.st.add((priority,taskId,userId))
        self.mp[taskId]=(userId,priority)

    def edit(self,taskId,newPriority):
        u,p=self.mp[taskId]
        self.st.remove((p,taskId,u))
        self.st.add((newPriority,taskId,u))
        self.mp[taskId]=(u,newPriority)

    def rmv(self,taskId):
        u,p=self.mp[taskId]
        self.st.remove((p,taskId,u))
        del self.mp[taskId]

    def execTop(self):
        if not self.st:return -1
        p,t,u=self.st[-1]
        self.st.pop()
        del self.mp[t]
        return u