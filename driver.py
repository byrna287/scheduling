#!/usr/bin/env python3

from scheduler import schedule
from CPU import run

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

if __name__ == '__main__':
   main()
