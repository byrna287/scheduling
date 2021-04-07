#!/usr/bin/env python3

from schedule_rr import make_gantt

# average turnaround time for fcfs, sjf and priority scheduling algorithms (non preemptive)
def fcfs_sjf_pri_avg_tt(task_list):
   wait_time = 0
   total_turn_time = 0
   for task in task_list:
      total_turn_time += wait_time + task[2]  # turnaround time = wait time + burst time
      wait_time += task[2]

   avg_turn_time = total_turn_time / len(task_list)
   return avg_turn_time

# average turnaround time for rr scheduling algorithm
def rr_avg_tt(task_list):
   proc, gantt = make_gantt(task_list)
   total_turn_time = 0
   for p in proc:
      for j in gantt[::-1]:
         if j[0] == p:
            total_turn_time += j[2]  # turnaround time = completion time - arrival time(0)
            break
   return total_turn_time / len(proc)

# print average turnaround time for algorithm
def avg_turnaround_time(algorithm, tasks):
   if algorithm in ["fcfs", "sjf", "priority"]:
      print("Average turnaround time: {:.3f} MS".format(fcfs_sjf_pri_avg_tt(tasks)))
   else:
      print("Average turnaround time: {:.3f} MS".format(rr_avg_tt(tasks)))
