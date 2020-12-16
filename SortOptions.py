def sortOptions(options_to_check):
    from tqdm import tqdm
    import json
    options = []
    progress_bar = tqdm(total=len(options)*2, disable=False)
    watch = []
    for stonk in options_to_check:
        progress_bar.update(1)
        try:
            puts = stonk.json()['putExpDateMap']
        except:
            continue
        for option_chain in puts:
            watch.append([puts[option_chain], stonk.json()['underlying']])

    for option_list in watch:
        for option in option_list[0]:

            progress_bar.update(1)
            options.append([option_list[0][option][0], option_list[1]])
    progress_bar.close()
    return options
