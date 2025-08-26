MR Physics Fundamentals
=======================



.. epigraph::

   Imagine a spinning charge—except it's not a charge and it's not literally spinning.
    :align: center


Trying to understand the Spin
------------------------------

- *What is spinning?*
- Every single particle is moving in a circular path around a common center and they all take the same time to finish the circle. Its important to note that individual particles don’t spin, they move in circular path.

- Therefore, a conclusion can be made that Spin is Emergent property.

- *Why electrons can’t spin?*
- Because electrons are fundamental particles, thus they are not made up of any smaller particles. For spinning we need group of particles, therefore electron can’t spin.

- *Why its hard to imagine?*
- Because we live in macroscopic world and even the smallest particle we imagine, is still made up of smaller particles.

- *Then if they don’t spin, why we still think in terms of spinning?*
- Because magnetism arises from moving charge, and if we had a group of charged particles spinning on their own axis we would observe a similar magnetic moment as single electron possesses.

- *Then why we don’t call that property a “quantum magnet”?*
- Because there is additional property which is also unique to spinning: Take a tabletop, which would instantly fall if placed vertically without spinning, however, once it spins, it resists the turning forces (or torques), while performing special motion called precession. The ability of spinning object to resist turning forces is called Angular momentum.

- *How can we check whether an invisible object is spinning or not?*
- We can apply a turning force and study its reaction, if it does not resist, then it does not have angular momentum, if it resists, then it has an angular momentum, thus spins.

- *How can we design such an experiment for electron?*
- Using the fact that electrons have magnetic moment, we can put them in stronger magnetic field which will try to re-orient the electron by applying torque to it.

- The experiment proved that electron is resisting and thus have an angular momentum.

- So in summary, we saw that charged electron has both angular and magnetic momentum, which are two characteristic properties for spinning charge, but also we assured ourselves that its not actually spinning.

- Its similar to say that an “unknown” animal exists in alien worlds which weights around 1 ton, has a long trunk and big ears and behaves like an elephant, but it is NOT elephant.

- And because we don’t live in alien word, our closest approximation would be to call that animal an “elephant” bearing in mind that still, its not an elephant.




Classical view
--------------

A **single** spin can be pictured as a tiny bar magnet, but MRI measures magnetization in **bulk matter** (more than :math:`10^{23}` spins per liter). Even in strong fields, the macroscopic behavior differs from a single magnet: the static field biases spins while thermal energy randomizes them. The balance gives a non‑zero equilibrium magnetization :math:`M_0`.

Spin: angular momentum and magnetic moment
-----------------------------------------

Nuclei with an odd number of protons and/or neutrons exhibit **spin angular momentum**:

.. math::

   \mathbf{S} = \hbar \mathbf{I}, \qquad \hbar = \frac{h}{2\pi}

The associated magnetic dipole moment is

.. math::

   \boldsymbol{\mu} = \gamma \mathbf{S},

where :math:`\gamma` is the gyromagnetic ratio.

Interaction with magnetic fields
--------------------------------

1. **Static main field** :math:`B_0`

   Spins tend to align with :math:`B_0`, producing :math:`M_0` along :math:`z`. They precess at the **Larmor frequency**:

   .. math::

      \omega_0 = \gamma B, \qquad f = \frac{\omega_0}{2\pi} = \frac{\gamma B}{2\pi}

   Here :math:`B` is the **local** field experienced by the nucleus (shielding leads to **chemical shift**).

2. **RF field** :math:`\mathbf{B}_1(t)`

   The RF field is applied transverse to :math:`B_0` (no :math:`z`‑RF needed). At resonance, :math:`\mathbf{B}_1` tips the magnetization to create transverse components detectable by receiver coils (Faraday’s law). Modern systems often use separate transmit and receive coils optimized for specific anatomy.

3. **Linear gradients** :math:`\mathbf{G}(t)`

   Spatial localization uses linear gradients (e.g., :math:`10\,\mathrm{mT/m}`), superimposed on :math:`B_0` to encode position.

Bloch equation (no relaxation)
------------------------------

Magnetic moment in a field experiences a torque:

.. math::

   \boldsymbol{\tau} = \boldsymbol{\mu} \times \mathbf{B}, \qquad
   \frac{d\mathbf{J}}{dt} = \boldsymbol{\tau}, \qquad
   \boldsymbol{\mu} = \gamma \mathbf{J}

Combining gives the **Bloch precession equation**:

.. math::

   \frac{d\boldsymbol{\mu}}{dt} = \gamma \boldsymbol{\mu} \times \mathbf{B}
   \quad\Longleftrightarrow\quad
   \frac{d\mathbf{M}}{dt} = \mathbf{M} \times \gamma \mathbf{B}.

With :math:`\mathbf{B} = (0,0,B_0)^\mathsf{T}`:

.. math::

   \frac{d}{dt}
   \begin{bmatrix}
   \mu_x\\ \mu_y\\ \mu_z
   \end{bmatrix}
   =
   \gamma
   \begin{bmatrix}
   \mu_y B_0\\ -\mu_x B_0\\ 0
   \end{bmatrix}
   =
   -\omega_0
   \begin{bmatrix}
   \mu_y\\ -\mu_x\\ 0
   \end{bmatrix},
   \qquad \omega_0 = -\gamma B_0 .

Solutions (precession at :math:`\omega_0`):

.. math::

   \mu_x(t) = a\cos(\omega_0 t + \phi),\quad
   \mu_y(t) = a\sin(\omega_0 t + \phi),\quad
   \mu_z(t) = \text{const}.

Rotating frame transformation
-----------------------------

An RF field oscillating at :math:`\omega_0` can be written as

.. math::

   \mathbf{B}_1(t) = B_1
   \begin{bmatrix}
   \cos(\omega_0 t + \phi)\\
   \sin(\omega_0 t + \phi)\\
   0
   \end{bmatrix}.

In a frame rotating at :math:`\omega_0`, this becomes **static**:

.. math::

   \mathbf{B}_1^{(\text{rot})} = B_1
   \begin{bmatrix}
   \cos\phi\\
   \sin\phi\\
   0
   \end{bmatrix}.

Choice of phase :math:`\phi` sets the effective RF axis in the rotating frame.

Bloch equation with relaxation
------------------------------

A phenomenological form including relaxation:

.. math::

   \frac{d\mathbf{M}}{dt}
   = \mathbf{M} \times \gamma \mathbf{B}
     - \frac{M_x \,\hat{\imath} + M_y \,\hat{\jmath}}{T_2}
     - \frac{(M_z - M_0)\,\hat{k}}{T_1},

where :math:`M_0` is the thermal equilibrium magnetization.

Excitation and polarization
---------------------------

A static transverse field has negligible effect; **resonant** :math:`\mathbf{B}_1(t)` is required. A linearly polarized RF field can be decomposed into two counter‑rotating circular components; only the component co‑rotating with the spins is **on‑resonance** (principle behind circularly polarized transmit/receive).

Ignoring relaxation during a short RF pulse:

.. math::

   \frac{d\mathbf{M}}{dt} = \mathbf{M} \times \gamma\big( \mathbf{B}_0 + \mathbf{B}_1(t) \big),
   \qquad \omega_0=\gamma B_0,\ \ \omega_1(t)=\gamma B_1(t).

Relaxation
----------

We lose **transverse** magnetization primarily due to loss of **phase coherence**, not because longitudinal magnetization is reduced by tipping.

- :math:`T_1` (spin–lattice): recovery of :math:`M_z` (typically 100–1500 ms).
- :math:`T_2` (spin–spin): decay of :math:`M_{xy}` from microscopic irreversible dephasing (typically 20–300 ms).
- :math:`T_2^*`: additional macroscopic, reversible dephasing from field inhomogeneity; :math:`T_2^* < T_2`. Good shimming brings :math:`T_2^* \to T_2`.

**Longitudinal relaxation**

.. math::

   \frac{d M_z}{dt} = -\frac{(M_z - M_0)}{T_1}
   \quad\Longrightarrow\quad
   M_z(t) = M_0 + \big(M_z(0)-M_0\big)\,e^{-t/T_1}.

After a :math:`90^\circ` pulse, :math:`M_z(0)=0`:

.. math::

   M_z(t) = M_0 \big(1 - e^{-t/T_1}\big).

**Transverse relaxation**

.. math::

   \frac{d M_{xy}}{dt} = -\frac{M_{xy}}{T_2}
   \quad\Longrightarrow\quad
   M_{xy}(t) = M_{xy}(0)\,e^{-t/T_2}.
   \ (\text{For }90^\circ,\ M_{xy}(0)=M_0)

Signal equation & detection
---------------------------

Signal amplitude is proportional to the transverse magnetization. The received signal is the superposition of contributions over the excited volume:

.. math::

   s(t) = \int_{\text{vol}} M(\mathbf{r},t)\, dV
        = \int\!\!\!\int\!\!\!\int M(x,y,z,t)\, dx\,dy\,dz.

**Quadrature detection** measures two orthogonal channels (cosine/sine), improving SNR and resolving frequency sign (since :math:`\cos(f)=\cos(-f)` but :math:`\sin` changes sign). The complex representation combines them as real and imaginary parts.

Magnetism
---------

Biot–Savart law
^^^^^^^^^^^^^^^

The magnetic field contribution :math:`dB` from a current element :math:`I\,d\boldsymbol{\ell}` at point :math:`P` is

.. math::

   dB \propto \frac{I\, d\ell \,\sin\alpha}{R^2}
   \quad\Longrightarrow\quad
   dB = k\, \frac{I\, d\ell \,\sin\alpha}{R^2},

with proportionality constant :math:`k` and distance :math:`R` from the element to :math:`P`.

Ampère’s law
^^^^^^^^^^^^

The line integral of :math:`\mathbf{B}` around a closed loop equals the enclosed current:

.. math::

   \oint \mathbf{B}\cdot d\boldsymbol{\ell} = \mu_0\, I_{\text{enclosed}}.




