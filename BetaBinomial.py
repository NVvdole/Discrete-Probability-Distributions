# File Name: BetaBinomial.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import betabinom
import math

print("Beta-Binomial Distribution")
print("")
print("n = trials")
print("\u03B11 = first shape parameter")
print("\u03B12 = second shape parameter")
print("x = successes")
print("")

n = int(input("Enter n: "))
while n < 0:
    n = int(input("Enter n: "))
    
alpha1 = float(input("Enter \u03B11: "))
while alpha1 <= 0.0:
    alpha1 = float(input("Enter \u03B11: "))
    
alpha2 = float(input("Enter \u03B12: "))
while alpha2 <= 0.0:
    alpha2 = float(input("Enter \u03B12: "))
    
x = int(input("Enter x: "))
while x < 0 or x > n:
    x = int(input("Enter x: "))
print("")

pmf = betabinom.pmf(x, n, alpha1, alpha2)
cdf = betabinom.cdf(x, n, alpha1, alpha2)
ccdf = betabinom.sf(x, n, alpha1, alpha2)
mean = betabinom.mean(n, alpha1, alpha2)
med = betabinom.median(n, alpha1, alpha2)
mode = float(math.floor(n * ((alpha1 - 1.0) / (alpha1 + alpha2 - 2.0))))
var = betabinom.var(n, alpha1, alpha2)
std_dev = betabinom.std(n, alpha1, alpha2)
skew = betabinom.stats(n, alpha1, alpha2, moments = "s")
kurt = betabinom.stats(n, alpha1, alpha2, moments = "k")
ent = betabinom.entropy(n, alpha1, alpha2)

print("PMF, CDF, and CCDF")
print("pX(" + str(x) + ") = " + str(pmf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if alpha1 > 1.0 and alpha2 > 1.0:
    print("Mode(X) = " + str(mode))
elif alpha1 < 1.0 and alpha2 < 1.0:
    print("Mode(X) = 0.0, " + str(float(n)))
elif alpha1 <= 1.0 and alpha2 > 1.0:
    print("Mode(X) = 0.0")
elif alpha1 > 1.0 and alpha2 <= 1.0:
    print("Mode(X) = " + str(float(n)))
else:
    print("Mode(X) = N/A")
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