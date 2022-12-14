import math


def validate_hours(hours):
    if len(hours) != 2 or int(hours) > 23:
        return False
    return True


def validate_minutes(minutes):
    if len(minutes) != 2 or int(minutes) > 60:
        return False
    return True


def minute_degrees(minutes):
    return int(minutes) / 60 * 360


def hour_degrees(hours):
    return int(hours) / 24 * 360


def get_clock_angle(iso_time):
    time_list = iso_time.split()
    if len(time_list) < 2:
        print("invalid input format")
        return
    input_hours = time_list[0]
    input_minutes = time_list[1]

    if not validate_hours(input_hours):
        print(input_hours + ":" + input_minutes)
        print("invalid hours format")
        return

    if not validate_minutes(input_minutes):
        print(input_hours + ":" + input_minutes)
        print("invalid minutes format")
        return
    diff_degrees = abs(minute_degrees(input_minutes) - hour_degrees(input_hours))
    narrowest_degrees = 360 - diff_degrees if diff_degrees > 180 else diff_degrees
    degrees = math.floor(narrowest_degrees)
    print(degrees)
    return degrees


if __name__ == '__main__':
    input_iso_time = input("Enter hour and minute: \n\n")
    get_clock_angle(input_iso_time)
