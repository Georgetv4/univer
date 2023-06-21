def subtract_times(end_time, start_time):
    if end_time[0] < start_time[0] or end_time[0] == start_time[0] and end_time[1] < start_time[1]:
        return 0

    return (end_time[0]*60 + end_time[1]) - (start_time[0]*60 + start_time[1])

def total_waiting_time(arrival_times, exit_times):
    if len(arrival_times) < 2:
        return 0

