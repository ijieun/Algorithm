a, b, c = map(int, input().split())

# Write your code here!

def find_minutes(a,b,c):
   first_minutes = 10*24*60 + 11*60 + 11
   second_minutes = (a-1)*24*60 + b*60 + c 
   if first_minutes > second_minutes:
      return -1
   else:
      return second_minutes - first_minutes


print(find_minutes(a,b,c))