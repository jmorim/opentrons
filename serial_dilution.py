from opentrons import protocol_api

metadata = {
            'protocolName': 'Serial Dilution',
            'description': 'Testing serial dilution',
            'author': 'morimoto'
            }

requirements = {'robotType': 'OT-2', 'apiLevel': '2.15'}

def run(protocol: protocol_api.ProtocolContext):
  # Labware
  tips_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 6)
  tips_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
  falcons = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 2)
  epps = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 1)
  plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 4)

  # Pipettes
  left_pipette = protocol.load_instrument('p1000_single_gen2', 'left', tip_racks=[tips_1000])
  right_pipette = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tips_300])

  # Commands
  ## Transfer diluent (water) to each eppendorf (A1 through A3)
  right_pipette.transfer(300, falcons['A3'], epps['A1'])

  ## loop example
  for i in range(3):
    ### epps.rows()[0] = row A, [i] loops A1 to A3
    #spot = epps.rows()[0][i]
    ### transfer from falcon tube rack A1 (standard stock) to each eppendorf
    #right_pipette.transfer(300, falcons['A1'], spot, mix_after=(3, 50))
    ### Serial dilute down the column
    ### colon operator (:) designates from beginning or to end of list
    ### left_pipette.transfer(100, row[:11], row[1:], mix_after(3, 50))
    #print(epps.rows()[i])
    #right_pipette.transfer(300, epps.rows()[i][:6], epps.rows()[i][1:], mix_after=(3, 50))
    row = plate.rows()[i]
    right_pipette.transfer(300, falcons['A3'], row[0], mix_after=(3, 50))
    right_pipette.transfer(300, row[:11], row[1:], mix_after=(3, 50))