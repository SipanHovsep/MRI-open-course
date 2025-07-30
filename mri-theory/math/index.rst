Mathematics for MRI
===================

Cosine transform
----------------

Idea: test whether a frequency is present by correlating the signal with a cosine at that frequency.  
If the frequency is present, the integral is **non‑zero**; if absent (and orthogonal), it is **zero**.

.. math::

   C(\nu) = \int_{-\infty}^{\infty} f(t)\,\cos(2\pi \nu t)\,dt

- For a signal lacking a given component (e.g., :math:`24\,\mathrm{Hz}`), :math:`C(24\,\mathrm{Hz}) \approx 0`.
- Orthogonality of sinusoids underlies this test.

Fourier transform
-----------------

Using Euler’s identity, a complex exponential compactly represents sine and cosine:

.. math::

   e^{\,i\theta} = \cos\theta + i\sin\theta
   \quad\Rightarrow\quad
   \cos(2\pi \nu t) + i\sin(2\pi \nu t) = e^{\,i 2\pi \nu t}

A common Fourier transform pair (unitary conventions vary):

.. math::

   F(\nu) = \int_{-\infty}^{\infty} f(t)\,e^{-i 2\pi \nu t}\,dt,
   \qquad
   f(t)  = \int_{-\infty}^{\infty} F(\nu)\,e^{+i 2\pi \nu t}\,d\nu

Phase matters
-------------

- The spectrum is **complex**: :math:`F(\nu) = |F(\nu)| e^{i\phi(\nu)}`.  
  Magnitude :math:`|F|` sets **how much**, phase :math:`\phi` sets **when/shape**.
- Time shift :math:`f(t-t_0)` adds a **linear phase ramp**:

  .. math::
     \mathcal{F}\{f(t-t_0)\} = F(\nu)\,e^{-i 2\pi \nu t_0}

- Ignoring/altering phase can distort reconstructions (ringing, shifts, asymmetric waveforms), even if the magnitude is unchanged.

Reference
---------

*Signal processing video by de Graaf*.
