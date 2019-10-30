
from Application import Application
from unittest.mock import MagicMock
from ratelimit import RateLimitException
from time import sleep

instance = Application()

################################################################################

# def testThrottlePollFail():
#   mock = MagicMock()

#   # test the function
#   try:
#     while True:
#       instance.throttledPoll(mock)

#   except RateLimitException:
#     assert(False, 'this should never happen')

def testThrottlePollWithSleep():
  mock = MagicMock()

  throttledPoll = instance.createThrottledPoll(mock, calls=1, period=5)

  # test the function
  try:
    throttledPoll()
    sleep(5)
    throttledPoll()

  except RateLimitException:
    assert(False, 'exception should never happen')

  print(mock.call_count)
  assert(mock.call_count == 2)

def testThrottlePoll():
  mock = MagicMock()
  throttledPoll = instance.createThrottledPoll(mock, calls=1, period=2)

  # test the function
  throttledPoll()
  throttledPoll()

  assert(mock.call_count == 2)


################################################################################

print('START')

# testThrottlePollFail()
# testThrottlePoll()
testThrottlePollWithSleep()

print('END')