from decorator import delay

class Timer():
    toClearTimer = False
    def setTimeout(self, fn, time):
        isInvokationCancelled = False
        @delay(time)
        def some_fn():
                if (self.toClearTimer is False):
                        fn()
                else:
                    print('Invokation is cleared!')
        some_fn()
        return isInvokationCancelled
    def setClearTimer(self):
        self.toClearTimer = True