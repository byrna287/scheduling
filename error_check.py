#!/usr/bin/env python3

import os.path

def error_check(file, alg):
   if os.path.exists(file) == False:
      print("Error: the file \"" + file + "\" does not exist")
      return -1

   elif alg not in ["fcfs", "sjf", "priority", "rr"]:
      print("Error: invalid algorithm name \"" + alg + "\"")
      return -1

   return 0
