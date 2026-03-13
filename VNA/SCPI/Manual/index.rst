Collecting Raw Measurements
===========================

To perform an offline or custom calibration, you must collect the "raw" (uncorrected) S-parameters of your physical standards (Short, Open, and Load). By disabling the internal VNA correction, we capture the raw transfer function of the cables and connectors, which ``scikit-rf`` will later use to calculate the error terms.

Implementation
--------------

The following script sets a high-resolution sweep (17,901 points) to ensure maximum precision across the 18 GHz span and saves the resulting data as a complex Touchstone file.

.. code-block:: python
   :linenos:

   import pyvisa

   rm = pyvisa.ResourceManager()
   vna = rm.open_resource('TCPIP0::10.0.0.5::hislip0::INSTR')
   vna.timeout = 120000

   # Disable internal VNA correction to get "dirty" raw data
   vna.write("SENSe1:CORRection:STATe OFF")
   print("Correction state:", vna.query("SENSe1:CORRection:STATe?"))

   # Set frequency range and high-density points
   vna.write("SENSe1:FREQuency:STARt 100e6")
   vna.write("SENSe1:FREQuency:STOP 18e9")
   vna.write("SENSe1:SWEep:POINts 17901")

   # Execute a single sweep and wait for completion
   vna.write("SENSe1:SWEep:MODE SINGle")
   vna.query("*OPC?")

   # Export the trace for Port 1 as a complex .s1p file
   vna.write("MMEMory:STORe:TRACe:PORTs 1, 'load_raw.s1p', COMPlex, 1")

   print("Done. load_raw.s1p saved.")
   print(vna.query("MMEMory:CDIRectory?"))

   vna.close()
   rm.close()

Terminal Output
---------------

.. code-block:: text

   Correction state: 0
   Done. load_raw.s1p saved.
   'C:\Users\Public\Documents\Rohde-Schwarz\ZNL\Save\'

Technical Breakdown
-------------------

* **Correction State 0**: We verify that the VNA is not applying any internal calibration. This is essential because we want to measure the "errors" of the system so that we can characterize them ourselves.
* **17,901 Points**: For a sweep from 100 MHz to 18 GHz, this provides a 1 MHz resolution per point. This high density is preferred when performing time-domain analysis or when the measurement setup involves long cables that create rapid phase rotations.
* **SINGle Sweep & \*OPC?**: High-point count sweeps take significant time. Using ``SINGle`` mode combined with the ``*OPC?`` (Operation Complete) query ensures that Python waits for the VNA hardware to finish the entire 18 GHz sweep before attempting to save the file.
* **COMPlex Format**: Standard S-parameter files can be saved in Magnitude/Phase format, but ``COMPlex`` (Real/Imaginary) is the most robust format for mathematical processing in ``numpy`` and ``scikit-rf``.
