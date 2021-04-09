#!/usr/bin/env python3

# [taskname, priority, burst]
def sort_on(task):
   return task[1]

# returns tasks sorted in order of priority, highest first
def priority(task_list):
   return sorted(task_list, key=sort_on, reverse=True)
