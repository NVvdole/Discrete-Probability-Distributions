# File Name: Bernoulli.py
# Author: Verginia Mae Dole
# Date Created: 4/1/2022

from scipy.stats import bernoulli

print("Bernoulli Distribution")
print("")
print("p = success probability")
print("x = successes")
print("")

p = float(input("Enter p: "))
while p < 0.0 or p > 1.0:
    p = float(input("Enter p: "))
    
x = int(input("Enter x: "))
while x < 0 or x > 1:
    x = int(input("Enter x: "))
print("")

pmf = bernoulli.pmf(x, p)
cdf = bernoulli.cdf(x, p)
ccdf = bernoulli.sf(x, p)
mean = bernoulli.mean(p)
med = bernoulli.median(p)
var = bernoulli.var(p)
std_dev = bernoulli.std(p)
skew = bernoulli.stats(p, moments = "s")
kurt = bernoulli.stats(p, moments = "k")
ent = bernoulli.entropy(p)

print("PMF, CDF, and CCDF")
print("pX(" + str(x) + ") = " + str(pmf))
print("FX(" + str(x) + ") = " + str(cdf))
print("FXc(" + str(x) + ") = " + str(ccdf))
print("")

print("Mean, Median, and Mode")
print("E(X) = " + str(mean))
print("Med(X) = " + str(med))
if p < 0.5:
    print("Mode(X) = 0.0")
elif p == 0.5:
    print("Mode(X) = 0.0, 1.0")
else:
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