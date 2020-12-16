def filterOptions(options, ROI):
    from tqdm import tqdm
    from operator import itemgetter
    filtered_options = []
    progress_bar = tqdm(total=len(options), disable=False)
    for option in options:
        progress_bar.update(1)
        # If expired
        if option[0]['delta'] == "NaN":
            continue
        # if OTM
        if option[0]['strikePrice'] >= option[1]['mark']:
            continue
        # If the ROI is at least 1
        if (option[0]['bid']/option[0]['strikePrice']) < ROI:
            continue
        # If the POP is at least 70% (0.25 delta)
        if option[0]['delta'] <= -0.25:
            continue
        # If there is volume
        filtered_options.append(option)
    progress_bar.close()
    return filtered_options
