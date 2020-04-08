'''
Utility functions for URL generation and other things
'''

def timestamp_to_seconds(timestamp):
    '''
    Takes timestamp of form HH:MM:SS (or MM:SS, or SS) and converts to number
    of seconds. Useful for generating YouTube URLs at time offsets.
    '''

    hms = timestamp.split(':')
    seconds = 0
    for i,num in enumerate(hms):
        seconds += 60**(len(hms)-i-1) * int(num)

    return seconds

