# File Name: NegativeHypergeometric.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import nhypergeom
import math

print("Negative Hypergeometric Distribution")
print("")
print("N = population size")
print("K = population successes")
print("r = failures")
print("x = successes")
print("")

N = int(input("Enter N: "))
while N < 0:
    N = int(input("Enter N: "))
    
K = int(input("Enter K: "))
while K < 0 or K > N:
    K = int(input("Enter K: "))
    
r = int(input("Enter r: "))
while r < 0 or r > N - K:
    r = int(input("Enter r: "))
    
x = int(input("Enter x: "))
while x < 0 or x > K:
    x = int(input("Enter x: "))
print("")

pmf = nhypergeom.pmf(x, N, K, r)
cdf = nhypergeom.cdf(x, N, K, r)
ccdf = nhypergeom.sf(x, N, K, r)
mean = nhypergeom.mean(N, K, r)
med = nhypergeom.median(N, K, r)
mode = float(math.floor(K * (float(r - 1) / (N - K - 1))))
var = nhypergeom.var(N, K, r)
std_dev = nhypergeom.std(N, K, r)
skew = nhypergeom.stats(N, K, r, moments = "s")
kurt = nhypergeom.stats(N, K, r, moments = "k")
ent = nhypergeom.entropy(N, K, r)

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
