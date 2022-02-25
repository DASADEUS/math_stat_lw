# -*- coding: utf-8 -*-

from statistics import mean
from statistics import median
from statistics import harmonic_mean
import numpy as np
import statistics
import re
from scipy.stats import norm
import plotly.graph_objects as go  
def harmonic_mean(x):
    return len(x)/sum(1/x)
def geom_mean(x):
    return np.prod(x**(1/len(x)))
def F_n(x,sample):
    return len(sample[sample <= x])/len(sample)
import statsmodels.api as sm
from scipy.stats import binom, randint, geom, bernoulli,expon,poisson,uniform
from math import sqrt,factorial

"""# 1"""

student = np.array([0, 97, 97, 82, 90, 100, 86, 64, 79, 97, 44, 67, 76, 94, 98, 70, 88, 76, 54, 79, 68, 24, 80, 82, 54])
def task_1(sample):
    mean_student = np.mean(sample[sample > 0])
    median_student = np.median(sample[sample > 0])
    harmonic_mean_student = harmonic_mean(sample[sample >= median_student])
    geom_mean_student = geom_mean(sample[sample >= median_student])
    best_median_student = np.median(sample[sample >= median_student])
    good_students = len(sample[((sample <= best_median_student )& (sample >= harmonic_mean_student) |
                                 (sample >= best_median_student )& (sample <= harmonic_mean_student))])
    print(f"Средняя положительная оценка A = {round(mean_student,1)}")
    print(f"Медиана положительных оценок M = {round(median_student,1)}")
    print(f"Средне гармоническое H = {round(harmonic_mean_student,1)}")
    print(f"Средне геометрическое G = {round(geom_mean_student,1)}")
    print(f"Медианная оценка в лучшей части группы = {round(best_median_student,1)}")
    print(f"количество студентов, оценки которых оказались между H и Q = {good_students}")
    print()
    
task_1(student)

"""# 2"""

pd= np.array([-44, 52, 125, 100, -357, 43, -135, -83, -133, -156, -77, -243, -208, 16, 161, 194, -292, 528, 17, 77, -377, -75, -348, -305, 304, 286, 77, -111, 6, -118, -21, -91, 92, -217, 236, 24])
def task_2(sample):
    mean_pd = np.mean(sample)
    std_pd = np.std(sample)
    PD = norm(mean_pd,std_pd)
    L = PD.ppf(0.25)
    H = PD.ppf(0.75)
    pd_interval = len(sample[(sample <= H )& (sample >= L)])
    d = max(np.abs([F_n(x,sample) for x in sorted(sample)] - PD.cdf(sorted(sample)))) 
    
    print(f"Среднее арифметическое ПД = {round(mean_pd,1)}")
    print(f"Эмпирическое стандартное отклонение ПД = {round(std_pd,1)}")
    print(f"Квартиль L = {round(L,1)}; квартиль Н = {round(H,1)}")
    print(f"Количество ПД, попавших в интервал от L до H = {round(pd_interval,1)}")
    ecdf = sm.distributions.ECDF(sample,side = 'left')
    x = sorted(sample)#np.linspace(min(sample),max(sample))
    y_cdf_empir = ecdf(x)
    y_cdf = PD.cdf(x)
    print(f"Расстояние между функциями распределений = {round(d,3)}")
    
task_2(pd)

"""# 3"""

x = [61, 65, 89, 34, 80, 41, 77, 71, 100, 73, 78, 88, 73, 99, 71, 62, 68, 98, 61, 37, 55, 46, 79, 38, 47, 55, 88, 77]
y = [51, 49, 67, 31, 76, 39, 94, 61, 80, 63, 66, 82, 68, 97, 70, 40, 82, 91, 60, 46, 46, 56, 76, 31, 38, 75, 77, 62]

v = [x[i] for i in range(len(x)) if x[i] >= 50 and y[i] >= 50]
u = [y[i] for i in range(len(y)) if x[i] >= 50 and y[i] >= 50]

a = round(np.cov(v, u, bias = True)[0,1],2)
b = round(np.corrcoef(v, u)[0,1],3)
print(a, b)

"""# 4"""

n = [20, 24, 26]
x = [76, 77, 75]
s = [7, 5, 4]

a = [x[i]*n[i] for i in range(len(n))]
r = (a[0] + a[1] + a[2])/(n[0] + n[1] + n[2]) 

M_0 = s[0]**2+x[0]**2
M_1 = s[1]**2+x[1]**2
M_2 = s[2]**2+x[2]**2
M = (M_0*n[0]+M_1*n[1]+M_2*n[2])/(n[0] + n[1] + n[2]) 
s_0 = (M_012 - r**2)**(1/2)
print(round(r,1), round(s_0,3))