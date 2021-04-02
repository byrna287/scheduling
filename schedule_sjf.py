#!/usr/bin/env python3

#[['P1', 4, 5], ['P2', 1, 3], ['P3', 2, 1], ['P4', 2, 7], ['P5', 3, 4]]

def sort_on(task):
   return task[2]

def sjf(task_list):
   return sorted(task_list, key=sort_on)
