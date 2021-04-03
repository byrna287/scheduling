#!/usr/bin/env python3

def sort_on(task):
   return task[1]

def priority(task_list):
   return sorted(task_list, key=sort_on, reverse=True)
