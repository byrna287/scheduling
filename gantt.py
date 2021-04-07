#!/usr/bin/env python3

def make_gantt(task_list):
   proc = []
   gantt = []
   wait_time = 0
   for task in task_list:
      if task[0] not in proc:
         proc.append(task[0])
      g = [task[0], wait_time]
      wait_time += task[2]
      g.append(wait_time)
      gantt.append(g)
   return proc, gantt
