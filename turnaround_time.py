#!/usr/bin/env python3

from gantt import make_gantt

# average turnaround time for fcfs, sjf and priority scheduling algorithms (non preemptive)
def fcfs_sjf_pri_avg_tt(task_list):
   proc, gantt = make_gantt(task_list)
   total_turn_time = 0
   for task in gantt:
      total_turn_time += task[2]       # turnaround time = completion time - arrival time(0)
   return total_turn_time / len(proc)  # divide by number of processes

# average turnaround time for rr scheduling algorithm
def rr_avg_tt(task_list):
   proc, gantt = make_gantt(task_list)
   total_turn_time = 0
   for p in proc:                # for each process
      for task in gantt[::-1]:   # backwards through gantt chart
         if task[0] == p:               # match process
            total_turn_time += task[2]  # turnaround time = completion time - arrival time(0)
            break                       # break as only need completion time of last time process in cpu
   return total_turn_time / len(proc)   # divide by number of processes

# print average turnaround time for algorithm
def avg_turnaround_time(algorithm, tasks):
   if algorithm in ["fcfs", "sjf", "priority"]:
      print("Average turnaround time: {:.3f} MS".format(fcfs_sjf_pri_avg_tt(tasks)))
   else:
      print("Average turnaround time: {:.3f} MS".format(rr_avg_tt(tasks)))
