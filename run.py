# Python standard library
import os
import glob
import gc

# 3rd party packages
import pylab as plt
from blimpy import Waterfall
import turbo_seti.find_doppler.seti_event as turbo
import turbo_seti.find_event as find
from turbo_seti.find_doppler.find_doppler import FindDoppler
from turbo_seti.find_event.find_event_pipeline import find_event_pipeline
from turbo_seti.find_event.plot_event_pipeline import plot_event_pipeline

# Local imports
#import download_progress





# You can edit this variable to match whichever directory you will use to store your data files
data_directory = '/datag/public/guest/DIAG_AGBT21A_996_36/'
rep_directory = '/datax/scratch/erikar/SETIproject/'
rep_dat_directory= '/datax/scratch/erikar/SETIproject/datfiles/'




# Create a simple .lst file of the .h5 files in the data directory
h5_list = sorted(glob.glob(os.path.join(data_directory, '*.fil')))
    
# This writes the .h5 files into a .lst, as required by the find_event_pipeline:
h5_list_path = os.path.join(rep_directory,'h5_files.lst')
with open(h5_list_path, 'w') as f:
    for h5_path in h5_list:
        if 'rawspec.8.' not in h5_path:
              f.write(h5_path + '\n')

# You don't have to print, but it's a good way to check that your list is in the correct order:
with open(h5_list_path, 'r') as f:
    print(f.read())




print(h5_list)





for file in h5_list:
    gc.collect()
    print(file)
    doppler = FindDoppler(file,
                      max_drift = 4, # Max drift rate = 4 Hz/second
                      snr = 20,      # Minimum signal to noise ratio = 10:1
                      out_dir = rep_dat_directory  # This is where the turboSETI output files will be stored.
                     )
    doppler.search()

print('\n===== All DAT files have been computed and a list of them has been constructed\n')
