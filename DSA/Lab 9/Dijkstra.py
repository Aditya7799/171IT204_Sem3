class BinHeap:
    def __init__(self):
        self.L = [0]
        self.Size = 0


    def heapifyUp(self,i):
        while i // 2 > 0:
          if self.L[i] < self.L[i // 2]:
             tmp = self.L[i // 2]
             self.L[i // 2] = self.L[i]
             self.L[i] = tmp
          i = i // 2

    def insert(self,k):
      self.L.append(k)      
      self.Size = self.Size + 1
      self.heapifyUp(self.Size)

    def heapifyDown(self,i):
      while (i * 2) <= self.Size:
          mc = self.minChild(i)
          if self.L[i] < self.L[mc]:
              tmp = self.L[i]
              self.L[i] = self.L[mc]
              self.L[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.Size:
          return i * 2
      else:
          if self.L[i*2] < self.L[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def extractMin(self):
      retval = self.L[1]
      self.L[1] = self.L[self.Size]
      self.Size = self.Size - 1
      self.L.pop()
      self.heapifyDown(1)
      return retval



    def update(self,node):
      for i in range(1,self.Size+1):
        if(i==node):
          break
      self.heapifyUp(i)







    

class Node:
    def __init__(self,value=None,next=None,weight=None):
        self.value=value 
        self.next=next
        self.weight=weight
        self.parent=None
        self.dist=10000000
        #dist=distance from source
        #weight=Edge weight


    def __lt__(self,other):
            if(self.dist<other.dist):
                return True
            else:
                return False
            




class Graph:
    def __init__(self,nodes=None):
        self.nodes=nodes
        self.adlist=[None]*nodes
        
        

    def insert(self,a,b,w):
        temp=self.adlist[a]
        self.adlist[a]=Node(b,temp,w)

    def setDist(self,value,dist):
        for i in self.adlist:
            curr=i
            while(curr!=None):
                if(curr.value==value):
                    curr.dist=dist
                    
                curr=curr.next
                
    def setParent(self,value,parent):
        for i in self.adlist:
            curr=i
            while(curr!=None):
                if(curr.value==value):
                    curr.parent=parent
                    
                curr=curr.next
    def getNode(self,value):
            for i in self.adlist:
                curr=i
                while(curr!=None):
                    if(curr.value==value):
                        return curr
                    curr=curr.next
            
    
    

    def Dijk(self,source):
            H=BinHeap()
            self.setParent(source,None)
            self.setDist(source,0)
                     

            for i in range(self.nodes):
                H.insert(self.getNode(i))




            while(H.Size!=0):
                w=H.extractMin()
                curr=self.adlist[w.value]
                while(curr!=None):
                  if(curr.dist>w.dist+curr.weight):
                    self.setDist(curr.value,w.dist+curr.weight)
                    H.update(curr)
                    self.setParent(curr.value,w.value)
                  curr=curr.next

    def printdist(self):
      visited=[]
      for i in self.adlist:
        curr=i
        while(curr!=None):
          if(not(curr.value in visited)):
            print("For Node:",curr.value,":Distance=",curr.dist)
            print("Path followed=")
            self.path(curr)
            visited.append(curr.value)
          curr=curr.next




    def path(self,node):
      string=""
      while(node!=None):
        string=string+str(node.value)+" "
        node=self.getNode(node.parent)

      
      print(string)



def main():
    
    nodes=int(input("Enter the number of nodes"))
    g=Graph(nodes)
    print("Enter the edges,-1 to break")
    while(True):
        a=int(input("Enter the source     "))
        b=int(input("Enter the destination"))
        r=int(input("Enter the weight     "))
        if(a!=-1 and b !=-1 ):
            g.insert(a,b,r)
            g.insert(b,a,r)
        else:
            break

    g.Dijk(0)
    g.printdist()



    
    
    



main()

    
    







        
        
