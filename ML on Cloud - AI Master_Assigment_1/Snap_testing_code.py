import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
# IMPUTERS:
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


pd.set_option('Display.Max_column', None)

clear = lambda:os.system('clear')

clear()

# FUNCTIONS:
def NaNs_calculator(data):
    
    '''MISSING DATA ON THE DATASET (TOTAL): (This goes before the describe)'''

    percentage_missing = (data.isna().mean()*100).sort_values(ascending = False)        # Storing the Percentages of NaNs
    sum_missing = data.isna().sum().sort_values(ascending = False)                      # Storing the Sum of NaNs
    names = sum_missing.index.to_list()                                                 # Storing names (to show in the columns)
    data_type = data[names].dtypes                                                      # Storing the type of data based on the order from the previous obtained data (slicing)
    sum_values = sum_missing.to_list()                                                  # Getting count of missing values
    perc_values = np.around(percentage_missing.to_list(), 3)                            # Getting percentage of missing values
    types = data_type.to_list()                                                         # Getting the types of the data
    # TURN ALL THE DATA INTO A DATAFRAME
    df_missing = pd.DataFrame({"NAMES" : names,                                         
                                    "VALUE COUNT" : sum_values,
                                    "PERCENTAGE (%)" : perc_values,
                                    "DATA TYPE": types})
    return df_missing
# --------------------
def data_slicing(data, chunk_number):
    """THIS FUNCTION WILL SLICE THE DATA FRAME INTO SMALER PIECES. FOR EXAMPLE, PASSING THE COUNTRIES IN WILL PROVIDE THE LABELS FOR YOUR GRAPHS"""
    
    # EXTRACTING THE CHUCKS
    segment_numbers = int(len(data)/chunk_number)           # for example a chunk_number of 4 will give 4 segments of 44 rows per chunk. 
    sliced_df = []                                          # Stored chunks
    segment = None                                          # to store the slice 

    for chunk in range(0, len(data), segment_numbers):
        segment = data[chunk:chunk + segment_numbers]       # Start index to the end
        sliced_df.append(segment)                           # Storing the segment

    return sliced_df
# -----------------------


df = pd.read_csv(r"/Users/alberto/Desktop/PROJECTS/ML on Cloud/global-data-on-sustainable-energy.csv")
# # print(df.head(10))

# # print(NaNs_calculator(df))


# # if("\n" in "Density\n(P/Km2)"):
# #     print('SI')
# #     print("Density\n(P/Km2)".replace("\n", "_"))

# for x in list(df.columns):

#     # TESTING STORING AND CHANGING NAMES ACCORDINGLY:

#     if(x == "Value_co2_emissions_kt_by_country"):
#         name = x.replace("Value_co2_emissions_kt_by_country", "TARGET_2_VALUE_CO2_EMISSIONS_PER_COUNTRY")
#         df.rename(columns={x: name}, inplace=True)
#     elif(x == "Primary energy consumption per capita (kWh/person)"):
#         name = x.replace("Primary energy consumption per capita (kWh/person)", "TARGET_1_PRIMARY_ENERGY_CONSUMPTION_PER_CAPITA_(KWH/PERSON)")
#         df.rename(columns={x: name}, inplace=True)
#     else:
#         if(" " in x):
#             name = x.replace(" ", '_')                  
#         elif("-" in x):
#             name = x.replace("-", '_')                  
#         elif("\\n" in x):
#             name = x.replace("\\n", '_')
#         else:
#             name = x                  
#         df.rename(columns={x: name.title()}, inplace=True)  # Setting the new name to the column
#     name = ''


# # -----------------

# # Decorations

# # labes_to_plot = sliced_df[0].index# Getting the names of the labels to graph
# # positions = len(labes_to_plot)# Ticks positions
# # rotation_angle = 45# Setting the rotation angle (in degrees)
# # plt.xticks(positions, labes_to_plot, rotation=rotation_angle)# Rotating the x-axis labels
# # plt.title('Enery consumption on average per country (KW/person)')# Setting the title
# # plt.grid()# Putting gred
# # plt.plot(sliced_df[0])#  section to plot
# # plt.tight_layout()



# # print(df.head(2))


# # ----------------------------------------
# clear()
# energy_country = df[['Entity', 'TARGET_1_PRIMARY_ENERGY_CONSUMPTION_PER_CAPITA_(KWH/PERSON)']]# Enerigy consumption per country
# data = data_slicing(energy_country['Entity'].unique(), 22) # Passing only the countries to plot the trend afterwards (10 countries per graph)
# print(data[0]) # this contains 8 countries to plot
# # len(data)

# l1 = [1, 2, 3, 4]
# l2 = ["a", "b", "c", "d"]

# for x, y in zip(l1, l2):
#     print(f'X = {x}, Y = {y}')

# # # -----------------------------
# clear()
# # Assuming year integers are provided
# years = df['Year']

# # Convert year integers to datetime objects
# datetime_objects = pd.to_datetime(df['Year'], format='%Y')

# # Create a date range with yearly frequency
# date_range = pd.date_range(start = datetime_objects.min(), end = datetime_objects.max(), freq='YS')
# print((date_range).unique())
# print((df['Year'].unique()))

# # MATCHING THE NUMBERS INTO A DICTIONARY
# # parsed_date = {2:'El num 2'}
# # print(parsed_date)
# # print(parsed_date[2])

# parsed_date ={} # 1. dict con los valores correspindientes (num: date value)
# for num_year, parsed_year in zip(df['Year'], date_range):
#     # print(f'from num_year = {num_year} into parsed_year = {parsed_year}')
#     parsed_date[num_year] = parsed_year
#     # print(parsed_date[num_year])

# print(len(parsed_date))

# # 2. loopeo sobre la columna year, y cada conicidencia va a ser a crear una nueva variable que vamos a poner dentro del data frame como index

# # Creating a new varible to store the parsed dates:
# dates = []

# for year_in_col in df['Year']:
#     # Creating a new column
#     dates.append(parsed_date[year_in_col])

# print(len(dates))

# 3. Adding it into a data frame

# df['Parse_years'] = dates

# print(df)

data_filtered = df[['Entity', 'Year', 'Value_co2_emissions_kt_by_country', 'Primary energy consumption per capita (kWh/person)']]
clear()

print(data_filtered.columns)

# for x in data_filtered.columns:
#     if(x == "Value_co2_emissions_kt_by_country"):
#         name = x.replace("Value_co2_emissions_kt_by_country", "CO2_EMISSIONS_PER")
#         data_filtered.rename(columns={x: name}, inplace=True)
#     elif(x == "Primary energy consumption per capita (kWh/person)"):
#         name = x.replace("Primary energy consumption per capita (kWh/person)", "ENERGY_CONSUMPTION(KWH/PERSON)")
#         data_filtered.rename(columns={x: name}, inplace=True)
#     else:
#         name = x
#     name = ''
# print(data_filtered.columns)

# IMPUTING VALUES WITH THE IMPUTER: GETTING THE COLUMNS WHERE WE WANT TO IMPUTE (NOT THE ONE WITH ZERO NaNs):
to_impute = NaNs_calculator(data_filtered)                                              # Basically, I am calling again the data frame to filter it
names_to_impute = to_impute[to_impute["PERCENTAGE (%)"] > 0]["NAMES"].tolist()      # Leaving out the columns that got no NaNs
col = data_filtered[names_to_impute]                                                    # Selecting only the column names to be imputed

# IMPUTING:
imputer = IterativeImputer(max_iter=10, random_state=0)                             # instantiating the imputer
imputed_col = imputer.fit_transform(col)                                            # Fitting the new data to the columns
data_filtered[names_to_impute] = imputed_col                                            # Replace the imputed values back into the original DataFrame
print(f'Number of columns after cleaning: {len(data_filtered.columns)}')                                                        # Checking the data