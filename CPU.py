#!/usr/bin/env python3

# prints out the tasks after they've been sorted into order using a scheduling algorithm
def run(task_list):
   for task in task_list:
      name, burst = task[0], task[2]
      print("process {} arrived at time 0 and ran for {} MS".format(name, burst))
