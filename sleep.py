import time
from Timer import Timer

running = False

def loop_for(seconds):
    global running

    running = True

    while running:
        print('sec')
        print(running)
        try:
            time.sleep(1)
        except:
            continue

################################################################################

timer = Timer()

def some_fn():
    global running

    running = False
    print('Setting running to false')

#  Above will execute some_fn call after 5 sec
timer.setTimeout(some_fn, 5.0)
# timer.setClearTimer()

# Above line of codes will not execute some_fn call as timer is cleared before 3 seconds


################################################################################

loop_for(5)