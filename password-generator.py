import random 
def gen(n):
  start='1'*n
  end='9'*n
  i=random.randint(int(start),int(end))
  return i
if __name__=="__main__":
  x=int(input("HOW MANY DIGIT PASSWORD DO YOU WANT "))
  p=gen(x)
  print(p)
