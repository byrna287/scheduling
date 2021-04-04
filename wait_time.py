#!/usr/bin/env python3

# average wait time for fcfs, sjf and priority scheduling algorithms (non-preemptive)

def avg_wait_time(task_list):
   total_wait = 0
   wait_each = 0
   for i in range(len(task_list) - 1):
      wait_each += task_list[i][2]
      total_wait += wait_each

   avg_wait = total_wait / len(task_list)
   return avg_wait
