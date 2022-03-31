# File Name: MultivariateHypergeometric.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import multivariate_hypergeom
from scipy.stats import hypergeom
import math

print("Multivariate Hypergeometric Distribution")
print("")
print("N = population size")
print("K1 = Category 1 population successes")
print("K2 = Category 2 population successes")
print("K3 = Category 3 population successes")
print("n = draws")
print("x1 = Category 1 successes")
print("x2 = Category 2 successes")
print("x3 = Category 3 successes")
print("")

N = int(input("Enter N: "))
while N < 0:
    N = int(input("Enter N: "))
    
K = []
temp = int(input("Enter K1: "))
while temp < 0 or temp > N:
    temp = int(input("Enter K1: "))
K.append(temp)
temp = int(input("Enter K2: "))
while temp < 0 or temp > N - K[0]:
    temp = int(input("Enter K2: "))
K.append(temp)
temp = int(input("Enter K3: "))
while temp < 0 or temp > N - K[0] - K[1]:
    temp = int(input("Enter K3: "))
K.append(temp)

n = int(input("Enter n: "))
while n < 0 or n > N:
    n = int(input("Enter n: "))

x = []
temp = int(input("Enter x1: "))
while temp < 0 or temp > n or temp > K[0]:
    temp = int(input("Enter x1: "))
x.append(temp)
temp = int(input("Enter x2: "))
while temp < 0 or temp > n - x[0] or temp > K[1]:
    temp = int(input("Enter x2: "))
x.append(temp)
temp = int(input("Enter x3: "))
while temp < 0 or temp > n - x[0] - x[1] or temp > K[2]:
    temp = int(input("Enter x3: "))
x.append(temp)
print("")

jpmf = multivariate_hypergeom.pmf(x, K, n)
mpmf1 = hypergeom.pmf(x[0], N, K[0], n)
mpmf2 = hypergeom.pmf(x[1], N, K[1], n)
mpmf3 = hypergeom.pmf(x[2], N, K[2], n)

mcdf1 = hypergeom.cdf(x[0], N, K[0], n)
mcdf2 = hypergeom.cdf(x[1], N, K[1], n)
mcdf3 = hypergeom.cdf(x[2], N, K[2], n)

mccdf1 = hypergeom.sf(x[0], N, K[0], n)
mccdf2 = hypergeom.sf(x[1], N, K[1], n)
mccdf3 = hypergeom.sf(x[2], N, K[2], n)

mean1 = hypergeom.mean(N, K[0], n)
mean2 = hypergeom.mean(N, K[1], n)
mean3 = hypergeom.mean(N, K[2], n)

med1 = hypergeom.median(N, K[0], n)
med2 = hypergeom.median(N, K[1], n)
med3 = hypergeom.median(N, K[2], n)

mode1 = float(math.floor(float((n + 1) * (K[0] + 1)) / (N + 2)))
mode2 = float(math.floor(float((n + 1) * (K[1] + 1)) / (N + 2)))
mode3 = float(math.floor(float((n + 1) * (K[2] + 1)) / (N + 2)))

var1 = hypergeom.var(N, K[0], n)
var2 = hypergeom.var(N, K[1], n)
var3 = hypergeom.var(N, K[2], n)

std_dev1 = hypergeom.std(N, K[0], n)
std_dev2 = hypergeom.std(N, K[1], n)
std_dev3 = hypergeom.std(N, K[2], n)

skew1 = hypergeom.stats(N, K[0], n, moments = "s")
skew2 = hypergeom.stats(N, K[1], n, moments = "s")
skew3 = hypergeom.stats(N, K[2], n, moments = "s")

kurt1 = hypergeom.stats(N, K[0], n, moments = "k")
kurt2 = hypergeom.stats(N, K[1], n, moments = "k")
kurt3 = hypergeom.stats(N, K[2], n, moments = "k")

ent1 = hypergeom.entropy(N, K[0], n)
ent2 = hypergeom.entropy(N, K[1], n)
ent3 = hypergeom.entropy(N, K[2], n)

cov1 = -(n * (float(N - n) / (N - 1.0)) * (float(K[0]) / N) * (float(K[1]) / N))
cov2 = -(n * (float(N - n) / (N - 1.0)) * (float(K[0]) / N) * (float(K[2]) / N))
cov3 = -(n * (float(N - n) / (N - 1.0)) * (float(K[1]) / N) * (float(K[2]) / N))

corr1 = cov1 / (std_dev1 * std_dev2)
corr2 = cov2 / (std_dev1 * std_dev3)
corr3 = cov3 / (std_dev2 * std_dev3)

print("PMFs")
print("pX1,X2,X3(" + str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ") = " + str(jpmf))
print("pX1(" + str(x[0]) + ") = " + str(mpmf1))
print("pX2(" + str(x[1]) + ") = " + str(mpmf2))
print("pX3(" + str(x[2]) + ") = " + str(mpmf3))
print("")

print("CDFs")
print("FX1(" + str(x[0]) + ") = " + str(mcdf1))
print("FX2(" + str(x[1]) + ") = " + str(mcdf2))
print("FX3(" + str(x[2]) + ") = " + str(mcdf3))
print("")

print("CCDFs")
print("FX1c(" + str(x[0]) + ") = " + str(mccdf1))
print("FX2c(" + str(x[1]) + ") = " + str(mccdf2))
print("FX3c(" + str(x[2]) + ") = " + str(mccdf3))
print("")

print("Means")
print("E(X1) = " + str(mean1))
print("E(X2) = " + str(mean2))
print("E(X3) = " + str(mean3))
print("")

print("Medians")
print("Med(X1) = " + str(med1))
print("Med(X2) = " + str(med2))
print("Med(X3) = " + str(med3))
print("")

print("Modes")
print("Mode(X1) = " + str(mode1))
print("Mode(X2) = " + str(mode2))
print("Mode(X3) = " + str(mode3))
print("")

print("Variances")
print("Var(X1) = " + str(var1))
print("Var(X2) = " + str(var2))
print("Var(X3) = " + str(var3))
print("")

print("Standard Deviations")
print("SD(X1) = " + str(std_dev1))
print("SD(X2) = " + str(std_dev2))
print("SD(X3) = " + str(std_dev3))
print("")

print("Skewnesses")
print("Skew(X1) = " + str(skew1))
print("Skew(X2) = " + str(skew2))
print("Skew(X3) = " + str(skew3))
print("")

print("Kurtoses")
print("Kurt(X1) = " + str(kurt1))
print("Kurt(X2) = " + str(kurt2))
print("Kurt(X3) = " + str(kurt3))
print("")

print("Entropies")
print("H(X1) = " + str(ent1))
print("H(X2) = " + str(ent2))
print("H(X3) = " + str(ent3))
print("")

print("Covariances")
print("Cov(X1, X2) = " + str(cov1))
print("Cov(X1, X3) = " + str(cov2))
print("Cov(X2, X3) = " + str(cov3))
print("")

print("Correlation Coefficients")
print("Corr(X1, X2) = " + str(corr1))
print("Corr(X1, X3) = " + str(corr2))
print("Corr(X2, X3) = " + str(corr3))
