#!/usr/bin/env python3

from schedule_fcfs import fcfs
from schedule_sjf import sjf
from schedule_priority import priority
from schedule_rr import rr

def schedule(alg, tasks):
   if alg == "fcfs":
      tasks = fcfs(tasks)
   elif alg == "sjf":
      tasks = sjf(tasks)
   elif alg == "priority":
      tasks = priority(tasks)
   elif alg =="rr":
      tasks = rr(tasks)

   return tasks
