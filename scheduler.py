#!/usr/bin/env python3

from schedule_fcfs import fcfs
from schedule_sjf import sjf

def schedule(alg, tasks):
   if alg == "fcfs":
      tasks = fcfs(tasks)
   elif alg == "sjf":
      tasks = sjf(tasks)

   return tasks