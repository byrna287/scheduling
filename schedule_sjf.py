#!/usr/bin/env python3

# [taskname, priority, burst]
def sort_on(task):
   return task[2]

# returns tasks sorted in order of the length of cpu burst, lowest first
def sjf(task_list):
   return sorted(task_list, key=sort_on)
