def getOptions():
    import time, config
    from datetime import date, timedelta
    from tqdm import tqdm
    from tda import auth, client
    from get_all_tickers import get_tickers as gt
    try:
        c = auth.client_from_token_file(config.token_path, config.api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome(
                executable_path='/Users/likedapro/Desktop/Python/Stonks/Options Chain/chromedriver') as driver:
            c = auth.client_from_login_flow(
                driver, config.api_key, config.redirect_uri, config.token_path)

    tickers = gt.get_tickers()
    options_to_check = []

    progress_bar = tqdm(total=len(tickers), disable=False)
    # progress_bar = tqdm(total=3, disable=False)
    #
    for ticker in tickers:
    # for ticker in ['AAPL', 'TLSA', 'MSFT']:
        progress_bar.update(1)
        response = c.get_option_chain(ticker,
                                      contract_type=client.Client.Options.ContractType.PUT,
                                      strike_range=client.Client.Options.StrikeRange.OUT_OF_THE_MONEY,
                                      include_quotes=True,
                                      strike_to_date=(date.today()+timedelta(days=60)),
                                      strike_from_date=(date.today()+timedelta(days=1)),
                                      strike_count=5

                                      )
        options_to_check.append(response)
        time.sleep(0.45)
    progress_bar.close()
    return options_to_check

