if __name__ == '__main__':
     N = int(raw_input())
     arr=[]
     for i in range(N):
         a=raw_input()
         if a=='insert':
             p=int(raw_input())
             e=int(raw_input())
             arr.insert(p,e)
         elif a=='remove':
             r=int(raw_input())
             arr.remove(r)
         elif a=='append':
             ap=int(raw_input())
             arr.append(ap)
         elif a=='sort':
             arr.sort() 
             print arr			
         elif a=='pop':
             arr.pop()
         elif a=='reverse':
             arr.reverse()
         elif a=='print':
             print arr


