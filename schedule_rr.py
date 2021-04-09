#!/usr/bin/env python3

# [taskname, priority, burst]
# time quantum = 10 MS

# returns tasks sorted in order they came in, except when cpu burst is higher than the time quantum
# tasks go to back of list after one time quantum
def rr(task_list):
   quantum = 10
   for task in task_list:
      if task[2] > quantum:
         taskcpy = task[:]
         taskcpy[2] -= quantum
         task_list.append(taskcpy)
         task[2] = quantum

   return task_list
