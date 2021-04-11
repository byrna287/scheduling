#!/usr/bin/env python3

# Ailbhe Byrne
# 19424402
# I acknowledge the DCU academic integrity policy

# prints out the tasks after they've been sorted into order using a scheduling algorithm
def run(task_list):
   for task in task_list:
      name, burst = task[0], task[2]
      print("process {} arrived at time 0 and ran for {} MS".format(name, burst))
