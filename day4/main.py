#/usr/bin/env python3
import re
import datetime as dt

# Strategy one:
# Guard that slept the most * the minute timeslot they slept most frequently
# Observation: No guard fell asleep BEFORE midnight

class Event:
    """
    Helper class for ordering events temporally
    """
    
    def __init__(self, time, event):
        self.time = time
        self.event = event

    def __lt__(self, other):
        return self.time < other.time

    def __str__(self):
        return str(self.time) + ' ' + self.event

def parse_event(event):
    vals = re.search(r'\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<event>.*)', event)
    year = int(vals.group('year'))
    month = int(vals.group('month'))
    day = int(vals.group('day'))
    hour = int(vals.group('hour'))
    minute= int(vals.group('minute'))
    event = vals.group('event')
    return Event(dt.datetime(year, month, day, hour, minute), event)

def get_guard(event):
    vals = re.search(r'#(?P<guard_id>\d+)', event.event)
    if (vals):
        return vals.group('guard_id')
    return None

def is_asleep(event):
    vals = re.compile(r'falls asleep').match(event.event)
    if (vals):
        return True
    return False

def is_awake(event):
    vals = re.compile(r'wakes up').match(event.event)
    if (vals):
        return True
    return False

def main():
    # part1()
    part2()

def part1():
    with open('in.txt') as f:
        events = []
        for line in f.readlines():
            e = parse_event(line)
            events.append(e)

        events.sort()
        for event in events:
            print(event)


        guards = dict()
        curr_guard = None
        is_sleep = False
        sleep_start_time = None
        for event in events:
            next_guard = get_guard(event)
            if (next_guard):
                curr_guard = next_guard
                if (curr_guard not in guards):
                    guards[curr_guard] = [0] * 60
                continue
            # Parse wake up and sleep events
            if (is_asleep(event)):
                is_sleep = True
                sleep_start_time = event.time
                continue
            if (is_awake(event)):
                is_sleep = False
                sleep_end_time = event.time
                for i in range(sleep_start_time.minute, sleep_end_time.minute):
                    guards[curr_guard][i] += 1
        guard_max_sleep = None
        guard_max_sleep_value = 0
        for guard in guards:
            if sum(guards[guard]) > guard_max_sleep_value:
                guard_max_sleep = guard
                guard_max_sleep_value = sum(guards[guard])
        max_value = max(guards[guard_max_sleep])
        max_timeslot = guards[guard_max_sleep].index(max_value)
        print('Guard: ' + str(guard_max_sleep) + ' slept most at ' + str(max_timeslot))


def part2():
    with open('in.txt') as f:
        events = []
        for line in f.readlines():
            e = parse_event(line)
            events.append(e)

        events.sort()
        for event in events:
            print(event)


        guards = dict()
        curr_guard = None
        is_sleep = False
        sleep_start_time = None
        for event in events:
            next_guard = get_guard(event)
            if (next_guard):
                curr_guard = next_guard
                if (curr_guard not in guards):
                    guards[curr_guard] = [0] * 60
                continue
            # Parse wake up and sleep events
            if (is_asleep(event)):
                is_sleep = True
                sleep_start_time = event.time
                continue
            if (is_awake(event)):
                is_sleep = False
                sleep_end_time = event.time
                for i in range(sleep_start_time.minute, sleep_end_time.minute):
                    guards[curr_guard][i] += 1
        guard_max_sleep = None
        guard_max_sleep_value = 0
        for guard in guards:
            if max(guards[guard]) > guard_max_sleep_value:
                guard_max_sleep = guard
                guard_max_sleep_value = max(guards[guard])
        max_value = max(guards[guard_max_sleep])
        max_timeslot = guards[guard_max_sleep].index(max_value)
        print('Guard: ' + str(guard_max_sleep) + ' slept most at ' + str(max_timeslot))

if __name__ == '__main__':
    main()
