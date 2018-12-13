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


def main():
    part1()
    # part2()

def part1():
    with open('in.txt') as f:
        events = []
        for line in f.readlines():
            e = parse_event(line)
            events.append(e)

        events.sort()

        guards = dict()
        curr_guard = None
        for event in events:
            if get_guard(event):
                curr_guard = get_guard(event)
                continue


def part2():
    # 1000x1000 array
    # These are gross solutions
    cut_claim = [[0] * 2000 for i in range(2000)]
    with open('in.txt') as f:
        lines = f.readlines()
        for line in lines:
            vals = re.search(r'\#\d+ @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line)
            if (vals):
                x = int(vals.group('x'))
                y = int(vals.group('y'))
                w = int(vals.group('w'))
                h = int(vals.group('h'))
                for i in range(w):
                    for j in range(h):
                        cut_claim[x + i + 1][y + j + 1] += 1
        for line in lines:
            vals = re.search(r'\#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)', line)
            if (vals):
                x = int(vals.group('x'))
                y = int(vals.group('y'))
                w = int(vals.group('w'))
                h = int(vals.group('h'))
                has_overlap = False
                for i in range(w):
                    if not has_overlap:
                        for j in range(h):
                            if (cut_claim[x + i + 1][y + j + 1] > 1):
                                has_overlap = True
                                break
                if not has_overlap:
                    print(vals.group('id'))
                    return



if __name__ == '__main__':
    main()
