#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo 
# (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

one=8*60 +15
two=(7*60+12)*3
three=one
total= one +two+three
start= 6*3600+52*60
finish=total+start
a= int(finish//3600)
b= int(finish%3600)//60
c= int(finish%60)
print(a,':',b,':',c,'am')