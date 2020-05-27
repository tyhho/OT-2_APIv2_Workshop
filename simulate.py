# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:43:58 2020

@author: Trevor Ho
"""

#%% Simulation
from opentrons.simulate import simulate, format_runlog
protocol_filename = 'Test_script.py' # TODO: change this for a new file
protocol_file = open(protocol_filename)
runlog = simulate(protocol_file, file_name='')
print(format_runlog(runlog[0])) # Line modified compared to Opentrons Doc

#%% Export simulated log file for documentation

simulated_log_filename = protocol_filename.split('.py')[0] + '_log.txt'
simulated_log = open(simulated_log_filename, 'w+')
simulated_log.write(format_runlog(runlog[0]))
simulated_log.close()