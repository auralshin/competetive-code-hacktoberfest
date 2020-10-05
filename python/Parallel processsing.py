#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq


class Worker:
    """Worker class.
    The workers are sorted by release time. If the release time is the same for
    both of them, workers are sorted by their thread_id.
    """

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time


class JobQueue:
    """Simulation of a program that processes a list of jobs in parallel.
    Samples:
    >>> job_queue = JobQueue()
    >>> job_queue.num_workers = 2
    >>> job_queue.jobs = [1, 2, 3, 4, 5]
    >>> job_queue.assign_jobs()
    >>> job_queue.write_response()
    0 0
    1 0
    0 1
    1 2
    0 4
    >>> # Explanation:
    >>> # 1. The two threads try to simultaneously take jobs from the list, so
    >>> # thread with index 0 actually takes the first job and starts
    >>> # working on it at the moment 0.
    >>> # 2. The thread with index 1 takes the second job and starts
    >>> # working on it also at the moment 0.
    >>> # 3. After 1 second, thread 0 is done with the first job and takes
    >>> # the third job from the list, and starts processing it immediately
    >>> # at time 1.
    >>> # 4. One second later, thread 1 is done with the second job and takes
    >>> # the fourth job from the list, and starts processing it immediately
    >>> # at time 2.
    >>> # 5. Finally, after 2 more seconds, thread 0 is done with the third job
    >>> # and takes the fifth job from the list, and starts processing it
    >>> # immediately at time 4.
    >>> job_queue = JobQueue()
    >>> job_queue.num_workers = 4
    >>> job_queue.jobs = [1] * 20
    >>> job_queue.assign_jobs()
    >>> job_queue.write_response()
    0 0
    1 0
    2 0
    3 0
    0 1
    1 1
    2 1
    3 1
    0 2
    1 2
    2 2
    3 2
    0 3
    1 3
    2 3
    3 3
    0 4
    1 4
    2 4
    3 4
    >>> # Explanation: Jobs are taken by 4 threads in packs of 4, processed in
    >>> # 1 second, and then the next pack comes. This happens 5 times starting
    >>> # at moments 0, 1, 2, 3 and 4. After that all the 5 × 4 = 20 jobs
    >>> # are processed.
    """

    def read_data(self):
        """Reads data from standard input."""
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = len(self.jobs)
        assert m == self.size

    def write_response(self):
        """Writes the response to standard output."""
        for worker_id, start_time in self.result:
            print(worker_id, start_time)

    def assign_jobs(self):
        """Assigns jobs to corresponding workers"""
        self.result = []
        self.worker_queue = [Worker(i) for i in range(self.num_workers)]

        for job in self.jobs:
            worker = heapq.heappop(self.worker_queue)

            self.result.append((worker.thread_id, worker.release_time))

            worker.release_time += job
            heapq.heappush(self.worker_queue, worker)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == "__main__":
    job_queue = JobQueue()
    job_queue.solve()

