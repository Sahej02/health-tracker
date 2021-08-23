STEPS_TO_METRES = 0.75

def week_stats(dist_in_metres, time_in_seconds):
    
    metrics = {}
    award = 0

    for i in range(len(dist_in_metres) - 1, -1, -1):
        if dist_in_metres[i] == 0:
            award += 1
            dist_in_metres.pop(i)
            time_in_seconds.pop(i)

    speed_in_ms = [dist_in_metres[i]/time_in_seconds[i] for i in range(len(dist_in_metres))]
    metrics["max_speed"] = round(max(speed_in_ms), 2)
    metrics["max_dist"] = round(max(dist_in_metres), 2)
    metrics["min_speed"] = round(min(speed_in_ms), 2)
    metrics["min_dist"]= round(min(dist_in_metres), 2)
    metrics["avg_speed"] = round(sum(speed_in_ms)/len(speed_in_ms), 2)
    metrics["avg_dist"] = round(sum(dist_in_metres)/len(dist_in_metres), 2)

    return metrics, award

def month_stats(weeks_list):

    metrics = {}
    award = True
    count = 0
    result = 0

    for i in range(4):
        if weeks_list[i][1] > 2:
            count = 0
        else:
            count += 1
            result = max(result, count)
    
    if result < 2:
        award = False

    metrics["max_speed"] = max([weeks_list[i][0]["max_speed"] for i in range(4)])
    metrics["max_dist"] = max([weeks_list[i][0]["max_dist"] for i in range(4)])
    metrics["min_speed"] = min([weeks_list[i][0]["min_speed"] for i in range(4)])
    metrics["min_dist"]= min([weeks_list[i][0]["min_dist"] for i in range(4)])
    metrics["avg_speed"] = round(sum([weeks_list[i][0]["avg_speed"] for i in range(4)])/4, 2)
    metrics["avg_dist"] = round(sum([weeks_list[i][0]["avg_dist"] for i in range(4)])/4, 2)

    return metrics, award, result

def quarter_stats(months_list):

    metrics = {}
    award = True
    count = 0
    result = 0

    for i in range(4):
        if months_list[i][1] == False:
            count = 0
        else:
            count += 1
            result = max(result, count)
    
    if result < 2:
        award = False

    metrics["max_speed"] = max([months_list[i][0]["max_speed"] for i in range(4)])
    metrics["max_dist"] = max([months_list[i][0]["max_dist"] for i in range(4)])
    metrics["min_speed"] = min([months_list[i][0]["min_speed"] for i in range(4)])
    metrics["min_dist"]= min([months_list[i][0]["min_dist"] for i in range(4)])
    metrics["avg_speed"] = round(sum([months_list[i][0]["avg_speed"] for i in range(4)])/4, 2)
    metrics["avg_dist"] = round(sum([months_list[i][0]["avg_dist"] for i in range(4)])/4, 2)

    return metrics, award, result

def read_file(identify):

    check = True
    dist_in_metres = []
    time_in_seconds = []
    with open("input.txt", "r") as file:
        for line in file:
            if not line.strip():
                continue
            s, t = line.split(",")[1:]
            s = int(s) * STEPS_TO_METRES
            t = t.split(":")
            t = 3600 * int(t[0]) + 60 * int(t[1]) + int(t[2])
            dist_in_metres.append(s)
            time_in_seconds.append(t)
    
    if identify == "w":
        if len(dist_in_metres) != 7:
            check = False

    elif identify == "m":
        if len(dist_in_metres) != 28:
            check = False

    elif identify == "q":
        if len(dist_in_metres) != 112:
            check = False

    return dist_in_metres, time_in_seconds, check
