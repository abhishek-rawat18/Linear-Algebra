import pandas as pd

def matches(players,alpha,AtpPoints,GroupMatches,SemiFinals,Final):

  n=len(players) #the number of players

  initial=AtpPoints[:] #initial score of players

  df=pd.DataFrame() #to store match points for various alpha
  df["Players"]=players
  df["Initial"]=initial

  df2=pd.DataFrame() #to store ranks for various alpha

  z=list(zip(players,initial))
  sorted=mergesort(z) #in descending order
  ranks=list() #a list of ranks according to various alpha
  temp=[]
  for i in range(0,n):
    temp.append(sorted[i][0])
  ranks.append(temp)
  df2["Initial"]=ranks[0]
  
  ranks=list()
  
  x=[GroupMatches,SemiFinals,Final] #list of types of matches
  y=[200,400,500] #list of match points according to match type

  for a in range(0,len(alpha)):
    AtpPoints=initial[:]
    for i in range(0,len(x)):
      for j in range(0,len(x[i])):
        match=x[i][j]
        won,lost=match #since an edge denotes winner to looser  
        AtpPoints[won-1]+=y[i]+round(AtpPoints[lost-1]*alpha[a])
        #this is the scoring system

    df[alpha[a]]=AtpPoints
    
    #Now ranking
    z=list(zip(players,AtpPoints))
    sorted=mergesort(z) #in descending order
    temp=[]
    for i in range(0,n):
      temp.append(sorted[i][0])
    ranks.append(temp)

    df2[alpha[a]]=ranks[a]
    
  print(df)
  print("\n")
  print(df2)
  
#functions for sorting players to rank them
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

#Our input
players=['Federer','Nadal','Djokovic','Murray','Del Potro'
         ,'Davydenko','Verdasco','Soderling']
AtpPoints=[10150,9205,7910,6630,5985,3630,3300,3010]
GroupMatches=[(4,5),(1,7),(5,7),(1,4),(4,7),(5,1),(8,2),
               (3,6),(8,3),(6,2),(3,2),(6,8)]
SemiFinals=[(6,1),(5,8)]
Final=[(6,5)]
alpha=[0,0.05,0.1,0.15,0.2]

matches(players,alpha,AtpPoints,GroupMatches,SemiFinals,Final)
#calling the main function with the set of inputs
