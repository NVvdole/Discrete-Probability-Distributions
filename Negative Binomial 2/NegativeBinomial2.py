# File Name: NegativeBinomial2.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import nbinom
import math

print("Negative Binomial Distribution 2")
print("")
print("k = successes")
print("p = success probability")
print("y = failures")
print("")

k = int(input("Enter k: "))
while k < 1:
    k = int(input("Enter k: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
y = int(input("Enter y: "))
while y < 0:
    y = int(input("Enter y: "))
print("")

pmf = nbinom.pmf(y, k, p)
cdf = nbinom.cdf(y, k, p)
ccdf = nbinom.sf(y, k, p)
mean = nbinom.mean(k, p)
med = nbinom.median(k, p)
mode = float(math.floor(((1.0 - p) * (k - 1)) / p))
var = nbinom.var(k, p)
std_dev = nbinom.std(k, p)
skew = nbinom.stats(k, p, moments = "s")
kurt = nbinom.stats(k, p, moments = "k")
ent = nbinom.entropy(k, p)

print("PMF, CDF, and CCDF")
print("pY(" + str(y) + ") = " + str(pmf))
print("FY(" + str(y) + ") = " + str(cdf))
print("FYc(" + str(y) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(Y) = " + str(mean))
print("Med(Y) = " + str(med))
print("Mode(Y) = " + str(mode))
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
