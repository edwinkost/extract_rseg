
import netCDF4 as nc
import numpy as np

rseg_filename = "/projects/0/dfguu/users/edwin/data/rseg_grdc/RSEG_V01.nc"

rseg = nc.Dataset(rseg_filename)
rseg.variables.keys()

# ~ >>> rseg.variables.keys()
# ~ dict_keys(['KG_Class', 'GRDC_Num', 'Lat', 'Lon', 'Mean_Disch', 'PFAF_ID', 'Time', 'GDisch_SharePol', 'Disch', 'Disch_Err', 'Disch_Flag', 'Disch_Quality_Flag'])

headers = [
'GRDC_Num',
'Lat',
'Lon',
'Mean_Disch',
'PFAF_ID',
'GDisch_SharePol',
'Disch_Err',
'Disch_Flag',
'Disch_Quality_Flag'
]

rseg_station_table = np.column_stack((
np.array(rseg['GRDC_Num'][:]),
np.array(rseg['Lat'][:]),
np.array(rseg['Lon'][:]),
np.array(rseg['Mean_Disch'][:]),
np.array(rseg['PFAF_ID'][:]),
np.array(rseg['GDisch_SharePol'][:]),
np.array(rseg['Disch_Err'][:]),
np.array(rseg['Disch_Flag'][:]),
np.array(rseg['Disch_Quality_Flag'][:])
))

np.savetxt("rseg_station_table.csv", rseg_station_table,
delimiter = ";",
header = ";".join(headers),
comments='', 
)
