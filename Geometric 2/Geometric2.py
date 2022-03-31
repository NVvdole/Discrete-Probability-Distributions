# File Name: Geometric2.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import geom

print("Geometric Distribution 2")
print("")
print("p = success probability")
print("y = failures")
print("")

p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
y = int(input("Enter y: "))
while y < 0:
    y = int(input("Enter y: "))
print("")

pmf = geom.pmf(y + 1, p)
cdf = geom.cdf(y + 1, p)
ccdf = geom.sf(y + 1, p)
mean = geom.mean(p) - 1.0
med = geom.median(p) - 1.0
var = geom.var(p)
std_dev = geom.std(p)
skew = geom.stats(p, moments = "s")
kurt = geom.stats(p, moments = "k")
ent = geom.entropy(p)

print("PMF, CDF, and CCDF")
print("pY(" + str(y) + ") = " + str(pmf))
print("FY(" + str(y) + ") = " + str(cdf))
print("FYc(" + str(y) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(Y) = " + str(mean))
print("Med(Y) = " + str(med))
print("Mode(Y) = 0.0")
print("")

print("Variance and Standard Deviation")
print("Var(Y) = " + str(var))
print("SD(Y) = " + str(std_dev))
print("")

print("Skewness and Kurtosis")
print("Skew(Y) = " + str(skew))
print("Kurt(Y) = " + str(kurt))
print("")

print("Entropy")
print("H(Y) = " + str(ent))
