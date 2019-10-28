
from Timer import Timer
from Application import Application
from unittest.mock import MagicMock

instance = Application()

def onTimeout():
  instance.disallowPolling()
  print('Setting State.running to false')

################################################################################

def testThrottlePoll():
  timer = Timer()

  timer.setTimeout(onTimeout, 5)

  instance.allowPolling()

  mock = MagicMock()

  # test the function
  instance.throttledPoll(1, mock)

  assert(mock.call_count == 4)


################################################################################

print('START:')

testThrottlePoll()

print('END:')