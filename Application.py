from time import sleep
import time
from CaseService import getNextCases
from ratelimit import limits, sleep_and_retry

class Application:
  def createThrottledPoll(self, action, calls=1, period=5):
    @sleep_and_retry
    @limits(calls=calls, period=period)
    def throttledPoll():
      action()

    return throttledPoll

  # def main(self):
  #   self.throttledPoll(getNextCases)