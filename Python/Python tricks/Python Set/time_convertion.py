def timeConversion(s):
    hours, minutes, seconds = s.split(':')
    period = ''
    if "AM" in s:
        period = seconds.strip('AM')
        if hours == '12':
            hours = '00'
    if "PM" in s:
        period = seconds.strip('PM')
        print(period)
        if hours != '12':
            hours = str(int(hours)+12)
    return f"{hours}:{minutes}:{period}"