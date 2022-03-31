# File Name: Binomial.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import binom
import math

print("Binomial Distribution")
print("")
print("n = trials")
print("p = success probability")
print("x = successes")
print("")

n = int(input("Enter n: "))
while n < 0:
    n = int(input("Enter n: "))
    
p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
x = int(input("Enter x: "))
while x < 0 or x > n:
    x = int(input("Enter x: "))
print("")

pmf = binom.pmf(x, n, p)
cdf = binom.cdf(x, n, p)
ccdf = binom.sf(x, n, p)
mean = binom.mean(n, p)
med = binom.median(n, p)
mode = float(math.floor(p * (n + 1)))
var = binom.var(n, p)
std_dev = binom.std(n, p)
skew = binom.stats(n, p, moments = "s")
kurt = binom.stats(n, p, moments = "k")
ent = binom.entropy(n, p)

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
