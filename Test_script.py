# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:41:56 2020

@author: Trevor Ho
"""

# from opentrons import simulate
# protocol = simulate.get_protocol_api(version = '2.4')

from opentrons import protocol_api

metadata = {
    'apiLevel': '2.4'
}

def run(protocol: protocol_api.ProtocolContext):

    plate1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate2 = protocol.load_labware('corning_24_wellplate_3.4ml_flat', 2)
    tip_rack = protocol.load_labware('opentrons_96_tiprack_300ul', 3)

    r_pipette = protocol.load_instrument(
        'p300_single',
        'right',
        tip_racks=[tip_rack]
    )

    r_pipette.transfer(200,
                 plate2.wells_by_name()['A1'],
                 plate1.wells_by_name()['A1']
                )

    r_pipette.transfer(150,
                 plate2.wells_by_name()['A1'],
                 plate1.wells_by_name()['A2']
                )


# print(*protocol.commands(), sep = '\n')