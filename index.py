
from Timer import Timer
from Application import Application

instance = Application()

def onTimeout():
  instance.disallowPolling()
  print('Setting State.running to false')

################################################################################

def runTest():
  timer = Timer()

  timer.setTimeout(onTimeout, 5)

  instance.allowPolling()

  # test the function
  instance.main()


################################################################################

print('START:')

runTest()

print('END:')