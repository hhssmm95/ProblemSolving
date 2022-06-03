from collections import defaultdict
from math import ceil


def toMinute(time):
    return int(time[0:2])*60 + int(time[3:])

def solution(fees, records):
    answer = []
    defaultTime, defaultFee, perTime, perFee = fees
    records.sort(key = lambda x : (list(x.split())[1], list(x.split())[0]))

    i = 0
    prevCarNum = -1
    totalTime = 0
    while i < len(records):

        time1, carNum1, behavior1 = records[i].split()
        if i+1 >= len(records):
            carNum2 = ""
        else:
            time2, carNum2, behavior2 = records[i+1].split()
        if carNum1 != carNum2:
            time2 = "23:59"
            carNum2 = carNum1
            behavior2 = 'OUT'
            i+=1
        else:
            i+=2

        if prevCarNum != -1 and prevCarNum != carNum1:
            totalCost = 0
            totalCost+=defaultFee
            if totalTime > defaultTime:
                totalCost += (ceil((totalTime-defaultTime) / perTime) * perFee)
            answer.append(totalCost)
            totalTime = 0
            

        

        totalTime += toMinute(time2) - toMinute(time1)
        prevCarNum = carNum1

    totalCost = 0
    totalCost+=defaultFee
    if totalTime > defaultTime:
        totalCost += (ceil((totalTime-defaultTime) / perTime) * perFee)
    answer.append(totalCost)
        


    return answer

print(solution([120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))

'''cases
fees	records	result
[180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
[1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
'''