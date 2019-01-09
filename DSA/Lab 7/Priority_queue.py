class BinHeap:
    def __init__(self):
        self.L = [0]
        self.Size = 0


    def heapifyUp(self,i):
        while i // 2 > 0:
          if self.L[i] > self.L[i // 2]:
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
          mc = self.maxChild(i)
          if self.L[i] < self.L[mc]:
              tmp = self.L[i]
              self.L[i] = self.L[mc]
              self.L[mc] = tmp
          i = mc

    def maxChild(self,i):
      if i * 2 + 1 > self.Size:
          return i * 2
      else:
          if self.L[i*2] > self.L[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def extractMax(self):
      retval = self.L[1]
      self.L[1] = self.L[self.Size]
      self.Size = self.Size - 1
      self.L.pop()
      self.heapifyDown(1)
      return retval

    def buildHeap(self,alist):
      self.L=[0]
      self.Size=0
      for i in alist:
      	self.insert(i)
      	

def main():
    bh = BinHeap()
    ch=0
    # while(ch!=6):
    #     print(" 1.Insert\n 2.Delete-Max\n 3.Max \n 4.Build-Heap \n 5.Heap_Sort \n 6.Exit \n")
    #     ch=int(input("Enter choice :"))
    #     if ch==1:
    #         temp=0
    #         temp=int(input("Enter Element : "))
    #         bh.insert(temp)

    #     elif ch==2:
    #         print("Max was : " , bh.extractMax())
        
    #     elif ch==3:
    #         print("Max is : " , bh.L[1])
        
    #     elif ch==4:
    #          bh.buildHeap([9,5,2,3,6])
        
    #     elif ch==5:
        	
    #         for i in range(0,bh.Size):
    #             result.append(bh.extractMax())
    #         bh.buildHeap(result)
    #         print(result)

    bh.insert(6)
    bh.insert(5)
    bh.insert(21)
    bh.insert(40)
    bh.insert(1)
    bh.insert(50)
    bh.insert(2)
    bh.insert(14)
    bh.insert(81)

    print(bh.L)



    #extractmax
    print(bh.extractMax())


    #heapsort
    result=[]
    for i in range(0,bh.Size):
      result.append(bh.extractMax())
    bh.buildHeap(result)
    print(result)





          
            
           
        


        
    
if __name__=='__main__':
    main()
