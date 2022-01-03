from collections import namedtuple

AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])


class JobQueue:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self.finish_time = []
        self.assigned_jobs = []
        for i in range(self.n):
            self.finish_time.append([i, 0])

    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.n:
            if self.finish_time[min_index][1] > self.finish_time[left][1]:
                min_index = left
            elif self.finish_time[min_index][1] == self.finish_time[left][1]:
                if self.finish_time[min_index][0] > self.finish_time[left][0]:
                    min_index = left
        if right < self.n:
            if self.finish_time[min_index][1] > self.finish_time[right][1]:
                min_index = right
            elif self.finish_time[min_index][1] == self.finish_time[right][1]:
                if self.finish_time[min_index][0] > self.finish_time[right][0]:
                    min_index = right
        if min_index != i:
            self.finish_time[i], self.finish_time[min_index] = self.finish_time[min_index], self.finish_time[i]
            self.SiftDown(min_index)

    def NextWorker(self, job):
        root = self.finish_time[0]
        next_worker = root[0]
        started_at = root[1]
        self.assigned_jobs.append(AssignedJob(next_worker,started_at))
        self.finish_time[0][1] += job
        self.SiftDown(0)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # test = "124860658 388437511 753484620 349021732 311346104 235543106 665655446 28787989 706718118 409836312 217716719 757274700 609723717 880970735 972393187 246159983 318988174 209495228 854708169 945600937 773832664 587887000 531713892 734781348 603087775 148283412 195634719 968633747 697254794 304163856 554172907 197744495 261204530 641309055 773073192 463418708 59676768 16042361 210106931 901997880 220470855 647104348 163515452 27308711 836338869 505101921 397086591 126041010 704685424 48832532 944295743 840261083 407178084 723373230 242749954 62738878 445028313 734727516 370425459 607137327 541789278 281002380 548695538 651178045 638430458 981678371 648753077 417312222 446493640 201544143 293197772 298610124 31821879 46071794 509690783 183827382 867731980 524516363 376504571 748818121 36366377 404131214 128632009 535716196 470711551 19833703 516847878 422344417 453049973 58419678 175133498 967886806 49897195 188342011 272087192 798530288 210486166 836411405 909200386 561566778"
    # jobs = list(map(int, test.split(' ')))
    # n_workers = 10

    job_queue = JobQueue(n_workers, jobs)
    for job in jobs:
        job_queue.NextWorker(job)
    assigned_jobs = job_queue.assigned_jobs


    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
