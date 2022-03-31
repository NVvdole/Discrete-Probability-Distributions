# File Name: Poisson.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import poisson
import math

print("Poisson Distribution")
print("")
print("\u03BB = average rate of success")
print("x = successes")
print("")

lamb = float(input("Enter \u03BB: "))
while lamb <= 0.0:
    lamb = float(input("Enter \u03BB: "))
    
x = int(input("Enter x: "))
while x < 0:
    x = int(input("Enter x: "))
print("")

pmf = poisson.pmf(x, lamb)
cdf = poisson.cdf(x, lamb)
ccdf = poisson.sf(x, lamb)
mean = poisson.mean(lamb)
med = poisson.median(lamb)
mode = float(math.floor(lamb))
var = poisson.var(lamb)
std_dev = poisson.std(lamb)
skew = poisson.stats(lamb, moments = "s")
kurt = poisson.stats(lamb, moments = "k")
ent = poisson.entropy(lamb)

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
