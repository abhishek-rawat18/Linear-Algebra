import pandas as pd

def matches(players,AtpPoints,GroupMatches,SemiFinals,Finals):

  n=len(players)

  print("Enter value of alpha:")
  alpha=float(input())

  initial=AtpPoints[:]

  x=[GroupMatches,SemiFinals,Finals] #list of types of matches
  y=[200,400,500] #list of match points according to match type
  
  for i in range(0,len(x)):
    for j in range(0,len(x[i])):
      match=x[i][j]
      won,lost=match      
      AtpPoints[won-1]+=y[i]+round(AtpPoints[lost-1]*alpha,2)
    
  df=pd.DataFrame(columns=["Player","Initial","Final"])
  for i in range(0,n):
    x={"Player":players[i],"Initial":initial[i],"Final":round(AtpPoints[i])}
    df=df.append(x,ignore_index=True)
  print(df)

  print("\n")
  
  #Now ranking
  z=list(zip(players,AtpPoints))
  sorted=mergesort(z) #in descending order
  for i in range(0,n):
    print("Rank {} : {}".format(i+1,sorted[i][0]))
  

def mergesort(l):
  if len(l) < 2:
    return l
  mid = len(l)//2
  leftlist = l[0:mid]
  rightlist = l[mid:]
  return merge(mergesort(leftlist),mergesort(rightlist))

def merge(l1,l2): 
  if l1 == [] or l2 == []:
    return l1 + l2
  if l1[0][1] >= l2[0][1]:
    return [l1[0]] + merge(l1[1:], l2)
  else:
    return [l2[0]] + merge(l1, l2[1:])


players=['Federer','Nadal','Djokovic','Murray',
         'Del Potro','Davydenko','Verdasco','Soderling']
AtpPoints=[10150,9205,7910,6630,5985,3630,3300,3010]
GroupMatches=[(4,5),(1,7),(5,7),(1,4),(4,7),(5,1),(8,2),
              (3,6),(8,3),(6,2),(3,2),(6,8)]
SemiFinals=[(6,1),(5,8)]
Final=[(6,5)]
matches(players,AtpPoints,GroupMatches,SemiFinals,Final)  
  


    


