# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:41:56 2020

@author: User
"""

from opentrons import simulate
protocol = simulate.get_protocol_api(version = '2.4')

plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)


tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', 2)

r_pipette = protocol.load_instrument('p300_single', 'right', 
                                     tip_racks = [tip_rack])

for i in range(3):

    r_pipette.transfer(200,
                       plate.wells()[0],
                       plate.wells()[1],
                       blow_out=True)

print(*protocol.commands(), sep = '\n')