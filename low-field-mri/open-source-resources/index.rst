Open source resources
=====================

Below are concise overviews of notable open‑source MRI projects with back‑links.

Shimming Toolbox
----------------
Open‑source tools for B0 shimming workflows: importing field maps, masking,
shim optimization (e.g., spherical harmonic or multi‑coil), and evaluation
pipelines for research and education.

**Website:** `Shimming Toolbox (stable) <https://shimming-toolbox.org/en/stable/>`_

PulSeq
------
Vendor‑neutral, text‑based description of MRI pulse sequences. Lets you define
RF/gradients/events once and run them on supported executors across vendors
or research consoles.

**Website:** `PulSeq <https://pulseq.github.io/>`_

MaRCoS
------
Low‑cost/open MRI control system centered on the Red Pitaya SDRlab 122‑16.
Provides server/FPGA/client stack and supports executing PulSeq definitions;
aimed at low‑field research and teaching.

**GitHub:** `MaRCoS <https://github.com/marcos-mri>`_

Gadgetron
---------
Streaming MRI reconstruction framework (C++). Uses ISMRMRD, with modular
“gadgets” pipelines for online/real‑time recon; supports integration with
custom algorithms and optional acceleration.

**Website:** `Gadgetron <https://gadgetron.github.io/>`_

BART (Berkeley Advanced Reconstruction Toolbox)
-----------------------------------------------
Command‑line MRI reconstruction toolbox. Implements parallel imaging and
compressed‑sensing methods (e.g., NUFFT, ESPIRiT calibration), plus rich
k‑space/image processing utilities for reproducible workflows.

**Website:** `BART <https://mrirecon.github.io/bart/>`_
