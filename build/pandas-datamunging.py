
# %% =============================================================================
# ########## COMBINING DATA ###########
# ########## COMBINING DATA ###########
# =============================================================================

import numpy as np
import pandas as pd
from numpy.random import randn


# %% =============================================================================
# #CONCATENATION
# =============================================================================

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

#Concatenation basically glues together DataFrames. Keep in mind that dimensions should match along the axis you are concatenating on. 
#You can use pd.concat and pass in a list of DataFrames to concatenate together:

df_all = pd.concat([df1,df2,df3])

print(df_all)

df_all_side = pd.concat([df1,df2,df3] , axis=1)

print(df_all_side)
# %% =============================================================================
# # JOINING - MERGE FUNCTION - 1 KEY
# =============================================================================

df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})   

pd.merge(df1, df2, how='inner' ,on='key') # default is inner join

# %% =============================================================================
# # JOINING - MERGE FUNCTION - 2 KEYS
# =============================================================================


df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(df1, df2, on=['key1', 'key2'])

pd.merge(df1, df2, how='outer', on=['key1', 'key2'])

pd.merge(df1, df2, how='left', on=['key1', 'key2'])

pd.merge(df1, df2, how='right', on=['key1', 'key2'])

# %% =============================================================================
# # JOINING - JOIN FUNCTION - joining on index
# =============================================================================

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

df2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

df1.join(df2) # default is left join
df1.join(df2, how='outer')
