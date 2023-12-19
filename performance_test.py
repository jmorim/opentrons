from opentrons import protocol_api

metadata = {
  'protocolName': 'Layout',
  'description': 'Layout protocol for calibrating position',
  'author': 'morimoto'
}

requirements = {'robotType': 'OT-2', 'apiLevel': '2.15'}

def run(protocol: protocol_api.ProtocolContext):
  # Labware layout
  ## Tips
  tips_300 = protocol.load_labware('opentrons_96_tiprack_300ul', 3)
  tips_1000 = protocol.load_labware('opentrons_96_tiprack_1000ul', 6)

  ## Falcon tube rack
  falcons = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 11)

  ## Eppendorf tube racks
  eppendorfs_1 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 1)
  eppendorfs_4 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 4)
  eppendorfs_7 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 7)
  eppendorfs_10 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 10)
#  eppendorfs_11 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 11)

  ## Wellplates
  plate_2 = protocol.load_labware('agilent_54_vialplate_1500ul', 2)
  plate_5 = protocol.load_labware('greinerbioone_96_wellplate_280ul', 5)
  plate_8 = protocol.load_labware('greinerbioone_96_wellplate_280ul', 8)

  ## Pipettes
  p1000 = protocol.load_instrument('p1000_single', 'left', tip_racks=[tips_1000])
  p300 = protocol.load_instrument('p300_single', 'right', tip_racks=[tips_300])

  # Protocol actions
  ## Transfer 256 uL of stock solution (1.00 mg/mL) to A1 vial
  p300.transfer(256, eppendorfs_1['A1'], plate_2['A1'], touch_tip=True)
  ## Dilute to 1000 uL making a 256 ug/mL solution
  p1000.transfer(1000-256, falcons['A3'], plate_2['A1'], touch_tip=True)
  ## Transfer 500 uL diluent to each vial 
  ## (check if p1000 tips fit in vial)
  for i in range(3):
    p1000.distribute(500, falcons['A3'], plate_2.rows()[i][1:8], touch_tip=True)
    p1000.transfer(1000, falcons['A3'], plate_2.rows()[i][8], touch_tip=True)
  
  for i in range(3):
    # [:6]
    # 0, 1, 2, 3, 4, 5, 6
    # [1:7]
    # 1, 2, 3, 4, 5, 6, 7
    # 0 to 1, 1 to 2, 2 to 3, 3 to 4, 4 to 5, 5 to 6, 6 to 7
    p1000.transfer(500, plate_2.rows()[i][:7], plate_2.rows()[i][1:8], 
                   mix_before=(3, 500), touch_tip=True, new_tip='always')