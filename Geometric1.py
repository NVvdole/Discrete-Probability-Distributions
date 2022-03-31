# File Name: Geometric1.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import geom

print("Geometric Distribution 1")
print("")
print("p = success probability")
print("x = trials")
print("")

p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
x = int(input("Enter x: "))
while x < 1:
    x = int(input("Enter x: "))
print("")

pmf = geom.pmf(x, p)
cdf = geom.cdf(x, p)
ccdf = geom.sf(x, p)
mean = geom.mean(p)
med = geom.median(p)
var = geom.var(p)
std_dev = geom.std(p)
skew = geom.stats(p, moments = "s")
kurt = geom.stats(p, moments = "k")
ent = geom.entropy(p)

print("PMF, CDF, and CCDF")
print("pX(" + str(x) + ") = " + str(pmf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = 1.0")
print("")

print("Variance and Standard Deviation")
print("Var(X) = " + str(var))
print("SD(X) = " + str(std_dev))
print("")

print("Skewness and Kurtosis")
print("Skew(X) = " + str(skew))
print("Kurt(X) = " + str(kurt))
print("")

print("Entropy")
print("H(X) = " + str(ent))