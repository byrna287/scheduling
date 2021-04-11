#!/usr/bin/env python3

# Ailbhe Byrne
# 19424402
# I acknowledge the DCU academic integrity policy

import os.path

# returns -1 if there's an error and 0 if no errors
def error_check(file, alg):
   if os.path.exists(file) == False:  # check if file exists so it can be read
      print("Error: file \"" + file + "\" does not exist")
      return -1

   elif alg not in ["fcfs", "sjf", "priority", "rr"]:  # check if the algorithm name is valid
      print("Error: invalid algorithm name \"" + alg + "\"")
      return -1

   return 0
