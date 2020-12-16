def screen():
    import GetOptions, SortOptions, FilterOptions, ToSpreadsheet

    # Get options
    options_to_check = GetOptions.getOptions()

    # Sort Options
    options = SortOptions.sortOptions(options_to_check)

    #Filter options
    filtered_options = FilterOptions.filterOptions(options, 0.02) # With at least 1% ROI

    #Display Results
    # print(filtered_options)
    # print(json.dumps(filtered_options, indent=1 ))

    #To Spreadsheet
    ToSpreadsheet.toSpreadSheet(filtered_options)






