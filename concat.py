# importing the required modules
import glob
import pandas as pd
  
# specifying the path to csv files
path = r'C:\Users\l034855\Documents\Data\Titer'
  
# csv files in the path
files = glob.glob(path + "/*.csv")
  
# defining an empty list to store 
# content
data_frame = pd.DataFrame()
content = []
  
# checking all the csv files in the 
# specified path
for filename in files:
    
    # reading content of csv file
    # content.append(filename)
    df = pd.read_csv(filename, index_col=None)
    content.append(df)
  
# converting content to data frame
data_frame = pd.concat(content)
data_frame = data_frame[data_frame['sample id'] != 'M287-PU-001'] 

describe = pd.DataFrame() 
describe = data_frame.describe()
describe.to_csv('titer_stats_noAME.csv')
data_frame.to_csv('Titer_data_concat_noAME.csv')
