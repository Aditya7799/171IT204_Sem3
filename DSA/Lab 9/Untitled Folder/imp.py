def insert(T,k,v,d):
        if T[k]==None:
            T[k]=ListNode()
            T[k].value=k
            temp=ListNode()
            temp.value=v
            temp.dist=d
            T[k].next=temp
            
            
        else:
            if search(T,k,v)==0:
                temp=ListNode()
                temp.value=v
                temp.dist=d
                temp.next=T[k].next
                T[k].next=temp
                

def search(T,k,v):
    temp=T[k]
    while temp!=None:
        if temp.value==v:
            return 1
        temp=temp.next
    return 0
def ke(T,n):
    temp=ListNode()
    for i in range(0,n):
        if T[i]!=None and T[i].next!=None:
            temp=T[i].next
            print(T[i].value,":", end=' ')
        if T[i]==None:
            print(i,":",end=' ')
        while temp!=None:
            print(temp.value,end=' ')
            temp=temp.next
        print()


class ListNode():
    def __init__(self):
        self.value=None
        self.next=None
        self.prev=None
        self.color=None
        self.dist=None


class Heap:
    def __init__(self,n):
        self.arr=[0 for i in range(100)]
        self.leng=-1
        self.size=n
    def inserth(self,x):
        if self.leng==self.size:
            print("Full")
        else:
            self.arr[self.leng+1]=x
            self.leng=self.leng+1
            i=self.leng
            while i!=0:
                if i%2!=0:
                    if self.arr[i//2].dist>x.dist:
                        t=self.arr[i//2]
                        self.arr[i//2]=x
                        self.arr[i]=t
                    i=i//2          
                else:
                    if self.arr[(i//2)-1].dist>x.dist:
                        t=self.arr[(i//2)-1]
                        self.arr[(i//2)-1]=x
                        self.arr[i]=t
                    i=(i//2)-1
    
    def print(self):
        for i in range(self.leng+1):
            print(self.arr[i].value,end=" ")
        print()

    def getmin(self):
        return self.arr[0]
    def extractmin(self):
        #print("Self.len",self.leng)
        if self.leng==0:
            self.leng=self.leng-1
            return self.arr[0]

            #print("Already Empty")
            #exit()
        else:
            x=self.arr[0]
            self.arr[0],self.arr[self.leng]=self.arr[self.leng],self.arr[0]
            self.leng=self.leng-1
            #print(self.arr[0])
            self.heapify()
            return x

    def comc(self,i):
        if self.leng>1 and 2*i+2<=self.leng:
            if self.arr[i].dist>self.arr[2*i+1].dist or self.arr[i].dist>self.arr[2*i+2].dist:
                x=self.getm(self.arr[2*i+1].dist,self.arr[2*i+2].dist)
                if self.arr[2*i+1].dist==x:
                    self.arr[i],self.arr[2*i+1]=self.arr[2*i+1],self.arr[i]
                    self.comc(2*i+1)
                else:
                    self.arr[i],self.arr[2*i+2]=self.arr[2*i+2],self.arr[i]
                    self.comc(2*i+2)

    def printn(self):
        for i in range(self.size):
            print(self.arr[i],end =' ')
    def heapify(self):
        i=self.leng

        #print(self.arr[i],i)
        while i!=0:
            #self.comc(i)
            
            #print(i)   
            if i%2!=0:
            #   print("::",i)
                if self.arr[i//2].dist>=self.arr[i].dist:
                    t=self.arr[i//2]
                    self.arr[i//2]=self.arr[i]
                    self.arr[i]=t
                    #self.print()
                    self.comc(i)
                    #self.print()
                    #if i<=self.leng/2-1:
                        #print("HIHIHIH")
                        #self.comc(i)
                    if i==self.leng//2:
                        if self.arr[i].dist>self.arr[2*i+1].dist:
                            self.arr[2*i+1],self.arr[i]=self.arr[i],self.arr[2*i+1]
                i=i//2          
            else:
                if self.arr[i//2-1].dist>=self.arr[i].dist:
                    t=self.arr[(i//2)-1]
                    self.arr[(i//2)-1]=self.arr[i]
                    self.arr[i]=t
                    #self.print()
                    self.comc(i)
                    #if i<=self.leng/2-1:
                    #self.comc(i)
                    if i==self.leng//2:
                        if self.arr[i].dist>self.arr[2*i+1].dist:
                            self.arr[2*i+1],self.arr[i]=self.arr[i],self.arr[2*i+1]
                i=(i//2)-1
        self.comc(0)

    def getm(self,x,y):
        if x<y:
            return x
        return y

    def isEmpty(self):
        if self.leng<0:
            return True
        return False
    def updatePriority(self,v,x):
        for i in range(self.leng):
            if self.arr[i]==v:
                self.arr[i].dist=x
        self.heapify()
        