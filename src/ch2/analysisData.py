import getMagicData as gmd

sudf = gmd.sudf
gmd.sudf.describe()
sudf.loc[:,'Beds'] = sudf['Beds'].map(lambda x: 0 if 'Studio' in x else x)
#print(sudf.info())

sudf.loc[:,'Rent'] = sudf['Rent'].astype(int)
sudf.loc[:,'Beds'] = sudf['Beds'].astype(int)
sudf.loc[:,'Baths'] = sudf['Baths'].astype(float)
sudf.loc[:,'Sqft'] = sudf['Sqft'].str.replace(',','')
sudf.loc[:,'Sqft'] = sudf['Sqft'].astype(float)
sudf.loc[:,'Floor'] = sudf['Floor'].astype(float)
#print(sudf.info())
#print(sudf.describe())
sudf = sudf.drop([318])
#print(sudf.describe())
sudf.pivot_table('Rent', 'Zip', 'Beds', aggfunc='mean')
sudf.pivot_table('Rent', 'Zip', 'Beds', aggfunc='count')

