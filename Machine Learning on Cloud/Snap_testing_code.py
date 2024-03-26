import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


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


df = pd.read_csv(r"/Users/alberto/Downloads/PROJECTS/MACHINE-LEARNING-AND-DATA-SCIENCE-PROJECTS/Machine Learning on Cloud/global-data-on-sustainable-energy.csv", parse_dates=['Year'], index_col='Year')
# print(df.head(10))

# print(NaNs_calculator(df))


# if("\n" in "Density\n(P/Km2)"):
#     print('SI')
#     print("Density\n(P/Km2)".replace("\n", "_"))

for x in list(df.columns):

    # TESTING STORING AND CHANGING NAMES ACCORDINGLY:

    if(x == "Value_co2_emissions_kt_by_country"):
        name = x.replace("Value_co2_emissions_kt_by_country", "TARGET_2_VALUE_CO2_EMISSIONS_PER_COUNTRY")
        df.rename(columns={x: name}, inplace=True)
    elif(x == "Primary energy consumption per capita (kWh/person)"):
        name = x.replace("Primary energy consumption per capita (kWh/person)", "TARGET_1_PRIMARY_ENERGY_CONSUMPTION_PER_CAPITA_(KWH/PERSON)")
        df.rename(columns={x: name}, inplace=True)
    else:
        if(" " in x):
            name = x.replace(" ", '_')                  
        elif("-" in x):
            name = x.replace("-", '_')                  
        elif("\\n" in x):
            name = x.replace("\\n", '_')
        else:
            name = x                  
        df.rename(columns={x: name.title()}, inplace=True)  # Setting the new name to the column
    name = ''


# -----------------

# Decorations

# labes_to_plot = sliced_df[0].index# Getting the names of the labels to graph
# positions = len(labes_to_plot)# Ticks positions
# rotation_angle = 45# Setting the rotation angle (in degrees)
# plt.xticks(positions, labes_to_plot, rotation=rotation_angle)# Rotating the x-axis labels
# plt.title('Enery consumption on average per country (KW/person)')# Setting the title
# plt.grid()# Putting gred
# plt.plot(sliced_df[0])#  section to plot
# plt.tight_layout()



# print(df.head(2))


# ----------------------------------------
clear()
energy_country = df[['Entity', 'TARGET_1_PRIMARY_ENERGY_CONSUMPTION_PER_CAPITA_(KWH/PERSON)']]# Enerigy consumption per country
data = data_slicing(energy_country['Entity'].unique(), 22) # Passing only the countries to plot the trend afterwards (10 countries per graph)
print(data[0]) # this contains 8 countries to plot
# len(data)

l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c", "d"]

for x, y in zip(l1, l2):
    print(f'X = {x}, Y = {y}')