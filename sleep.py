import time
from Timer import Timer

################################################################################

class State:
  running = False

################################################################################

def loop_for(seconds, state):
    state.running = True

    while state.running:
        print('sec')
        print(state.running)
        try:
            time.sleep(1)
        except:
            continue

################################################################################

timer = Timer()

def some_fn():
    State.running = False
    print('Setting running to false')

#  Above will execute some_fn call after 5 sec
timer.setTimeout(some_fn, 5.0)
# timer.setClearTimer()

# Above line of codes will not execute some_fn call as timer is cleared before 3 seconds


################################################################################

print('START:')
print(State.running)

loop_for(5, State)

print('END:')
print(State.running)