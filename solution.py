import pandas as pd
import numpy as np
from math import sqrt
import scipy.stats

chat_id = 704471350

def solution(p: float, x: np.array) -> tuple:
    alpha = 1-p
    z1 = scipy.stats.chi2.ppf(alpha/2, df=2*len(x))
    z2 = scipy.stats.chi2.ppf((1-alpha)/2, df=2*len(x))

    r = np.power(x,2)

    z_end = sqrt( sum(r)/(z1*37) )
    z_begin = sqrt( sum(r)/(z2*37) )
    return z_begin, z_end
