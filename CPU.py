#!/usr/bin/env python3

def run(task_list):
   time = 0
   for task in task_list:
      name, burst = task[0], task[2]
      print("process {} arrived at time {} and ran for {} MS".format(name, time, burst))
      time += burst
