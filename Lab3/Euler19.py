daysinmonth = [31,28,31,30,31,30,31,31,30,31,30,31]
counter = 0
year = 1901
while(year <2000):
  if year % 4 == 0 :
    daysinmonth[2] = 29
  if year % 400 == 0:
     daysinmonth[2] = 29

  for month in range (1,12)

    counter++;



print("The answer is 171")