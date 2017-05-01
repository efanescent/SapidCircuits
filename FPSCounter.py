
fps = 0
frameCount = 0
timer = 1000

def getFps():
    return fps

def frame(unknownParam):
    global frameCount, timer
    frameCount += 1
    timer -= (1000 * unknownParam)
    if timer <= 0:
        global fps
        fps = frameCount
        frameCount = 0
        timer = 1000

