================================================
VNA Automatic Calibration via SCPI
================================================

Introduction
============

This chapter describes how to automate the calibration process of a Vector Network Analyzer (VNA) 
using **Standard Commands for Programmable Instruments (SCPI)** and Python. 

Calibration is the most critical step in RF measurements. It mathematically removes the 
systematic errors (Directivity, Source Match, and Reflection Tracking) introduced by the VNA 
hardware and cables, shifting the measurement plane to the end of the test port.

Objectives
----------

This tutorial serves two primary purposes:

1. **Practical Application**: To perform a "Full One-Port" (FOPort) automatic calibration 
   required for accurate reflection measurements (S11) up to 18 GHz.
2. **Skill Development**: To provide a hands-on example of how to communicate with high-end 
   test equipment using the PyVISA library and raw SCPI strings.

System Requirements
===================

* **Hardware**: Rohde & Schwarz ZNL series VNA and a compatible Automatic Calibration Unit (e.g., ZN-Z151).
* **Connection**: Ethernet (TCP/IP) via HiSLIP protocol.
* **Libraries**: ``pyvisa``, ``numpy``.

Implementation
==============

The following Python script initializes the instrument, sets the frequency sweep from 100 MHz 
to 18 GHz, and triggers the internal AutoCal routine.

.. code-block:: python
   :linenos:

   import pyvisa

   # Initialize communication
   rm = pyvisa.ResourceManager()
   vna = rm.open_resource('TCPIP0::10.0.0.5::hislip0::INSTR')
   vna.timeout = 120000  # Calibration hardware takes time to switch internal states

   # Reset the instrument to default state
   vna.write("*RST")

   # Set frequency range: 100 MHz to 18 GHz
   vna.write("SENSe1:FREQuency:STARt 100e6")
   vna.write("SENSe1:FREQuency:STOP 18e9")
   vna.write("SENSe1:SWEep:POINts 1001")

   # Run autocal on port 1 using factory characterization ('')
   # The VNA automatically detects the CalUnit connected to Port 1
   vna.write("SENSe1:CORRection:COLLect:AUTO '', 1")
   
   # *OPC? is vital: it pauses the script until the VNA hardware is finished
   vna.query("*OPC?") 

   # Verify calibration status
   state = vna.query("SENSe1:CORRection:STATe?").strip()
   print(f"Calibration active: {state}")  # 1 = Success/Active

   # Save the resulting calibration data to the internal storage
   vna.write("MMEMory:STORe:CORRection 1, 'AutoCal_Port1.cal'")

   vna.close()
   rm.close()

   # Later load with
   #vna.write("MMEMory:LOAD:CORRection 1, 'AutoCal_Port1.cal'")

Command Breakdown
=================

* ``SENSe1:CORRection:COLLect:AUTO '', 1``: The empty string tells the VNA to use the factory 
  data stored inside the CalUnit. The ``1`` specifies the physical Port 1 of the VNA.
* ``*OPC?``: Stands for "Operation Complete." It prevents the script from closing the 
  session before the physical switches inside the CalUnit have finished cycling.
