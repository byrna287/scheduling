#!/usr/bin/env python3

#[['P1', 4, 5], ['P2', 1, 3], ['P3', 2, 1], ['P4', 2, 7], ['P5', 3, 4]]

def run(task_list):
   time = 0
   for task in task_list:
      name, burst = task[0], task[2]
      print("process {} arrived at time {} and ran for {} MS".format(name, time, burst))
      time += burst
