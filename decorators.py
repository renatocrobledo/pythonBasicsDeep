# http://docs.python-guide.org/en/latest/writing/style/

def my_decorator(func):
  def function_wrapper(x):
    print('before!')
    func(x)
    print('after!')
  return function_wrapper

#@my_decorator
def foo(x):
  print('what happend?', x)

foo = my_decorator(foo)

foo('now')