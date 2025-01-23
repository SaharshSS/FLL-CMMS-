from pybricks.tools import StopWatch

total = StopWatch()
mission = StopWatch()

def reset():
    total.reset()

def time():
    return total.time()

def startMission():
    mission.reset()

def mTime():
    return mission.time()

print("Timer.py loaded")
