import numpy


def choose(n, k):
    result = numpy.math.factorial(n)/(numpy.math.factorial(k)*numpy.math.factorial(n-k))
    return result


def compute_mu_from_pmf(pmf):
    mu = 0
    for tup in pmf:
        mu += tup[0] * tup[1]
    return mu


def compute_variance_from_definition(pmf):
    mu = compute_mu_from_pmf(pmf)
    variance = 0
    for tup in pmf:
        variance += ((tup[0] - mu) ** 2) * tup[1]
    return variance


def compute_variance_from_shortcut(pmf):
    mu = compute_mu_from_pmf(pmf)
    expected_squared = 0
    for tup in pmf:
        expected_squared += (tup[0] ** 2) * tup[1]
    variance = expected_squared - mu ** 2
    return variance


def compute_standard_deviation(pmf):
    return numpy.sqrt(compute_variance_from_definition(pmf))


def binomial_random_variable_prob_exactly(x, n, p):
    # x is whatever number it needs to be
    # n is sample size
    # p is probability
    probability = choose(n, x)
    probability *= (p**x)
    probability *= (1-p)**(n-x)
    return probability


def binomial_random_variable_prob_at_least(x, n, p):
    probability = 0
    for i in range(x, n+1):
        probability+=binomial_random_variable_prob_exactly(i, n, p)
    return probability


def binomial_random_variable_prob_between(x, y, n, p):
    probability = 0
    for i in range(x, y+1):
        probability+=binomial_random_variable_prob_exactly(i, n, p)
    return probability


def binomial_random_variable_standard_deviation(n, p):
    return numpy.sqrt(n*p*(1-p))


def binomial_pmf(n, p):
    pmf = []
    for x in range(0, n+1):
        pmf +=[(x, binomial_random_variable_prob_exactly(x, n, p))]
    return pmf


def binomial_expected_value(n, p):
    return n*p


def main():
    # FUCK YOU PROB AND STAT, EAT MY PYTHON ASS
    ### input here ###
    n=20
    p=.1
    ##################
    pmf=binomial_pmf(n, p)
    print(binomial_random_variable_prob_between(0, 2, n, p))
    print(binomial_random_variable_prob_between(5, n, n, p))
    print(binomial_random_variable_prob_between(1, 4, n, p))
    print(binomial_random_variable_prob_exactly(0, n, p))
    print(compute_mu_from_pmf(pmf))
    print(compute_standard_deviation(pmf))

main()
