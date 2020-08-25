def factorial(n):
  return 1 if n == 1 else n * factorial(n-1)


# def change(amount):
#   if amount == 8:  return [3, 5]
#   if amount == 9:  return [3, 3, 3]
#   if amount == 10:  return [5, 5]
#   coins = change(amount - 3)
#   coins.append(3)
#   return coins


def change(amount):
  if amount < 5: return 0
  if amount % 5 == 0: return[5 for i in range(amount//5)]
  if amount == 12: return[5, 7]
  if amount == 7:  return [7]
  coins = change(amount -7)
  coins.append(7)
  return coins
print(change(49))

for i in range(5, 500):
  try:  change(i)
  except: print(i)


def find(end, start = 0):
  answer = 1618235
  if (mid := (start+end+1)//2) == answer: return mid
  return find(mid + 1, start) if answer < mid else find(end, mid - 1)
print(find(2097151))
