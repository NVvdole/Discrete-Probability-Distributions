# File Name: Hypergeometric.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import hypergeom
import math

print("Hypergeometric Distribution")
print("")
print("N = population size")
print("K = population successes")
print("n = draws")
print("x = successes")
print("")

N = int(input("Enter N: "))
while N < 0:
    N = int(input("Enter N: "))
    
K = int(input("Enter K: "))
while K < 0 or K > N:
    K = int(input("Enter K: "))
    
n = int(input("Enter n: "))
while n < 0 or n > N:
    n = int(input("Enter n: "))
    
x = int(input("Enter x: "))
while x < max(0, n + K - N) or x > min(n, K):
    x = int(input("Enter x: "))
print("")

pmf = hypergeom.pmf(x, N, K, n)
cdf = hypergeom.cdf(x, N, K, n)
ccdf = hypergeom.sf(x, N, K, n)
mean = hypergeom.mean(N, K, n)
med = hypergeom.median(N, K, n)
mode = float(math.floor(float((n + 1) * (K + 1)) / (N + 2)))
var = hypergeom.var(N, K, n)
std_dev = hypergeom.std(N, K, n)
skew = hypergeom.stats(N, K, n, moments = "s")
kurt = hypergeom.stats(N, K, n, moments = "k")
ent = hypergeom.entropy(N, K, n)

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
