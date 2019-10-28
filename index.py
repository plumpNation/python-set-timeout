
from Timer import Timer
from Application import Application
from Application import State

def some_fn():
  State.running = False
  print('Setting State.running to false')

################################################################################

def runTest():
  instance = Application()
  timer = Timer()

  timer.setTimeout(some_fn, 5)

  State.running = True

  instance.main(State)


################################################################################

print('START:')
print(State.running)

runTest()

print('END:')
print(State.running)