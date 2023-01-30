def time_calculator(start_time, duration, start_day='none'):
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    start_hour = int(start_time.split(":")[0])
    start_minute = int(start_time.split(":")[1].split(" ")[0])
    if start_time[len(start_time) - 2] == 'P':
        start_hour += 12
    end_hour = start_hour + int(duration.split(":")[0])
    end_minute = start_minute + int(duration.split(":")[1])
    if end_minute > 59:
        end_hour += 1
        end_minute = end_minute - 60
    i = 0
    while True:
        if end_hour > 23:
            i += 1
            end_hour -= 24
        else:
            break
    # formatting output:
    new_time = ''
    str_minute = ''
    if end_minute < 10:
        str_minute += '0'+str(end_minute)
    else:
        str_minute += str(end_minute)
    if end_hour == 0:
        new_time += '12:' + str_minute + ' AM'
    elif 0 < end_hour < 12:
        new_time += str(end_hour) + ':' + str_minute + ' AM'
    elif end_hour == 12:
        new_time += '12:' + str_minute + ' PM'
    elif 12 < end_hour < 24:
        new_time += str(end_hour - 12) + ':' + str_minute + ' PM'
    if start_day != 'none':
        t = i
        for j in days:
            if j.upper() == start_day.upper():
                break
            t += 1
        new_time += ', ' + days[t % 7]
    if i != 0:
        if i == 1:
            new_time += ' (next day)'
        else:
            new_time += ' (' + str(i) + ' days later)'
    return new_time


def main():
    print(time_calculator("3:00 PM", "3:10"))
    # Returns: 6:10 PM

    print(time_calculator("11:30 AM", "2:32", "Monday"))
    # Returns: 2:02 PM, Monday

    print(time_calculator("11:43 AM", "00:20"))
    # Returns: 12:03 PM

    print(time_calculator("10:10 PM", "3:30"))
    # Returns: 1:40 AM (next day)

    print(time_calculator("11:43 PM", "24:20", "tueSday"))
    # Returns: 12:03 AM, Thursday (2 days later)

    print(time_calculator("6:30 PM", "205:12"))
    # Returns: 7:42 AM (9 days later)


if __name__ == '__main__':
    main()
