
import netCDF4 as nc
import numpy as np

rseg_filename = "/projects/0/dfguu/users/edwin/data/rseg_grdc/RSEG_V01.nc"

rseg = nc.Dataset(rseg_filename)
rseg.variables.keys()

# ~ >>> rseg.variables.keys()
# ~ dict_keys(['KG_Class', 'GRDC_Num', 'Lat', 'Lon', 'Mean_Disch', 'PFAF_ID', 'Time', 'GDisch_SharePol', 'Disch', 'Disch_Err', 'Disch_Flag', 'Disch_Quality_Flag'])

column_headers = ['KG_Class', 'GRDC_Num', 'Lat', 'Lon', 'Mean_Disch', 'PFAF_ID', 'Time', 'GDisch_SharePol', 'Disch', 'Disch_Err', 'Disch_Flag', 'Disch_Quality_Flag']

grdc_all_stations = rseg["GRDC_Num"][:]

# ~ for i in range(0, len(grdc_all_stations)):
for i in range(0, 10):
    grdc_station = grdc_all_stations[i]
    print(grdc_station)

    print(rseg["Disch"][i][:])
    print(rseg["Disch"][i][-120:])
