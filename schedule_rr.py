#!/usr/bin/env python3

#[task, pri, burst]
#[['P1', 4, 13], ['P2', 1, 8], ['P3', 2, 15], ['P4', 2, 27], ['P5', 3, 14]]
# time quantum = 10 MS

def rr(task_list):
   quantum = 10
   for task in task_list:
      if task[2] > quantum:
         taskcpy = task[:]
         taskcpy[2] -= quantum
         task_list.append(taskcpy)
         task[2] = quantum

   return task_list
