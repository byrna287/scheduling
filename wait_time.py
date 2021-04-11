#!/usr/bin/env python3

# Ailbhe Byrne
# 19424402
# I acknowledge the DCU academic integrity policy

from gantt import make_gantt

# average wait time for fcfs, sjf and priority scheduling algorithms (non-preemptive)
def fcfs_sjf_pri_avg_wt(task_list):
   proc, gantt = make_gantt(task_list)
   total_wait = 0
   for task in gantt:
      total_wait += task[1]        # adds together all wait times in gantt chart
   return total_wait / len(proc)   # divide by number of processes

# average wait time for rr scheduling algorithm
def rr_avg_wt(task_list):
   proc, gantt = make_gantt(task_list)
   total_wait = 0
   for i in range(len(proc)):    # for each process
      p = proc[i]
      for j in range(len(gantt)):  # for each process in gantt chart
         if p == gantt[j][0]:      # match process to process in gantt chart
            if j >= len(proc):                           # if process has already been on cpu
               total_wait += gantt[j][1] - gantt[i][2]   # wait time = start time - end time of last time
               i = j                                     # i = last time process was on cpu
            else:
               total_wait += gantt[j][1]   # if first time on cpu, add wait time
   
         if j < len(gantt) - 1:
            if gantt[j][0] == gantt[j + 1][0]:   # if current process is same as next process
               break                             # exit loop as already have wait time

   return total_wait / len(proc)    # divide by number of processes

# print average waiting time for algorithm
def avg_wait_time(algorithm, tasks):
   if algorithm in ["fcfs", "sjf", "priority"]:
      print("Average waiting time: {:.3f} MS".format(fcfs_sjf_pri_avg_wt(tasks)))
   else:
      print("Average waiting time: {:.3f} MS".format(rr_avg_wt(tasks)))
