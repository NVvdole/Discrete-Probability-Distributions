# File Name: Logarithmic.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import logser

print("Logarithmic Distribution")
print("")
print("p = success probability")
print("x = successes")
print("")

p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
x = int(input("Enter x: "))
while x < 1:
    x = int(input("Enter x: "))
print("")

pmf = logser.pmf(x, p)
cdf = logser.cdf(x, p)
ccdf = logser.sf(x, p)
mean = logser.mean(p)
med = logser.median(p)
var = logser.var(p)
std_dev = logser.std(p)
skew = logser.stats(p, moments = "s")
kurt = logser.stats(p, moments = "k")
ent = logser.entropy(p)

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