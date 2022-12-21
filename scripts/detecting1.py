
def distance8_51(landmark, shape):
    x1, y1 = landmark[0].x * shape[1], landmark[0].y * shape[0]
    x2, y2 = landmark[8].x * shape[1], landmark[8].y * shape[0]
    x3, y3 = landmark[5].x * shape[1], landmark[5].y * shape[0]
    d1 = ((x1 - x2)**2 + (y1 - y2) **2) **.5
    d2 = ((x1 - x3)**2 + (y1 - y3) **2) **.5
    return d1/d2 > 1.5

def distance12_91(landmark, shape):
    x1, y1 = landmark[0].x * shape[1], landmark[0].y * shape[0]
    x2, y2 = landmark[12].x * shape[1], landmark[12].y * shape[0]
    x3, y3 = landmark[9].x * shape[1], landmark[9].y * shape[0]
    d1 = ((x1 - x2)**2 + (y1 - y2) **2) **.5
    d2 = ((x1 - x3)**2 + (y1 - y3) **2) **.5
    return (d1 < d2) or d1/d2 < 1.3
    

def distance16_131(landmark, shape):
    x1, y1 = landmark[0].x * shape[1], landmark[0].y * shape[0]
    x2, y2 = landmark[16].x * shape[1], landmark[16].y * shape[0]
    x3, y3 = landmark[13].x * shape[1], landmark[13].y * shape[0]
    d1 = ((x1 - x2)**2 + (y1 - y2) **2) **.5
    d2 = ((x1 - x3)**2 + (y1 - y3) **2) **.5
    return (d1 < d2) or d1/d2 < 1.3

def distance20_171(landmark, shape):
    x1, y1 = landmark[0].x * shape[1], landmark[0].y * shape[0]
    x2, y2 = landmark[20].x * shape[1], landmark[20].y * shape[0]
    x3, y3 = landmark[17].x * shape[1], landmark[17].y * shape[0]
    d1 = ((x1 - x2)**2 + (y1 - y2) **2) **.5
    d2 = ((x1 - x3)**2 + (y1 - y3) **2) **.5
    return (d1 < d2) or d1/d2 < 1.3
