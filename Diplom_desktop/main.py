import os
from time import sleep, time
import threading
import psutil
import datetime


    # for process in psutil.process_iter():
    #     # print(process)
    #     if process.name() == 'calc.exe':
    #         process.kill()
    #     sleep(1)
process={}
for p in psutil.process_iter():
    print(str(p))
    st = str(p).find("started=")
    if st != -1:
        st = str(p)[st:-1]
        process[str(p.name())] = st
print(process)
# for k, t in process.items():
#     print(k, " : ", t)
# process = dict(process)
# process = sorted(process.items(), key=lambda x: x[1])

# p = psutil.Process()
# for p in psutil.process_iter():
#     print(p.name(),  # execute internal routine once collecting multiple info
#     # p.cpu_times(),  # return cached value
#     p.cpu_percent(),  # return cached value
#     p.create_time(),  # return cached value
#     p.ppid(),  # return cached value
#     p.status(),)  # return cached value
# print(psutil.pids())
# print(psutil.Process(408))



# pids = psutil.get_pid_list()
# ps_list=psutil.get_pid_list()

# pids = psutil.process_iter()
# procs = []
# for pid in pids:
#     print(pid)
    # p = psutil.Process(pid)
    # new_proc = psutil.Process(p.name,
                       # str(p.pid),
                       # p.exe,
                       # p.username,
                       # str(p.get_cpu_percent()),
                       # str(p.get_memory_percent())
    #                    )
    # procs.append(new_proc)