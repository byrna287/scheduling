#!/usr/bin/env python3

from schedule_fcfs import fcfs

def schedule(alg, tasks):
   if alg == "fcfs":
      tasks = fcfs(tasks)
      return tasks
