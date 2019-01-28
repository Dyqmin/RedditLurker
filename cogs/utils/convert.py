import time


# Converts date to time that has passed since
def t_ago(t):
    secs = time.time() - t
    print(secs)
    secs = int(secs)
    if 120 > secs:
        return f'{secs} seconds ago'
    elif 3600 > secs:
        return '{} minutes ago'.format(secs // 60)
    elif 86400 > secs:
        if 7200 > secs:
            return '{} hour ago'.format(secs // 60 // 60)
        else:
            return '{} hours ago'.format(secs // 60 // 60)
    else:
        if 7200 > secs:
            return '{} day ago'.format(secs // 60 // 60 // 24)
        else:
            return '{} days ago'.format(secs // 60 // 60 // 24)