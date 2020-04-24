from CodeWarsTests import *


def pluralize(n, word):
    if n == 1:
        return '%d %s' % (n, word)
        
    return '%d %ss' % (n, word)
        
def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    
    units = (
        (365*24*60*60, 'year'),
        (24*60*60, 'day'),
        (60*60, 'hour'),
        (60, 'minute'),
        (1, 'second'),
    )
        
    r = []
    for unit in units:
        time_period, word = unit
        if seconds >= time_period:
            n = int(seconds / time_period)
            r.append(pluralize(n, word))
            seconds -= n * time_period
    
    return ' and'.join(', '.join(r).rsplit(',', 1))








test = Test()
test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")