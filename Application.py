import time
from CaseService import getNextCases

class Application:
  CAN_POLL = False
  POLL_INTERVAL = 1

  def allowPolling(self):
    self.CAN_POLL = True

  def disallowPolling(self):
    self.CAN_POLL = False

  def throttledPoll(self, seconds, action):
    while self.CAN_POLL:
      try:
          action()
          time.sleep(seconds)
      except:
          continue

  def main(self):
    self.throttledPoll(self.POLL_INTERVAL, getNextCases)