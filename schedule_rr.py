#!/usr/bin/env python3

# [task, pri, burst]
# [['P1', 3, 2], ['P2', 1, 2], ['P3', 4, 2], ['P1', 3, 2], ['P2', 1, 1], ['P3', 4, 2], ['P3', 4, 1]]
# time quantum = 10 MS

def rr(task_list):
   quantum = 4
   for task in task_list:
      if task[2] > quantum:
         taskcpy = task[:]
         taskcpy[2] -= quantum
         task_list.append(taskcpy)
         task[2] = quantum

   return task_list
