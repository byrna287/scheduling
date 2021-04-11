#!/usr/bin/env python3

# Ailbhe Byrne
# 19424402
# I acknowledge the DCU academic integrity policy

from schedule_fcfs import fcfs
from schedule_sjf import sjf
from schedule_priority import priority
from schedule_rr import rr
from CPU import run

# call correct scheduling algorithm on tasks
def schedule(alg, tasks):
   if alg == "fcfs":
      tasks = fcfs(tasks)
   elif alg == "sjf":
      tasks = sjf(tasks)
   elif alg == "priority":
      tasks = priority(tasks)
   elif alg =="rr":
      tasks = rr(tasks)

   run(tasks)     # prints out the tasks in correct order
   return tasks
