from math import pow, log10
# -----------------------------------------------------------------------------

INFLATION = 0.035  # somewhat conservative estimate

# -----------------------------------------------------------------------------


def recommend_start_amt(withdrawal, n_yrs, pgrowth, inflation=INFLATION):
    '''recommends starting amount given retirment portfolio/condition'''
    start = withdrawal/((pgrowth-inflation) *
                        (1 - pow((1+inflation)/(1+pgrowth), n_yrs)))
    return round(start, 2)

# -----------------------------------------------------------------------------


def recommend_withdrawal(start_amt):
    '''
    returns range of withdrawal amounts from safe -> risky

    historically, a safe withdrawal rate has had a floor of 3.5% starting amt
    regardless of duration of market performance - inflation included
    '''
    safe_rate = round(0.035*start_amt, 2)
    risky_rate = round(0.045*start_amt, 2)
    return (safe_rate, risky_rate)

# -----------------------------------------------------------------------------


def calculate_expected_yrs(withdrawal, start_amt, pgrowth, inflation=INFLATION):
    ''' returns average number of years in retirement given portfolio '''
    numerator = log10(1 - (withdrawal/(start_amt*(pgrowth-inflation))))
    denominator = log10((1 + inflation)/(1 + pgrowth))

    return round(numerator/denominator, 2)

# -----------------------------------------------------------------------------
