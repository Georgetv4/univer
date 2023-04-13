from datetime import datetime


def doctor_is_available(schedule, current_time):
    if not schedule:
        return "The doctor is available"

    current_time = datetime.strptime(current_time, '%H:%M')

    for i in schedule:
        start_time = datetime.strptime(i[0], '%H:%M')
        end_time = datetime.strptime(i[1], '%H:%M')
        if start_time <= current_time <= end_time:
            return end_time.strftime('%H:%M')

    return "The doctor is available"
