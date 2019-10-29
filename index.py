
from Application import Application
from unittest.mock import MagicMock
from ratelimit import RateLimitException
from time import sleep

instance = Application()

################################################################################

def testThrottlePollFail():
  mock = MagicMock()

  # test the function
  try:
    while True:
      instance.throttledPoll(mock)

  except RateLimitException:
    assert(mock.call_count == 1)

def testThrottlePoll():
  mock = MagicMock()

  # test the function
  try:
    instance.throttledPoll(mock)
    sleep(5)
    instance.throttledPoll(mock)

  except RateLimitException:
    assert(False, 'exception should never happen')

  assert(mock.call_count == 2)

def testThrottlePoll():
  mock = MagicMock()

  # test the function
  try:
    instance.throttledPoll(mock)
    sleep(5)
    instance.throttledPoll(mock)

  except RateLimitException:
    assert(False, 'exception should never happen')

  assert(mock.call_count == 2)

def testThrottlePoll():
  mock = MagicMock()

  # test the function
  instance.throttledPoll(mock)
  instance.throttledPoll(mock)

  assert(mock.call_count == 2)


################################################################################

print('START')

testThrottlePoll()

print('END')