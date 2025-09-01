"""
This script creates a valid SEL .rdb file by using a template approach.
It copies an existing valid RDB file and modifies its contents to match
the settings from the input text file.

This is the most reliable approach since creating a valid OLE2 structured
storage file from scratch is complex and error-prone.
"""

import os
import sys
import shutil
import olefile

def create_rdb_file(input_txt_path, output_rdb_path, template_rdb_path=None):
    """
    Convert a relay settings text file to a valid SEL .rdb file by copying a template
    and modifying its contents
    
    Args:
        input_txt_path (str): Path to the input text file with relay settings
        output_rdb_path (str): Path where the output RDB file will be created
        template_rdb_path (str, optional): Path to the template RDB file. 
            If not provided, will look for Relay710.rdb in the same directory as this module.
    """
    # Read the input text file
    with open(input_txt_path, 'r') as f:
        content = f.read()
    
    # Parse the content into sections
    sections = parse_txt_content(content)
    
    # If no template path provided, use the default one
    if template_rdb_path is None:
        template_rdb_path = os.path.join(os.path.dirname(__file__), "Relay710.rdb")
    
    # Copy the template RDB file to the output path
    shutil.copyfile(template_rdb_path, output_rdb_path)
    
    # Open the copied RDB file for modification
    try:
        ole = olefile.OleFileIO(output_rdb_path, write_mode=True)
        
        # Clear existing streams (we'll replace them)
        # Note: olefile doesn't support deleting streams, so we'll overwrite them
        
        # Write the required streams
        write_required_streams(ole, sections)
        
        # Close the OLE file
        ole.close()
        
        print(f"Successfully created {output_rdb_path}")
    except Exception as e:
        # If there's an error, remove the partially created file
        if os.path.exists(output_rdb_path):
            os.remove(output_rdb_path)
        raise e

def parse_txt_content(content):
    """
    Parse the text content into sections
    """
    sections = {}
    current_section = None
    
    for line in content.split('\n'):
        line = line.strip()
        if not line or line.startswith(';'):
            continue
            
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            sections[current_section] = {}
        elif '=' in line and current_section:
            key, value = line.split('=', 1)
            sections[current_section][key] = value
    
    return sections

def write_required_streams(ole, sections):
    """
    Write the required streams to the OLE file
    """
    # Base path for streams
    base_path = "Relays/New Settings 2"
    
    # Write Cfg.txt
    cfg_content = create_cfg_content(sections)
    try:
        ole.write_stream(f"{base_path}/Misc/Cfg.txt", cfg_content.encode('utf-8'))
    except ValueError:
        # If the stream doesn't exist or is the wrong size, we'll skip it
        print(f"Warning: Could not write {base_path}/Misc/Cfg.txt")
    
    # Write DatabaseVersion.txt
    try:
        ole.write_stream(f"{base_path}/Misc/DatabaseVersion.txt", "1.1\n".encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/Misc/DatabaseVersion.txt")
    
    # Write Device.txt
    device_name = sections.get('Device', {}).get('Model', 'New Settings 2')
    try:
        ole.write_stream(f"{base_path}/Misc/Device.txt", f"{device_name}\n".encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/Misc/Device.txt")
    
    # Write Version
    version_content = "1.1\n"
    try:
        ole.write_stream(f"{base_path}/Misc/Version", version_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/Misc/Version")
    
    # Write setting files
    write_setting_files(ole, sections, base_path)

def create_cfg_content(sections):
    """
    Create the Cfg.txt content
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    cfg_content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    cfg_content += "FID=SEL-710-Rxxx-Vx-Z008004-Dxxxxxxxx\r\n"
    cfg_content += "BFID=SLBT-710-Rxxx-V0-Z007004-Dxxxxxxxx\r\n"
    cfg_content += "PARTNO=071001A5X6X71821210\r\n"
    cfg_content += "[CLASSES]\r\n"
    cfg_content += "1,\"Group 1\"\r\n"
    cfg_content += "2,\"Group 2\"\r\n"
    cfg_content += "3,\"Group 3\"\r\n"
    cfg_content += "L1,\"Logic 1\"\r\n"
    cfg_content += "L2,\"Logic 2\"\r\n"
    cfg_content += "L3,\"Logic 3\"\r\n"
    cfg_content += "G,\"Global\"\r\n"
    cfg_content += "PF,\"Port F\"\r\n"
    cfg_content += "P1,\"Port 1\"\r\n"
    cfg_content += "P2,\"Port 2\"\r\n"
    cfg_content += "P3,\"Port 3\"\r\n"
    cfg_content += "P4,\"Port 4\"\r\n"
    cfg_content += "F,\"Front Panel\"\r\n"
    cfg_content += "R,\"Report\"\r\n"
    cfg_content += "M,\"Modbus User Map\"\r\n"
    
    return cfg_content

def write_setting_files(ole, sections, base_path):
    """
    Write the setting files based on the sections
    """
    # Write set_1.txt (Protection - Overcurrent)
    overcurrent_content = create_overcurrent_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_1.txt", overcurrent_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_1.txt")
    
    # Write set_2.txt (Protection - Voltage)
    voltage_content = create_voltage_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_2.txt", voltage_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_2.txt")
    
    # Write set_3.txt (Protection - Frequency)
    frequency_content = create_frequency_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_3.txt", frequency_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_3.txt")
    
    # Write set_F.txt (Motor Protection)
    motor_content = create_motor_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_F.txt", motor_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_F.txt")
    
    # Write set_G.txt (Alarms and Events)
    alarms_content = create_alarms_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_G.txt", alarms_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_G.txt")
    
    # Write set_L1.txt (Logic Settings)
    logic_content = create_logic_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_L1.txt", logic_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_L1.txt")
    
    # Write set_P1.txt (Communications)
    comm_content = create_comm_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_P1.txt", comm_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_P1.txt")
    
    # Write set_M.txt (Metering)
    metering_content = create_metering_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_M.txt", metering_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_M.txt")
    
    # Write set_R.txt (Testing)
    testing_content = create_testing_content(sections)
    try:
        ole.write_stream(f"{base_path}/set_R.txt", testing_content.encode('utf-8'))
    except ValueError:
        print(f"Warning: Could not write {base_path}/set_R.txt")

def create_overcurrent_content(sections):
    """
    Create content for overcurrent protection settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[1]\r\n"
    
    oc_section = sections.get('Protection - Overcurrent', {})
    
    # Map the settings
    content += f"50P1P,\"{oc_section.get('50P Pickup', 'OFF')}\"\u001c\r\n"
    content += f"50P1D,\"{oc_section.get('50P Delay', '0.00')}\"\u001c\r\n"
    content += f"51P1P,\"{oc_section.get('51P Pickup', 'OFF')}\"\u001c\r\n"
    content += f"51P1TD,\"{oc_section.get('51P Time Dial', '3.00')}\"\u001c\r\n"
    content += f"50N1P,\"{oc_section.get('50N Pickup', 'OFF')}\"\u001c\r\n"
    content += f"50N1D,\"{oc_section.get('50N Delay', '0.00')}\"\u001c\r\n"
    content += f"51N1P,\"{oc_section.get('51N Pickup', 'OFF')}\"\u001c\r\n"
    content += f"51N1TD,\"{oc_section.get('51N Time Dial', '3.00')}\"\u001c\r\n"
    
    # Add default values for other settings
    content += "CTR1,\"100\"\u001c\r\n"
    content += "FLA1,\"50.0\"\u001c\r\n"
    content += "CTRN,\"100\"\u001c\r\n"
    content += "PTR,\"35.00\"\u001c\r\n"
    content += "VNOM,\"4160\"\u001c\r\n"
    content += "DELTA_Y,\"DELTA\"\u001c\r\n"
    content += "SINGLEV,\"N\"\u001c\r\n"
    content += "SF,\"1.15\"\u001c\r\n"
    content += "LRA1,\"6.0\"\u001c\r\n"
    content += "LRTHOT1,\"10.0\"\u001c\r\n"
    
    # Add more default settings as needed
    content += "50G1P,\"OFF\"\u001c\r\n"
    content += "50G1D,\"0.50\"\u001c\r\n"
    content += "51AP,\"OFF\"\u001c\r\n"
    content += "51AC,\"U3\"\u001c\r\n"
    content += "51ATD,\"3.00\"\u001c\r\n"
    content += "51ARS,\"N\"\u001c\r\n"
    content += "51ACT,\"0.00\"\u001c\r\n"
    content += "51AMR,\"0.00\"\u001c\r\n"
    content += "51ATC,\"1\"\u001c\r\n"
    content += "51BP,\"OFF\"\u001c\r\n"
    content += "51BC,\"U3\"\u001c\r\n"
    content += "51BTD,\"3.00\"\u001c\r\n"
    content += "51BRS,\"N\"\u001c\r\n"
    content += "51BCT,\"0.00\"\u001c\r\n"
    content += "51BMR,\"0.00\"\u001c\r\n"
    content += "51BTC,\"1\"\u001c\r\n"
    content += "51CP,\"OFF\"\u001c\r\n"
    content += "51CC,\"U3\"\u001c\r\n"
    content += "51CTD,\"3.00\"\u001c\r\n"
    content += "51CRS,\"N\"\u001c\r\n"
    content += "51CCT,\"0.00\"\u001c\r\n"
    content += "51CMR,\"0.00\"\u001c\r\n"
    content += "51CTC,\"1\"\u001c\r\n"
    content += "51P2P,\"OFF\"\u001c\r\n"
    content += "51P2C,\"U3\"\u001c\r\n"
    content += "51P2TD,\"3.00\"\u001c\r\n"
    content += "51P2RS,\"N\"\u001c\r\n"
    content += "51P2CT,\"0.00\"\u001c\r\n"
    content += "51P2MR,\"0.00\"\u001c\r\n"
    content += "51P2TC,\"1\"\u001c\r\n"
    content += "51QC,\"U3\"\u001c\r\n"
    content += "51QRS,\"N\"\u001c\r\n"
    content += "51QP,\"OFF\"\u001c\r\n"
    content += "51QTD,\"3.00\"\u001c\r\n"
    content += "51QCT,\"0.00\"\u001c\r\n"
    content += "51QMR,\"0.00\"\u001c\r\n"
    content += "51QTC,\"1\"\u001c\r\n"
    content += "51G1P,\"OFF\"\u001c\r\n"
    content += "51G1C,\"U3\"\u001c\r\n"
    content += "51G1TD,\"1.50\"\u001c\r\n"
    content += "51G1RS,\"N\"\u001c\r\n"
    content += "51G1CT,\"0.00\"\u001c\r\n"
    content += "51G1MR,\"0.00\"\u001c\r\n"
    content += "51G1TC,\"1\"\u001c\r\n"
    content += "51G2P,\"OFF\"\u001c\r\n"
    content += "51G2C,\"U3\"\u001c\r\n"
    content += "51G2TD,\"1.50\"\u001c\r\n"
    content += "51G2RS,\"N\"\u001c\r\n"
    content += "51G2CT,\"0.00\"\u001c\r\n"
    content += "51G2MR,\"0.00\"\u001c\r\n"
    content += "51G2TC,\"1\"\u001c\r\n"
    content += "46UBAD,\"10\"\u001c\r\n"
    content += "E2SPEED,\"N\"\u001c\r\n"
    content += "FVR_PH,\"NONE\"\u001c\r\n"
    content += "TCLRNEN,\"Y\"\u001c\r\n"
    content += "COOLEN,\"N\"\u001c\r\n"
    content += "ETHMBIAS,\"N\"\u001c\r\n"
    content += "E87M,\"N\"\u001c\r\n"
    content += "ESTAR_D,\"N\"\u001c\r\n"
    content += "E47T,\"Y\"\u001c\r\n"
    content += "EPTC,\"N\"\u001c\r\n"
    content += "E49RTD,\"NONE\"\u001c\r\n"
    content += "37PAD,\"1\"\u001c\r\n"
    content += "LOAD,\"OFF\"\u001c\r\n"
    content += "LOADLOWP,\"OFF\"\u001c\r\n"
    content += "BLK46,\"N\"\u001c\r\n"
    content += "BLK48,\"N\"\u001c\r\n"
    content += "BLK50EF,\"N\"\u001c\r\n"
    content += "BLK50P,\"N\"\u001c\r\n"
    content += "BLK37,\"N\"\u001c\r\n"
    content += "BLK66,\"N\"\u001c\r\n"
    content += "BLK49PTC,\"N\"\u001c\r\n"
    content += "BLK49RTD,\"N\"\u001c\r\n"
    content += "CTR2,\"100\"\u001c\r\n"
    content += "FLA2,\"50.0\"\u001c\r\n"
    content += "E49MOTOR,\"Y\"\u001c\r\n"
    content += "50P2D,\"0.50\"\u001c\r\n"
    content += "50N2P,\"OFF\"\u001c\r\n"
    content += "50N2D,\"10.0\"\u001c\r\n"
    content += "50G2P,\"OFF\"\u001c\r\n"
    content += "50G2D,\"10.0\"\u001c\r\n"
    content += "50Q1P,\"3.00\"\u001c\r\n"
    content += "50Q1D,\"0.1\"\u001c\r\n"
    content += "50Q2P,\"0.30\"\u001c\r\n"
    content += "50Q2D,\"0.2\"\u001c\r\n"
    content += "CTR87M,\"100\"\u001c\r\n"
    content += "87M1P,\"OFF\"\u001c\r\n"
    content += "87M1TD,\"0.10\"\u001c\r\n"
    content += "87M1TC,\"50S\"\u001c\r\n"
    content += "87M2P,\"OFF\"\u001c\r\n"
    content += "87M2TD,\"0.10\"\u001c\r\n"
    content += "87M2TC,\"NOT 50S\"\u001c\r\n"
    content += "LJTPU,\"OFF\"\u001c\r\n"
    content += "LJTDLY,\"0.50\"\u001c\r\n"
    content += "LJAPU,\"OFF\"\u001c\r\n"
    content += "LJADLY,\"5.00\"\u001c\r\n"
    content += "LLTPU,\"OFF\"\u001c\r\n"
    content += "LLTDLY,\"5.0\"\u001c\r\n"
    content += "LLAPU,\"OFF\"\u001c\r\n"
    content += "LLADLY,\"10.0\"\u001c\r\n"
    content += "LLSDLY,\"0\"\u001c\r\n"
    content += "46UBT,\"20\"\u001c\r\n"
    content += "46UBTD,\"5\"\u001c\r\n"
    content += "46UBA,\"10\"\u001c\r\n"
    content += "START_T,\"OFF\"\u001c\r\n"
    content += "STAR_MAX,\"OFF\"\u001c\r\n"
    content += "MAXSTART,\"OFF\"\u001c\r\n"
    content += "TBSDLY,\"OFF\"\u001c\r\n"
    content += "ABSDLY,\"OFF\"\u001c\r\n"
    content += "SPDSDLYT,\"OFF\"\u001c\r\n"
    content += "SPDSDLYA,\"OFF\"\u001c\r\n"
    content += "27P1P,\"OFF\"\u001c\r\n"
    content += "27P1D,\"0.5\"\u001c\r\n"
    content += "27P2P,\"OFF\"\u001c\r\n"
    content += "27P2D,\"5.0\"\u001c\r\n"
    content += "59P1P,\"1.10\"\u001c\r\n"
    content += "59P1D,\"0.5\"\u001c\r\n"
    content += "59P2P,\"OFF\"\u001c\r\n"
    content += "59P2D,\"5.0\"\u001c\r\n"
    content += "NVARTP,\"OFF\"\u001c\r\n"
    content += "PVARTP,\"OFF\"\u001c\r\n"
    content += "VARTD,\"1\"\u001c\r\n"
    content += "NVARAP,\"OFF\"\u001c\r\n"
    content += "PVARAP,\"OFF\"\u001c\r\n"
    content += "VARAD,\"1\"\u001c\r\n"
    content += "VARDLY,\"0\"\u001c\r\n"
    content += "37PTP,\"OFF\"\u001c\r\n"
    content += "37PTD,\"1\"\u001c\r\n"
    content += "37PAP,\"OFF\"\u001c\r\n"
    content += "37DLY,\"0\"\u001c\r\n"
    content += "55LGTP,\"OFF\"\u001c\r\n"
    content += "55LDTP,\"OFF\"\u001c\r\n"
    content += "55TD,\"1\"\u001c\r\n"
    content += "55LGAP,\"OFF\"\u001c\r\n"
    content += "55LDAP,\"OFF\"\u001c\r\n"
    content += "55AD,\"1\"\u001c\r\n"
    content += "55DLY,\"0\"\u001c\r\n"
    content += "81D1TP,\"OFF\"\u001c\r\n"
    content += "81D1TD,\"1.0\"\u001c\r\n"
    content += "81D2TP,\"OFF\"\u001c\r\n"
    content += "81D2TD,\"1.0\"\u001c\r\n"
    content += "81D3TP,\"OFF\"\u001c\r\n"
    content += "81D3TD,\"1.0\"\u001c\r\n"
    content += "81D4TP,\"OFF\"\u001c\r\n"
    content += "81D4TD,\"1.0\"\u001c\r\n"
    content += "LOADUPP,\"OFF\"\u001c\r\n"
    content += "BLKPROT,\"0\"\u001c\r\n"
    content += "TDURD,\"0.5\"\u001c\r\n"
    content += "TR,\"49T OR LOSSTRIP OR JAMTRIP OR 46UBT OR 50P1T OR 50G1T OR 59P1T OR 47T OR 55T OR SPDSTR OR 50N1T OR SMTRIP OR (27P1T AND NOT LOP) OR SV01T\"\u001c\r\n"
    content += "REMTRIP,\"0\"\u001c\r\n"
    content += "ULTRIP,\"0\"\u001c\r\n"
    content += "52A,\"0\"\u001c\r\n"
    content += "STREQ,\"PB03\"\u001c\r\n"
    content += "EMRSTR,\"0\"\u001c\r\n"
    content += "SPEED2,\"0\"\u001c\r\n"
    content += "SPEEDSW,\"0\"\u001c\r\n"
    content += "50P1D,\"0.00\"\u001c\r\n"
    content += "50P2P,\"OFF\"\u001c\r\n"
    content += "FLS,\"OFF\"\u001c\r\n"
    content += "LRQ,\"0.80\"\u001c\r\n"
    content += "SLIPSRC,\"R1\"\u001c\r\n"
    content += "SETMETH,\"RATING\"\u001c\r\n"
    content += "49RSTP,\"75\"\u001c\r\n"
    content += "TD1,\"1.00\"\u001c\r\n"
    content += "RTC1,\"AUTO\"\u001c\r\n"
    content += "LRA2,\"6.0\"\u001c\r\n"
    content += "LRTHOT2,\"10.0\"\u001c\r\n"
    content += "TD2,\"1.00\"\u001c\r\n"
    content += "RTC2,\"AUTO\"\u001c\r\n"
    content += "CURVE1,\"5\"\u001c\r\n"
    content += "TTT105,\"AUTO\"\u001c\r\n"
    content += "TTT110,\"AUTO\"\u001c\r\n"
    content += "TTT120,\"AUTO\"\u001c\r\n"
    content += "TTT130,\"AUTO\"\u001c\r\n"
    content += "TTT140,\"AUTO\"\u001c\r\n"
    content += "TTT150,\"AUTO\"\u001c\r\n"
    content += "TTT175,\"625.0\"\u001c\r\n"
    content += "TTT200,\"400.0\"\u001c\r\n"
    content += "TTT225,\"AUTO\"\u001c\r\n"
    content += "TTT250,\"225.0\"\u001c\r\n"
    content += "TTT275,\"AUTO\"\u001c\r\n"
    content += "TTT300,\"AUTO\"\u001c\r\n"
    content += "TTT350,\"AUTO\"\u001c\r\n"
    content += "TTT400,\"72.0\"\u001c\r\n"
    content += "TTT450,\"58.0\"\u001c\r\n"
    content += "TTT500,\"30.0\"\u001c\r\n"
    content += "TTT550,\"25.0\"\u001c\r\n"
    content += "TTT600,\"18.1\"\u001c\r\n"
    content += "TTT650,\"15.2\"\u001c\r\n"
    content += "TTT700,\"13.2\"\u001c\r\n"
    content += "TTT750,\"AUTO\"\u001c\r\n"
    content += "TTT800,\"AUTO\"\u001c\r\n"
    content += "TTT850,\"AUTO\"\u001c\r\n"
    content += "TTT900,\"AUTO\"\u001c\r\n"
    content += "TTT950,\"AUTO\"\u001c\r\n"
    content += "TTT1000,\"AUTO\"\u001c\r\n"
    content += "TTT1100,\"AUTO\"\u001c\r\n"
    content += "TTT1200,\"AUTO\"\u001c\r\n"
    content += "CURVE2,\"7\"\u001c\r\n"
    content += "TCAPU,\"85\"\u001c\r\n"
    content += "TCSTART,\"OFF\"\u001c\r\n"
    content += "COOLTIME,\"84\"\u001c\r\n"
    content += "COASTIME,\"5\"\u001c\r\n"
    content += "ERTDBIAS,\"N\"\u001c\r\n"
    content += "RTD1LOC,\"OFF\"\u001c\r\n"
    content += "RTD1TY,\"PT100\"\u001c\r\n"
    content += "TRTMP1,\"OFF\"\u001c\r\n"
    content += "ALTMP1,\"OFF\"\u001c\r\n"
    content += "RTD2LOC,\"OFF\"\u001c\r\n"
    content += "RTD2TY,\"PT100\"\u001c\r\n"
    content += "TRTMP2,\"OFF\"\u001c\r\n"
    content += "ALTMP2,\"OFF\"\u001c\r\n"
    content += "RTD3LOC,\"OFF\"\u001c\r\n"
    content += "RTD3TY,\"PT100\"\u001c\r\n"
    content += "TRTMP3,\"OFF\"\u001c\r\n"
    content += "ALTMP3,\"OFF\"\u001c\r\n"
    content += "RTD4LOC,\"OFF\"\u001c\r\n"
    content += "RTD4TY,\"PT100\"\u001c\r\n"
    content += "TRTMP4,\"OFF\"\u001c\r\n"
    content += "ALTMP4,\"OFF\"\u001c\r\n"
    content += "RTD5LOC,\"OFF\"\u001c\r\n"
    content += "RTD5TY,\"PT100\"\u001c\r\n"
    content += "TRTMP5,\"OFF\"\u001c\r\n"
    content += "ALTMP5,\"OFF\"\u001c\r\n"
    content += "RTD6LOC,\"OFF\"\u001c\r\n"
    content += "RTD6TY,\"PT100\"\u001c\r\n"
    content += "TRTMP6,\"OFF\"\u001c\r\n"
    content += "ALTMP6,\"OFF\"\u001c\r\n"
    content += "RTD7LOC,\"OFF\"\u001c\r\n"
    content += "RTD7TY,\"PT100\"\u001c\r\n"
    content += "TRTMP7,\"OFF\"\u001c\r\n"
    content += "ALTMP7,\"OFF\"\u001c\r\n"
    content += "RTD8LOC,\"OFF\"\u001c\r\n"
    content += "RTD8TY,\"PT100\"\u001c\r\n"
    content += "TRTMP8,\"OFF\"\u001c\r\n"
    content += "ALTMP8,\"OFF\"\u001c\r\n"
    content += "RTD9LOC,\"OFF\"\u001c\r\n"
    content += "RTD9TY,\"PT100\"\u001c\r\n"
    content += "TRTMP9,\"OFF\"\u001c\r\n"
    content += "ALTMP9,\"OFF\"\u001c\r\n"
    content += "RTD10LOC,\"OFF\"\u001c\r\n"
    content += "RTD10TY,\"PT100\"\u001c\r\n"
    content += "TRTMP10,\"OFF\"\u001c\r\n"
    content += "ALTMP10,\"OFF\"\u001c\r\n"
    content += "RTD11LOC,\"OFF\"\u001c\r\n"
    content += "RTD11TY,\"PT100\"\u001c\r\n"
    content += "TRTMP11,\"OFF\"\u001c\r\n"
    content += "ALTMP11,\"OFF\"\u001c\r\n"
    content += "RTD12LOC,\"OFF\"\u001c\r\n"
    content += "RTD12TY,\"PT100\"\u001c\r\n"
    content += "TRTMP12,\"OFF\"\u001c\r\n"
    content += "ALTMP12,\"OFF\"\u001c\r\n"
    content += "EWDGV,\"N\"\u001c\r\n"
    content += "EBRGV,\"N\"\u001c\r\n"
    
    return content

def create_voltage_content(sections):
    """
    Create content for voltage protection settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[2]\r\n"
    
    voltage_section = sections.get('Protection - Voltage', {})
    
    # Map the settings
    content += f"27P1P,\"{voltage_section.get('27P Undervoltage', 'OFF')}\"\u001c\r\n"
    content += f"59P1P,\"{voltage_section.get('59P Overvoltage', 'OFF')}\"\u001c\r\n"
    content += f"27N1P,\"{voltage_section.get('27N Undervoltage', 'OFF')}\"\u001c\r\n"
    content += f"59N1P,\"{voltage_section.get('59N Overvoltage', 'OFF')}\"\u001c\r\n"
    
    return content

def create_frequency_content(sections):
    """
    Create content for frequency protection settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[3]\r\n"
    
    freq_section = sections.get('Protection - Frequency', {})
    
    # Map the settings
    content += f"81U1TP,\"{freq_section.get('81U Underfrequency', 'OFF')}\"\u001c\r\n"
    content += f"81O1TP,\"{freq_section.get('81O Overfrequency', 'OFF')}\"\u001c\r\n"
    content += f"81R1TP,\"{freq_section.get('81R RateOfChange', 'OFF')}\"\u001c\r\n"
    
    return content

def create_motor_content(sections):
    """
    Create content for motor protection settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[F]\r\n"
    
    motor_section = sections.get('Motor Protection', {})
    
    # Map the settings
    content += f"JAMDET,\"{motor_section.get('Jam Detection', 'OFF')}\"\u001c\r\n"
    content += f"LKROTOR,\"{motor_section.get('Locked Rotor', 'OFF')}\"\u001c\r\n"
    content += f"TCAPU,\"{motor_section.get('Thermal Capacity', '85%')}\"\u001c\r\n"
    content += f"RSTINH,\"{motor_section.get('Restart Inhibit', '10s')}\"\u001c\r\n"
    
    return content

def create_alarms_content(sections):
    """
    Create content for alarms and events settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[G]\r\n"
    
    alarms_section = sections.get('Alarms and Events', {})
    
    # Map the settings
    content += f"TRIPMSG,\"{alarms_section.get('Trip Message', 'Motor Trip Detected')}\"\u001c\r\n"
    content += f"ALARM1,\"{alarms_section.get('Alarm1', 'NONE')}\"\u001c\r\n"
    content += f"ALARM2,\"{alarms_section.get('Alarm2', 'NONE')}\"\u001c\r\n"
    content += f"ALARM3,\"{alarms_section.get('Alarm3', 'NONE')}\"\u001c\r\n"
    
    return content

def create_logic_content(sections):
    """
    Create content for logic settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[L1]\r\n"
    
    logic_section = sections.get('Logic Settings', {})
    
    # Add logic equations
    for i in range(1, 4):
        equation_key = f'SELogic Equation{i}'
        if equation_key in logic_section:
            equation = logic_section[equation_key]
            # Convert to the format used in SEL files
            equation = equation.replace(' → ', ',')
            content += f"SV{i:02d},\"{equation}\"\u001c\r\n"
    
    # Add default values for other logic settings
    for i in range(4, 33):
        content += f"SV{i:02d},\"NA\"\u001c\r\n"
    
    # Add other default logic settings
    for i in range(1, 33):
        content += f"OUT{i:03d}FS,\"N\"\u001c\r\n"
    
    content += "OUT103FS,\"Y\"\u001c\r\n"
    content += "OUT101FS,\"Y\"\u001c\r\n"
    
    for i in range(1, 33):
        content += f"SET{i:02d},\"NA\"\u001c\r\n"
        content += f"RST{i:02d},\"NA\"\u001c\r\n"
    
    for i in range(1, 33):
        content += f"SV{i:02d}PU,\"0.00\"\u001c\r\n"
        content += f"SV{i:02d}DO,\"0.00\"\u001c\r\n"
    
    for i in range(1, 33):
        content += f"SC{i:02d}PV,\"1\"\u001c\r\n"
        content += f"SC{i:02d}R,\"NA\"\u001c\r\n"
        content += f"SC{i:02d}LD,\"NA\"\u001c\r\n"
        content += f"SC{i:02d}CU,\"NA\"\u001c\r\n"
        content += f"SC{i:02d}CD,\"NA\"\u001c\r\n"
    
    for i in range(1, 33):
        content += f"MV{i:02d},\"NA\"\u001c\r\n"
    
    content += "OUT103,\"TRIP OR PB04\"\u001c\r\n"
    content += "OUT101,\"HALARM OR SALARM\"\u001c\r\n"
    content += "OUT102,\"START\"\u001c\r\n"
    
    for i in range(1, 9):
        for j in ['A', 'B']:
            content += f"TMB{i}{j},\"NA\"\u001c\r\n"
    
    return content

def create_comm_content(sections):
    """
    Create content for communications settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[P1]\r\n"
    
    comm_section = sections.get('Communications', {})
    
    # Map the settings
    content += f"PROTOCOL,\"{comm_section.get('Protocol', 'Modbus')}\"\u001c\r\n"
    content += f"ADDR,\"{comm_section.get('Address', '1')}\"\u001c\r\n"
    content += f"BAUD,\"{comm_section.get('Baud', '9600')}\"\u001c\r\n"
    content += f"PARITY,\"{comm_section.get('Parity', 'None')}\"\u001c\r\n"
    content += f"STOPBITS,\"{comm_section.get('StopBits', '1')}\"\u001c\r\n"
    content += f"PORT,\"{comm_section.get('Port', 'RS485')}\"\u001c\r\n"
    content += f"STATION,\"{comm_section.get('StationName', 'Motor710')}\"\u001c\r\n"
    
    return content

def create_metering_content(sections):
    """
    Create content for metering settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[M]\r\n"
    
    metering_section = sections.get('Metering', {})
    
    # Map the settings
    content += f"DEMAND,\"{metering_section.get('Demand Interval', '15')}\"\u001c\r\n"
    content += f"ENERGY,\"{metering_section.get('Energy Format', 'kWh')}\"\u001c\r\n"
    content += f"CURSCALE,\"{metering_section.get('Current Scaling', '1.0')}\"\u001c\r\n"
    content += f"VOLSCALE,\"{metering_section.get('Voltage Scaling', '1.0')}\"\u001c\r\n"
    
    return content

def create_testing_content(sections):
    """
    Create content for testing settings
    """
    model = sections.get('Device', {}).get('Model', 'SEL-710')
    
    content = f"[INFO]\r\nRELAYTYPE={model}\r\n"
    content += "FID=SEL-710-RXXX-VX-Z008004-DXXXXXXXX\r\n"
    content += "BFID=SLBT-710-RXXX-V0-Z007004-DXXXXXXXX\r\n"
    content += "PARTNO=071001A5X6X71821210\r\n"
    content += "[R]\r\n"
    
    testing_section = sections.get('Testing', {})
    
    # Map the settings
    content += f"TESTMODE,\"{testing_section.get('TestMode', 'Disabled')}\"\u001c\r\n"
    content += f"LASTUPD,\"{testing_section.get('LastUpdate', '2025-08-30')}\"\u001c\r\n"
    
    return content

def main():
    """Main function for command line usage."""
    if len(sys.argv) != 3:
        print("Usage: python create_rdb_template.py <input_txt_file> <output_rdb_file>")
        sys.exit(1)
    
    input_txt_path = sys.argv[1]
    output_rdb_path = sys.argv[2]
    
    # Use the existing Relay710.rdb as template
    template_rdb_path = os.path.join(os.path.dirname(__file__), "Relay710.rdb")
    
    if not os.path.exists(input_txt_path):
        print(f"Error: Input file {input_txt_path} does not exist")
        sys.exit(1)
    
    if not os.path.exists(template_rdb_path):
        print(f"Error: Template file {template_rdb_path} does not exist")
        sys.exit(1)
    
    try:
        create_rdb_file(input_txt_path, output_rdb_path, template_rdb_path)
    except Exception as e:
        print(f"Error creating RDB file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()