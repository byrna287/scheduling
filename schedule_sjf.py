#!/usr/bin/env python3

def sort_on(task):
   return task[2]

def sjf(task_list):
   return sorted(task_list, key=sort_on)
