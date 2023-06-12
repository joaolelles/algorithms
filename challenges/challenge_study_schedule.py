def study_schedule(permanence_period, target_time):
    students = 0
    if target_time is None:
        return None
    for hour in permanence_period:
        if type(hour[0]) != int or type(hour[1]) != int:
            return None
        if hour[0] <= target_time <= hour[1]:
            students += 1
    return students
