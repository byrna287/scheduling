#!/usr/bin/env python3

def avg_wait_time(task_list):
   total_wait = 0
   wait_each = 0
   for i in range(len(task_list) - 1):
      wait_each += task_list[i][2]
      total_wait += wait_each

   avg_wait = total_wait / len(task_list)
   return avg_wait

def avg_turnaround_time(task_list):
   wait_time = 0
   total_turn_time = 0
   for task in task_list:
      total_turn_time += wait_time + task[2]
      wait_time += task[2]

   avg_turn_time = total_turn_time / len(task_list)
   return avg_turn_time

def fcfs(task_list):
   return task_list
