MRI Pulse Sequences Overview
============================

Sequence families
-----------------

- **Spin-echo family**: SE, multi-echo, FSE/TSE
- **Gradient-echo family**: GRE, FLASH, bSSFP/FIESTA, EPI
- **Inversion-recovery**: STIR, FLAIR, DIR, PSIR
- **Diffusion**: DWI, DTI, HARDI, multi-shell
- **Perfusion & flow**: ASL, DSC/DCE, TOF-MRA, phase-contrast
- **Quantitative maps**: :math:`T_1` (MOLLI, VFA), :math:`T_2/T_2^*`, :math:`T_{1\rho}`, :math:`B_1`, :math:`B_0`
- **Functional & rapid**: BOLD-EPI, multiband/SMS, cine
- **Spectroscopy**: PRESS, STEAM, MEGA-PRESS, semi-LASER
- **Magnetization transfer & CEST protocols**
- **Accelerated methods**: parallel imaging (SENSE/GRAPPA), compressed sensing


Pulse design and contrast
-------------------------

Combinations of excitation pulses are typically chosen so the measured signal amplitude becomes a function of MR parameters
:math:`(\rho, T_1, T_2)`.

.. note::

   Gradient fields are **double‑edged swords**:
   - Needed for spatial localization.
   - Turning them **on** increases dephasing and destroys some signal.
     To recover signal, apply an **opposite polarity** gradient with the **same area** (often higher amplitude, shorter time) to rephase.


.. admonition:: Why *not* undo :math:`G_{\text{phase}}` and :math:`G_{\text{freq}}` afterwards?

   - The phase shift from the **phase‑encoding gradient** *is* the spatial encoding.
     If you undo it, you remove spatial encoding from the image.
   - For the **frequency‑encoding gradient (FEG)**, you cannot simply apply an opposite gradient *after* readout because the echo and
     sampling are already finished at :math:`\mathrm{TE}`.
     Instead, you compensate **in advance** with a prephasing gradient (you de‑phase once, then re‑phase during readout).

.. admonition:: Why are there multiple :math:`G_{\text{phase}}` pulses?

   Each repetition uses a **different phase‑encoding strength** to fill a different **row of k‑space**.
   Repeating across many phase encodes fills the full k‑space matrix.


Repetition effects and Ernst angle
----------------------------------

For a **single** excitation, a :math:`90^\circ` pulse yields the most transverse signal.
When repeated, **TR** influences the optimal flip angle because longitudinal magnetization may not fully recover between excitations.

**Ernst angle**: optimal flip angle depending on :math:`T_1` and **TR**; with short **TR**, often :math:`\alpha < 90^\circ`.


Spin‑Echo (SE)
--------------

1. Apply :math:`G_{\text{slice}}` **during** the RF excitation; otherwise the entire volume is excited.
2. Apply an **opposite‑polarity** slice‑selection gradient lobe to:
   - Rephase dephasing caused by :math:`G_{\text{slice}}`.
   - Refocus spins within the selected slice.
   - Avoid unwanted signal from outside the slice.
3. Apply a :math:`180^\circ` refocusing pulse (with appropriate gradient schemes, e.g., crusher/phase gradients) to control slice cross‑talk and coherence pathways.
4. Wait after the :math:`180^\circ` pulse for dephasing to refocus into the **spin echo** at :math:`\mathrm{TE}`.


Gradient‑Echo (GRE)
-------------------

- No :math:`180^\circ` refocusing pulse.
- No post‑:math:`180^\circ` waiting period as in SE; echoes formed by gradient polarity/area manipulations.
- Generally **faster** and more flexible due to gradient control.
- Typically :math:`\alpha \neq 90^\circ` (small flip angles common).


Inversion‑Recovery (IR)
-----------------------

Basic form:

.. math::

   180^\circ \; \rightarrow \; \text{(wait } TI \text{)} \; \rightarrow \; \text{readout (e.g., SE)}

- **:math:`TI`**: inversion time between the :math:`180^\circ` pulse and the readout that sets which tissue is attenuated or nulled.

STIR (Short TI Inversion Recovery)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Chooses a **short** :math:`TI` to null **short :math:`T_1`** tissues (e.g., fat).
- Useful for **artifact suppression** (implants/metal).
- **Downsides**:
  - Longer **TR** → longer acquisition time.
  - Not compatible with **T1‑shortening contrast agents** (contrast effect is suppressed by fat‑nulling).
  - Reduced **SNR**.

FLAIR (Fluid‑Attenuated Inversion Recovery)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Uses a **long** :math:`TI` to null **fluid** (e.g., CSF).
- Helps **differentiate lesions** from ordinary fluids, enhancing lesion conspicuity adjacent to CSF spaces.
