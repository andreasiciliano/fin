# 2017-10-01
# Building financial model with Monte Carlo simulation of outcomes following
# the blueprint showed by Lars Krojers on his YouTube channel

import numpy
import random
from scipy.stats import norm


def portfolioRun(
    meanReturn,
    stdevReturn,
    years,
    initialContribution,
    growthInAnnualContribution,
    seedCapital,
    assetAllocation):
    
    startOfYear = []
    investmentReturn = []
    endOfYear = []
    yearlyReturns = []
    priorYear = seedCapital
    annualContribution = initialContribution
    for i in range(years):
        startOfYear.append(priorYear + annualContribution)
        yearlyReturn = [0.005, norm.ppf(random.random(), loc=meanReturn, scale=stdevReturn)]
        yearlyReturns.append(yearlyReturn)
        investmentReturn.append(startOfYear[i] * numpy.dot(assetAllocation, yearlyReturn))
        #investmentReturn.append(startOfYear[i] * (assetAllocation[0]* yearlyReturns[0] +
        #                                          assetAllocation[1]* yearlyReturns[1])
        #                        )
        endOfYear.append(startOfYear[i] + investmentReturn[i])

        priorYear = endOfYear[i]
        annualContribution = annualContribution * (1 + growthInAnnualContribution)
    return round(endOfYear[-1],2)

meanReturn = 0.05
stdevReturn = 0.25
years = 25
initialContribution = 4000
growthInAnnualContribution = 0.03
seedCapital = 0
assetAllocation = [0.5,   # Min Risk
              0.5   # Equities
              ]
endOfYear = []
for i in range(1000):
    endOfYear.append(portfolioRun(meanReturn, stdevReturn, years, initialContribution, growthInAnnualContribution, seedCapital, assetAllocation))
with open('out.txt', 'w') as f:
    for item in endOfYear:
        f.write('%s\n'% item)
