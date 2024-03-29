#!/usr/bin/env python3

# Ailbhe Byrne
# 19424402
# I acknowledge the DCU academic integrity policy

# [taskname, priority, burst]
def sort_on(task):
   return task[2]

# returns tasks sorted in order of the length of cpu burst, lowest first
def sjf(task_list):
   return sorted(task_list, key=sort_on)
