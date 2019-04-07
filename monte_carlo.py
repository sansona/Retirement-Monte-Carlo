import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
# ----------------- .txt files with historical performance---------------------
SP500_FILE = 'SP500_returns_1926-2013_pct.txt'
TEN_YR_TBOND_FILE = '10-yr_TBond_returns_1926-2013_pct.txt'
AVG_RETURN_FILE = '_stock_returns_1926-2013_pct.txt'

# -----------------------------------------------------------------------------


def load_data(fname):
    ''' returns list of chronological returns from .txt '''
    with open(fname, 'r') as f:
        data = []
        for line in f:
            data.append(float(line.rstrip('\n')))
    return data

# -----------------------------------------------------------------------------


def generate_avg_returns(perc_stocks):
    ''' averages % returns between historical S&P500 & 10 year TBonds '''
    try:
        os.chdir('historical_data')
    except FileNotFoundError:
        pass

    stock_data = load_data(SP500_FILE)
    bond_data = load_data(TEN_YR_TBOND_FILE)

    avg_data = []
    for i in range(len(stock_data)):
        avg_return = perc_stocks*stock_data[i] + (1-perc_stocks)*bond_data[i]
        avg_data.append(round(avg_return, 2))

    with open('%s%s' % (perc_stocks, AVG_RETURN_FILE), 'w') as f:
        for year in avg_data:
            f.write('%s\n' % year)

# -----------------------------------------------------------------------------


def calculate_amount_leftover(start_amt, withdraw_amt, avg_yrs, perc_stocks):
    '''
    given starting conditions, return numbers on status of fund by end of
    retirement including % of years w/ low funds & whether bankrupt by EOY
    '''
    generate_avg_returns(perc_stocks)
    data = load_data('%s%s' % (perc_stocks, AVG_RETURN_FILE))

    yr_low_amt = 0
    bankrupt = False

    # randomly select n_years in retirement from Gaussian around avg
    n_years = int(np.random.normal(avg_yrs, avg_yrs/10))
    for year in range(n_years):
        if year == 0:
            leftover_amt = start_amt

        # follow random period in historical data to model performance
        subset = np.random.choice(len(data) - n_years)
        historical_subset = data[subset:subset + n_years]

        leftover_amt *= (1 + (historical_subset[year]/100))
        leftover_amt -= withdraw_amt  # assume annual end of year withdrawal

        if leftover_amt <= start_amt/20:
            yr_low_amt += 1
        if leftover_amt <= 0:
            bankrupt = True

    perc_low_funds = round(yr_low_amt/n_years, 2)

    return leftover_amt, perc_low_funds, bankrupt

# -----------------------------------------------------------------------------


def monte_carlo(start_amt, withdraw_amt, avg_yrs, perc_stocks, n_lifetimes):
    '''monte carlo around calculate_amount_leftover function'''
    amts_leftover = []
    perc_years_low = []
    n_lifes_bankrupt = 0

    for i in range(n_lifetimes):
        leftover, low, bankrupt = calculate_amount_leftover(
            start_amt, withdraw_amt, avg_yrs, perc_stocks)

        amts_leftover.append(round(leftover, 2))
        perc_years_low.append(low)
        if bankrupt:
            n_lifes_bankrupt += 1

    perc_lifes_bankrupt = n_lifes_bankrupt/n_lifetimes
    perc_amts_low = [a*b for a, b in zip(amts_leftover, perc_years_low)]

    amt_df = pd.DataFrame({'Amounts leftover': amts_leftover,
                           'Low funds': perc_amts_low},
                          index=list(range(1, len(amts_leftover)+1)))

    return amt_df, perc_lifes_bankrupt

# -----------------------------------------------------------------------------


def plot_performance_hist(mc_df, br_perc):
    '''generates histogram of performance of portfolio'''
    sns.set(style='whitegrid')
    sns.set_context('talk')

    f, ax = plt.subplots(figsize=(50, 50))

    sns.set_color_codes('deep')
    sns.barplot(x=list(range(1, len(mc_df)+1)),
                y='Amounts leftover', data=mc_df,
                label='Amount leftover at end', color='b')

    sns.set_color_codes('bright')
    sns.barplot(x=list(range(1, len(mc_df)+1)),
                y='Low funds', data=mc_df,
                label='Percent of total years with low funds', color='r')

    ax.legend(ncol=2, loc='lower right', frameon=True)
    ax.set(ylabel='Dollars leftover')
    ax.set_xticklabels([])
    ax.set_title('Percent of simulations bankrupt: %s' %
                 (round(br_perc*100, 1)), fontsize=20)

    plt.show()

# -----------------------------------------------------------------------------
