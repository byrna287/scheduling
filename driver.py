#!/usr/bin/env python3

# need to: answer the questions, run instructions

from error_check import error_check
from scheduler import schedule
from wait_time import avg_wait_time
from turnaround_time import avg_turnaround_time

import sys
taskfile = sys.argv[1]    # text file with tasks with format: taskname, priority, burst
algorithm = sys.argv[2]   # one of fcfs, sjf, priority, rr

def main():
   error = error_check(taskfile, algorithm)  # if an error is found, will print error message
   if error == -1:                           # exits the program if an error was found
      sys.exit()

   with open(taskfile, "r") as file:            # opens text file to read tasks
      tasks = file.read().strip().split("\n")   # put tasks in a list, splitting on new line

   for i in range(len(tasks)):
      tasks[i] = tasks[i].split()               # make each task in tasks a list 
      tasks[i][0] = tasks[i][0].strip(",")      # strip commas, change numbers to ints
      tasks[i][1] = int(tasks[i][1].strip(","))
      tasks[i][2] = int(tasks[i][2])

   tasks = schedule(algorithm, tasks)           # call scheduler on tasks using algorithm
   avg_wait_time(algorithm, tasks)              # get average wait time
   avg_turnaround_time(algorithm, tasks)        # get average turnaround time

if __name__ == '__main__':
   main()
