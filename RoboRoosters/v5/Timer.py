from pybricks.tools import StopWatch

watch = StopWatch()
watch2 = StopWatch()

def reset():
    watch.reset()

def time():
    return watch.time()

def startMission():
    watch2.reset()

def mTime():
    return watch2.time()

print("Timer.py loaded")
