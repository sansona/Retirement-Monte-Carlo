import os

import numpy as np

# ------------------------------------------------------------------------------

SP500_FILE = 'SP500_returns_1926-2013_pct.txt'
TEN_YR_TBOND_FILE = '10-yr_TBond_returns_1926-2013_pct.txt'
AVG_RETURN_FILE = '_stock_returns_1926-2013_pct.txt'

# ------------------------------------------------------------------------------


def load_data(fname):
    ''' returns list of chronological returns from file '''
    with open(fname, 'r') as f:
        data = []
        for line in f:
            data.append(float(line.rstrip('\n')))
    return data

# ------------------------------------------------------------------------------


def generate_avg_returns(perc_stocks):
    ''' averages returns between historical S&P500 & 10 year TBonds '''
    try:
        os.chdir('historical_data')
    except FileNotFoundError:
        pass

    stock_data = load_data(SP500_FILE)
    bond_data = load_data(TEN_YR_TBOND_FILE)

    avg_data = []
    for i in enumerate(stock_data):
        avg_return = perc_stocks*stock_data[i] + (1-perc_stocks)*bond_data[i]
        avg_data.append(round(avg_return/100, 2))

    with open('%s%s' % (perc_stocks, AVG_RETURN_FILE), 'w') as f:
        for year in avg_data:
            f.write('%s\n' % year)

# ------------------------------------------------------------------------------


def calculate_amount_leftover(start_amt, withdraw_amt, avg_yrs, perc_stocks):
    '''
    given starting conditions, return numbers on status of fund by end of
    retirement. Uses Gaussian distribution around avg_yrs retired to model
    variability in retirement years and random subset of historical data to
    model portfolio performance
    '''
    generate_avg_returns(perc_stocks)
    data = load_data('%s%s' % (perc_stocks, AVG_RETURN_FILE))

    yr_low_amt = 0
    bankrupt = False

    # randomly select n_years in retirement from Gaussian around avg
    n_years = int(np.random.normal(avg_yrs, avg_yrs/10))
    for year in range(n_years):
        if year == 0:
            curr_amt = start_amt

        # follow random period in historical data to model performance
        subset = np.random.choice(len(data) - n_years)
        historical_subset = data[subset:subset + n_years]

        print('Return percent: %s' % historical_subset[year])
        print('Beginning year amt: %s' % curr_amt)
        curr_amt *= (1 + (historical_subset[year]/100))
        print('Year end amt: %s' % curr_amt)

        curr_amt -= withdraw_amt
        print('After deductions: %s ' % curr_amt)
        print('\n')

        if curr_amt <= 0:
            bankrupt = True
            break
        elif curr_amt <= start_amt/10:
            yr_low_amt += 1

    return curr_amt, yr_low_amt, bankrupt

# ------------------------------------------------------------------------------


def monte_carlo(start_amt, withdraw_amt, avg_yrs, perc_stocks, n_iter):
    '''monte carlo around calculate_amount_leftover function'''
    amts_leftover = []
    n_years_low = 0
    n_years_bankrupt = 0

    for i in range(n_iter):
        leftover, low, bankrupt = calculate_amount_leftover(
            start_amt, withdraw_amt, avg_yrs, perc_stocks)

        amts_leftover.append(leftover)
        n_years_low += low
        if bankrupt:
            n_years_bankrupt += 1

    print(amts_leftover)
    print('n_years_low: %s' % n_years_low)
    print('n_years_bankrupt: %s' % n_years_bankrupt)

    return (amts_leftover, n_years_low, n_years_bankrupt)

# ------------------------------------------------------------------------------
