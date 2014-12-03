__author__ = 'Anton Rasmussen'

# Welch's t-test Exercise

import numpy
import scipy.stats
import pandas

filename = "baseball_data.csv"

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file via the following link:
    https://www.dropbox.com/s/xcn0u2uxm8c4n6l/baseball_data.csv

    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.

    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.

    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html

    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.

    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.

    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """

    # read csv into pandas data frame
    df = pandas.read_csv('baseball_data.csv')

       ## run Welch's t-test on two cohorts defined by handedness

    # Define the cohorts
    right_cohort = df[df['handedness'] == 'R']
    left_cohort = df[df['handedness'] == 'L']

    # create arrays for ttest
    avg_right = right_cohort['avg']
    avg_left = left_cohort['avg']

    # perform Welch's ttest
    Welch_ttest = scipy.stats.ttest_ind(avg_right,avg_left,equal_var = False)

    # output formmating -- if scores differ, i.e. we can reject the null, p-value must be less than 0.05

    if Welch_ttest[1] <= 0.05:
        print "(False,", Welch_ttest
        return (False, Welch_ttest)

    else:
        print "(True,", Welch_ttest
        return (True, Welch_ttest)




compare_averages(filename)