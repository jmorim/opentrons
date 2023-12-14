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
  eppendorfs_11 = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 11)

  ## Wellplates
  plate_2 = protocol.load_labware('agilent_54_vialplate_1500ul', 8)
  plate_5 = protocol.load_labware('greinerbioone_96_wellplate_280ul', 5)
  plate_8 = protocol.load_labware('greinerbioone_96_wellplate_280ul', 8)