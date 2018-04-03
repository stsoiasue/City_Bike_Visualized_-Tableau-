import pandas as pd
import numpy as np
import os
import glob

# find all csv files in dir,
bike_data_files = glob.glob('*.csv')

for data_file in bike_data_files:

    print(f'now processing: {data_file}')

    try:
        
        # create dataframe with file
        df = pd.read_csv(data_file)
        
        # change time columns to datetime 
        df['starttime'] = pd.to_datetime(df['starttime'])
        df['stoptime'] = pd.to_datetime(df['stoptime'])

        # add reformatted date columns
        df['starttime(R)'] = df['starttime'].dt.strftime('%m/%d/%Y %H:%M:%S')
        df['stoptime(R)'] = df['stoptime'].dt.strftime('%m/%d/%Y %H:%M:%S')

        # define save path
        save_path = os.path.join('reformatted_files', 'reformatted_' + data_file)

        # save file
        df.to_csv(save_path)

    except:

        print(f'{data_file} was not reformatted')