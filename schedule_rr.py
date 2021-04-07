#!/usr/bin/env python3

# [task, pri, burst]
# [['P1', 3, 2], ['P2', 1, 2], ['P3', 4, 2], ['P1', 3, 2], ['P2', 1, 1], ['P3', 4, 2], ['P3', 4, 1]]
# time quantum = 10 MS

# [['P1', 0], ['P2', 2], ['P3', 4], ['P1', 6], ['P2', 8], ['P3', 9], ['P3', 11]]

def make_gantt(task_list, ):
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

def rr(task_list):
   quantum = 4
   for task in task_list:
      if task[2] > quantum:
         taskcpy = task[:]
         taskcpy[2] -= quantum
         task_list.append(taskcpy)
         task[2] = quantum

   return task_list
