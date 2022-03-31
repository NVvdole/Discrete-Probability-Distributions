# File Name: Multinomial.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import multinomial
from scipy.stats import binom
import math

print("Multinomial Distribution")
print("")
print("n = trials")
print("p1 = Category 1 success probability")
print("p2 = Category 2 success probability")
print("p3 = Category 3 success probability")
print("x1 = Category 1 successes")
print("x2 = Category 2 successes")
print("x3 = Category 3 successes")
print("")

n = int(input("Enter n: "))
while n < 0:
    n = int(input("Enter n: "))
    
p = []
temp = float(input("Enter p1: "))
while temp < 0.0 or temp > 1.0:
    temp = float(input("Enter p1: "))
p.append(temp)
temp = float(input("Enter p2: "))
while temp < 0.0 or temp > 1.0 - p[0]:
    temp = float(input("Enter p2: "))
p.append(temp)
temp = float(input("Enter p3: "))
while temp < 0.0 or temp > 1.0 - p[0] - p[1]:
    temp = float(input("Enter p3: "))
p.append(temp)

x = []
temp = int(input("Enter x1: "))
while temp < 0 or temp > n:
    temp = int(input("Enter x1: "))
x.append(temp)
temp = int(input("Enter x2: "))
while temp < 0 or temp > n - x[0]:
    temp = int(input("Enter x2: "))
x.append(temp)
temp = int(input("Enter x3: "))
while temp < 0 or temp > n - x[0] - x[1]:
    temp = int(input("Enter x3: "))
x.append(temp)
print("")

jpmf = multinomial.pmf(x, n, p)
mpmf1 = binom.pmf(x[0], n, p[0])
mpmf2 = binom.pmf(x[1], n, p[1])
mpmf3 = binom.pmf(x[2], n, p[2])

mcdf1 = binom.cdf(x[0], n, p[0])
mcdf2 = binom.cdf(x[1], n, p[1])
mcdf3 = binom.cdf(x[2], n, p[2])

mccdf1 = binom.sf(x[0], n, p[0])
mccdf2 = binom.sf(x[1], n, p[1])
mccdf3 = binom.sf(x[2], n, p[2])

mean1 = binom.mean(n, p[0])
mean2 = binom.mean(n, p[1])
mean3 = binom.mean(n, p[2])

med1 = binom.median(n, p[0])
med2 = binom.median(n, p[1])
med3 = binom.median(n, p[2])

mode1 = float(math.floor(p[0] * (n + 1)))
mode2 = float(math.floor(p[1] * (n + 1)))
mode3 = float(math.floor(p[2] * (n + 1)))

var1 = binom.var(n, p[0])
var2 = binom.var(n, p[1])
var3 = binom.var(n, p[2])

std_dev1 = binom.std(n, p[0])
std_dev2 = binom.std(n, p[1])
std_dev3 = binom.std(n, p[2])

skew1 = binom.stats(n, p[0], moments = "s")
skew2 = binom.stats(n, p[1], moments = "s")
skew3 = binom.stats(n, p[2], moments = "s")

kurt1 = binom.stats(n, p[0], moments = "k")
kurt2 = binom.stats(n, p[1], moments = "k")
kurt3 = binom.stats(n, p[2], moments = "k")

ent1 = binom.entropy(n, p[0])
ent2 = binom.entropy(n, p[1])
ent3 = binom.entropy(n, p[2])

cov1 = -(n * p[0] * p[1])
cov2 = -(n * p[0] * p[2])
cov3 = -(n * p[1] * p[2])

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
