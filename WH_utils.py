def get_WH_data_for_given_year(data_path: str, year: int) -> pd.DataFrame:
    
    ''' Provide data from specific year in categories 2 to 9
    
        Parameters
        ----------
        data_path
            where is the file
        year
            Requested year

        Returns
        -------
        comment
            Data from year of interest
    '''


def get_WH_data_for_given_year(data_file: str, year: int) -> pd.DataFrame:
    
    # Extract data
    WH_df = pd.read_csv(data_file)
    
    # Select year
    selected_rows = WH_df.loc[WH_df['Year']==year]
    
    # Select Category
    selected_columns = WH_df.columns[2:9]
    # Output 
    # WH_year_df = WH_df.loc[selected_rows, selected_columns]
    WH_year_df = selected_rows[selected_columns]
    return WH_year_df