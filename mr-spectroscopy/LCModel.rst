LCModel Analysis and Workflow
#############################

Overview
========

This section covers the full LCModel analysis workflow, including control file setup, folder organization, troubleshooting, and access to the official LCModel manual.

----

Control File Overview
=====================

The LCModel control file is a plain-text file that contains parameters controlling the LCModel analysis. Running LCModel without its GUI (from the terminal) is recommended for speed and efficiency. This approach also encourages learning the nuances of the control file parameters (see LCModel manual Section 5.3).

Example Control File
--------------------

.. code-block:: text

   $LCMODL
     key=210387309
     nunfil=1024
     title='NYUAD Siemens 3T Phantom (PRESS, TE=30ms)'
     filbas='/Users/SH7437/Desktop/LC/phantom.BASIS'
     filraw='/Users/SH7437/Desktop/LC/suppressed.RAW'
     filps='/Users/SH7437/Desktop/LC/phantom_results.ps'
     filh2o='/Users/SH7437/Desktop/LC/unsuppressed.RAW'
     doecc = T
     nsimul = 0
     hzpppm = 123.238898
     deltat = 0.0008334
   $END

Explanation of Key Parameters
-----------------------------

* **key:** Unique identifier for the run.  
* **nunfil:** Number of unfilled points.  
* **title:** Descriptive title of the study.  
* **filbas:** Full path to the basis file.  
* **filraw:** Full path to the suppressed raw data file.  
* **filps:** Full path for the output PostScript results file.  
* **filh2o:** Full path to the unsuppressed water data file.  
* **doecc:** Boolean flag for eddy current correction.  
* **hzpppm:** Frequency in parts per million.  
* **deltat:** Time between data points.

Running LCModel from the Terminal
---------------------------------

Compile and run LCModel from the terminal (without the GUI) using the compiled binary. This method significantly speeds up processing and allows for easier batch processing. To recompile from source, refer to the LCModel manual and available online instructions. The recommended practice is to write valid control files and run LCModel in terminal mode.

----

Organizing the Main Folder
==========================

Folder Structure
----------------

Create a main folder (e.g., ``/Users/SH7437/Desktop/LC``) to host all files required by LCModel. This folder should include:

* **Control File:** A text file that instructs LCModel on how to process the data.  
* **Basis File:** The `.BASIS` file generated from MRSCloud.  
* **Raw Data Files:**
  * **Suppressed Water Data:** The `.RAW` file generated from the suppressed acquisition.
  * **Unsuppressed Water Data:** The `.RAW` file for water reference data.

Keeping these files organized in one location simplifies batch processing and minimizes errors during execution.

.. image:: graphic/main.png
   :alt: LCModel folder structure
   :align: center

----

Additional Notes and Recommendations
====================================

Best Practices
--------------

1. **Data Organization**
   * Keep all related files in a single directory.
   * Use consistent naming conventions.
   * Maintain a log of processing steps.

2. **Quality Control**
   * Check raw data quality before processing.
   * Verify basis file matches experimental conditions.
   * Review LCModel output for convergence.

3. **Troubleshooting**
   * Common issues and solutions.
   * Parameter optimization tips.
   * Error message interpretation.

4. **Documentation**
   * Record all processing steps.
   * Document any manual interventions.
   * Keep track of parameter changes.

5. **Performance Optimization**
   * Batch processing recommendations.
   * Resource management.
   * Processing time optimization.

----

LCModel Manual
==============

This is the official LCModel manual.

:download:`Download LCModel Manual (PDF) <../files/lcmodel_manual.pdf>`
