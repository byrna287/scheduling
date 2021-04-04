#!/usr/bin/env python3

from scheduler import schedule
from CPU import run
from wait_time import avg_wait_time
from schedule_rr import rr_avg_wait_time

import sys
taskfile = sys.argv[1]
algorithm = sys.argv[2]

def main():
   with open(taskfile, "r") as file:
      tasks = file.read().strip().split("\n")

   for i in range(len(tasks)):
      tasks[i] = tasks[i].split()
      tasks[i][0] = tasks[i][0].strip(",")
      tasks[i][1] = int(tasks[i][1].strip(","))
      tasks[i][2] = int(tasks[i][2])

   tasks = schedule(algorithm, tasks)
   run(tasks)

   if algorithm in ["fcfs", "sjf", "priority"]:
      print("Average wait time: {:.4f} MS".format(avg_wait_time(tasks)))
   else:
      print(rr_avg_wait_time(tasks))

if __name__ == '__main__':
   main()
