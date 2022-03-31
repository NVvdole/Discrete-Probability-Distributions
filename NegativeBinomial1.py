# File Name: NegativeBinomial1.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import nbinom
import math

print("Negative Binomial Distribution 1")
print("")
print("k = successes")
print("p = success probability")
print("x = trials")
print("")

k = int(input("Enter k: "))
while k < 1:
    k = int(input("Enter k: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
x = int(input("Enter x: "))
while x < k:
    x = int(input("Enter x: "))
print("")

pmf = nbinom.pmf(x - k, k, p)
cdf = nbinom.cdf(x - k, k, p)
ccdf = nbinom.sf(x - k, k, p)
mean = nbinom.mean(k, p) + k
med = nbinom.median(k, p) + k
mode = float(math.floor(((1.0 - p) * (k - 1)) / p)) + k
var = nbinom.var(k, p)
std_dev = nbinom.std(k, p)
skew = nbinom.stats(k, p, moments = "s")
kurt = nbinom.stats(k, p, moments = "k")
ent = nbinom.entropy(k, p)

print("PMF, CDF, and CCDF")
print("pX(" + str(x) + ") = " + str(pmf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
print("Mode(X) = " + str(mode))
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