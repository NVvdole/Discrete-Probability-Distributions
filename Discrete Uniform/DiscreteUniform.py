# File Name: DiscreteUniform.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

import math

print("Discrete Uniform Distribution")
print("")
print("v = values")
print("x = observed value")
print("")

v = int(input("Enter v: "))
while v < 1:
    v = int(input("Enter v: "))
    
x = int(input("Enter x: "))
while x < 1 or x > v:
    x = int(input("Enter x: "))
print("")

pmf = 1.0 / v
cdf = float(x) / v
ccdf = 1.0 - cdf
mean = (v + 1.0) / 2.0
med = (v + 1.0) / 2.0
var = (pow(v, 2) - 1.0) / 12.0
std_dev = math.sqrt(var)
kurt = -(6.0 * (pow(v, 2) + 1.0)) / (5.0 * (pow(v, 2) - 1.0))
ent = math.log(v)

print("PMF, CDF, and CCDF")
print("pX(" + str(x) + ") = " + str(pmf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = N/A")
print("")

print("Variance and Standard Deviation")
print("Var(X) = " + str(var))
print("SD(X) = " + str(std_dev))
print("")

print("Skewness and Kurtosis")
print("Skew(X) = 0.0")
print("Kurt(X) = " + str(kurt))
print("")

print("Entropy")
print("H(X) = " + str(ent))
