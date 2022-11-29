import math

def getRelativeRotation(centerRotation, targetRotation):
    while targetRotation < centerRotation - 180:
        targetRotation += 360
    while targetRotation > centerRotation + 180:
        targetRotation -= 360
    return targetRotation

def getDistance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))

def lengthDirX(distance, angle):
    return math.cos(angle) * distance

def lengthDirY(distance, angle):
    return -math.sin(angle) * distance

def lengthDirXDegrees(distance, angle):
    return lengthDirX(distance, math.radians(angle))

def lengthDirYDegrees(distance, angle):
    return lengthDirY(distance, math.radians(angle))

def rectsColliding(rect1, rect2):
    return (rect1[0] <= rect2[2] and rect1[2] >= rect2[0] and rect1[1] <= rect2[3] and rect1[3] >= rect2[1])

def rectCircleColliding(rect, circle):
    rectWidth = rect[2] - rect[0]
    rectHeight = rect[3] - rect[1]
    circleDistance = (abs(circle[0][0] - (rect[0] + rect[2]) / 2),
                      abs(circle[0][1] - (rect[1] + rect[3]) / 2))
    
    if circleDistance[0] > rectWidth / 2 + circle[1] or circleDistance[1] > rectHeight / 2 + circle[1]:
        return False
    
    if circleDistance[0] <= rectWidth / 2 or circleDistance[1] <= rectHeight / 2:
        return True
    
    cornerDistanceSQ = math.pow(circleDistance[0] - rectWidth / 2, 2) + math.pow(circleDistance[1] - rectHeight / 2, 2)
    
    return (cornerDistanceSQ <= math.pow(circle[1], 2))