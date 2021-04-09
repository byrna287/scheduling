#!/usr/bin/env python3

# makes a Gantt chart, [taskname, waittime, endtime]
# returns a list of processes and Gantt chart
def make_gantt(task_list):
   proc = []
   gantt = []
   wait_time = 0
   for task in task_list:
      if task[0] not in proc:    # makes a list of processes
         proc.append(task[0])
      g = [task[0], wait_time]   # makes list to be appended to gantt chart for each task
      wait_time += task[2]       # adds burst to wait time to get end time
      g.append(wait_time)        # adds end time to list
      gantt.append(g)            # adds task to gantt chart
   return proc, gantt
