#!/usr/bin/env python3

# [task, pri, burst]
# [['P1', 3, 2], ['P2', 1, 2], ['P3', 4, 2], ['P1', 3, 2], ['P2', 1, 1], ['P3', 4, 2], ['P3', 4, 1]]
# time quantum = 10 MS

# [['P1', 0], ['P2', 2], ['P3', 4], ['P1', 6], ['P2', 8], ['P3', 9], ['P3', 11]]

def rr_avg_wait_time(task_list):
   proc = []
   gantt = []
   wait_time = 0
   for task in task_list:
      if task[0] not in proc:
         proc.append(task[0])
      gantt.append([task[0], wait_time])
      wait_time += task[2]

   print(gantt)
   total_wait = 0
   i = 0
   for i in range(len(proc)):
      p = proc[i]
      for j in range(len(gantt)):
         if p == gantt[j][0]:
            if j >= len(proc):
               total_wait += gantt[j][1] - gantt[i + 1][1]
               i = j
            else:
               total_wait += gantt[j][1]
   
         if j < len(gantt) - 1:
            if gantt[j][0] == gantt[j + 1][0]:
               break

   return total_wait / len(proc)


def rr(task_list):
   quantum = 10
   for task in task_list:
      if task[2] > quantum:
         taskcpy = task[:]
         taskcpy[2] -= quantum
         task_list.append(taskcpy)
         task[2] = quantum

   return task_list
