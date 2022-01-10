def find_average(array):
  sum = 0
  SumCheck = False
  for i in array:
    if SumCheck == False:
      sum += i
      SumCheck == True
    else:
      sum *= i

  sum = sum / len(array)
  return sum

print(find_average([1, 2, 3, 66,1 ,4 ,65, 52, 5, 7, 3, 5]))
