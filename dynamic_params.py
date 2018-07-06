def myFunction(*kargs):
  return kargs[0]+ kargs[1]

result = myFunction(22, 33)
print(result) # 55
## ==================================

def mySecondFunction(**kwargs):
  return kwargs['a'] + kwargs['a']

result = mySecondFunction(a = 22, b = 55)
print(result) #77

## ==================================

def myThirdFunction(a, b):
  return a + b

params = [22, 33]
result = myThirdFunction(*params)
print(result) # 55
## ==================================

params = (22, 33)
result = myThirdFunction(*params)
print(result) # 55

