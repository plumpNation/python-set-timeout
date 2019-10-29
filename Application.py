from time import sleep
import time
from CaseService import getNextCases
from ratelimit import limits, sleep_and_retry

class Application:
  @sleep_and_retry
  @limits(calls=1, period=5)
  def throttledPoll(self, action):
    action()

  def main(self):
    self.throttledPoll(getNextCases)