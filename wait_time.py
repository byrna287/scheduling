#!/usr/bin/env python3

from gantt import make_gantt

# average wait time for fcfs, sjf and priority scheduling algorithms (non-preemptive)
def fcfs_sjf_pri_avg_wt(task_list):
   proc, gantt = make_gantt(task_list)
   total_wait = 0
   for task in gantt:
      total_wait += task[1]
   return total_wait / len(proc)

# average wait time for rr scheduling algorithm
def rr_avg_wt(task_list):
   proc, gantt = make_gantt(task_list)
   total_wait = 0
   for i in range(len(proc)):
      p = proc[i]
      for j in range(len(gantt)):
         if p == gantt[j][0]:
            if j >= len(proc):
               total_wait += gantt[j][1] - gantt[i][2]
               i = j
            else:
               total_wait += gantt[j][1]
   
         if j < len(gantt) - 1:
            if gantt[j][0] == gantt[j + 1][0]:
               break

   return total_wait / len(proc)

# print average waiting time for algorithm
def avg_wait_time(algorithm, tasks):
   if algorithm in ["fcfs", "sjf", "priority"]:
      print("Average wait time: {:.3f} MS".format(fcfs_sjf_pri_avg_wt(tasks)))
   else:
      print("Average wait time: {:.3f} MS".format(rr_avg_wt(tasks)))
