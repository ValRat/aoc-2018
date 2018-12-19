#/usr/bin/env python3
import re

def main():
    # part1()
    part2()

def print_solution(solution):
    sol_string = ""
    for s in solution:
        sol_string += job_to_string(s)
    print(sol_string)

def create_graph(steps_input):
    # Steps are only from A to Z so can use 26 x 26 board for
    # representation. A to Z must exist otherwise we screwed.
    mat = [[0 for x in range(26)] for x in range(26)]
    num_inst = set()
    for line in steps_input:
        vals = re.search(r'Step (?P<dep>\w{1}) must be finished before step (?P<node>\w{1}) can begin.', line)
        if (vals):
            dep = vals.group('dep')
            node = vals.group('node')
            # Capital Ascii Representation
            mat[ord(dep) - 65][ord(node) - 65] = 1
            num_inst.add(dep)
            num_inst.add(node)
    return mat, len(num_inst)

def get_next_job(mat, exclude):
    # Scan columns starting from beginning
    for i in range(26):
        if i in exclude:
            continue

        is_runnable = True
        for j in range(26):
            if (mat[j][i]):
                is_runnable = False
                break
        if (is_runnable):
            return i
    return -1
    

def set_job_finish(mat, job):
    # Python always pass by reference
    for k in range(26):
        mat[job][k] = 0


def get_job_duration(job):
    # Non-Ascii representation
    return job + 61

def part1():
    with open('in.txt') as f:
        steps_input = f.readlines()
        mat, num_inst = create_graph(steps_input)

        order = []
        # Should in theory go until size of order doesn't change
        # i.e. all instructions accounted for
        len_order = None
        while (num_inst != len(order)):
            len_order = len(order)

            next_job = get_next_job(mat, order)
            if (next_job != -1):
                order.append(next_job)
                set_job_finish(mat, next_job)
        print_solution(order)

class Worker:

    def __init__(self):
        self.job = None
        self.t_end = 0

def has_available_worker(workers):
    for worker in workers:
        if worker.job is None:
            return worker
    return None

def has_available_job(mat, current, done):
    exclude = list(current)
    exclude.extend(list(done))
    return get_next_job(mat, exclude)

def assign_worker_job(worker, job, t):
    worker.job = job
    worker.t_end = t + get_job_duration(job)

def work_worker(worker, t):
    if (worker.t_end == t):
        job = worker.job
        worker.job = None
        return job
    return None

def print_status(workers):
    for i, worker in enumerate(workers):
        if (worker.job):
            print('Worker ', i, ' doing ', job_to_string(worker.job), ' finish at ', worker.t_end)
        else:
            print('Worker ', i, ' idle')

def job_to_string(job):
    return chr(job + 65)

def part2():
    with open('in.txt') as f:
        t = 0
        mat, num_inst = create_graph(f.readlines())
        workers = [Worker() for i in range(5)]

        done = []
        current = []

        while (len(done) != num_inst):
            for worker in workers:
                job_done = work_worker(worker, t)
                if (job_done is not None):
                    print('Finishing :', job_to_string(job_done), ' at time ', t)
                    current.remove(job_done)
                    done.append(job_done)
                    set_job_finish(mat, job_done)
            while (has_available_worker(workers) and has_available_job(mat, current, done) != -1):
                worker = has_available_worker(workers)
                job = has_available_job(mat, current, done)
                assign_worker_job(worker, job, t)
                print('Assigning :', job_to_string(job), ' at time ', t)
                current.append(job)
            if (t % 100 == 0):
                print('Time: ', t)
                print_status(workers)
            t += 1

        # Actual answer is t - 1
        print(t - 1)
        

if __name__ == '__main__':
    main()
