#!/usr/bin/env python3

from scheduler import schedule
from CPU import run
from wait_time import avg_wait_time
from turnaround_time import avg_turnaround_time
from error_check import error_check

import sys
taskfile = sys.argv[1]
algorithm = sys.argv[2]

def main():
   error = error_check(taskfile, algorithm)
   if error == -1:
      sys.exit()

   with open(taskfile, "r") as file:
      tasks = file.read().strip().split("\n")

   for i in range(len(tasks)):
      tasks[i] = tasks[i].split()
      tasks[i][0] = tasks[i][0].strip(",")
      tasks[i][1] = int(tasks[i][1].strip(","))
      tasks[i][2] = int(tasks[i][2])

   tasks = schedule(algorithm, tasks)
   run(tasks)

   avg_wait_time(algorithm, tasks)
   avg_turnaround_time(algorithm, tasks)

if __name__ == '__main__':
   main()
