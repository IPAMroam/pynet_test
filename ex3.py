#! /usr/bin/env python

a_var = "Name 1"
b_var = "Name 2"
c_var = "Name 3"

print "{:>30} {:>30} {:>30}".format(a_var,b_var,c_var)

d_var = raw_input("What is the IP address:  ")

ips = d_var.split(".")

print "{:<12}".format(ips)
print "{:<12} {:<12} {:<12} {:<12}".format(ips[0],ips[1],ips[2],ips[3])
