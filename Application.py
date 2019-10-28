import time

class State(object):
    running = False

class Application:

  def main(self, state):
    while state.running:
      print('sec')
      print(state.running)

      try:
          time.sleep(1)
      except:
          continue