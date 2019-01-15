#We say a number is sparse if there are no adjacent ones in its binary representation.
#For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N,
#find the smallest sparse number greater than or equal to N

def findnum(newint):
   global sparse
   sparse= False
   int= newint
   while (sparse==False):
      b = bin(int)[2:]
      l = len(b)-1
      i=0
   
      temp=0
      while (i<l):
         if (b[i]=='1') & (b[i+1]=='1'):
            temp=temp+1
     
         i=i+1
     
      if (temp==0):
         sparse=True
         print(int," is the closest sparse number")
      else:
         sparse=False
      
      int=int+1

findnum(67)
