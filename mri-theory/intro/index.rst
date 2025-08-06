Course Introduction
===================

The role of models in learning MRI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MRI is complex and multidisciplinary field having theoretical origins rooting from quantum mechanics and
utilizing the modern feet of cutting edge engineering methods to hide complexities into simple looking
tunnel-like machine.


MRI stands for Magnetic Resonance Imaging and we will take these terms as starting point by understanding
how images are constructed utilizing phenomenon of magnetic resonance. Historically magnetic resonance phenomenon
preceeds the imaging, thus we will start from the origins of magnetic resonance phenomenon.
MRI was called the most significant medical imaging invention after X ray.

The learning journey would be accompanied by models and analogies, however, before using them, its good to understand
few fundamental truths about the models.

.. admonition:: Quote
   :class: quote

      “All models are wrong, but some are useful.”

   .. container:: quote-attrib

      — George E. P. Box

.. admonition:: Quote
   :class: quote

   Imagine that … the world is something like a great chess game being played by the gods, and we are observers of the game.
   … If we watch long enough, we may eventually catch on to a few of the rules…. However, we might not be able to understand
   why a particular move is made in the game, merely because it is too complicated and our minds are limited….
   We must limit ourselves to the more basic question of the rules of the game.
   If we know the rules, we consider that we “understand” the world.

   .. container:: quote-attrib

      — Richard P. Feynman



Historical precedings
^^^^^^^^^^^^^^^^^^^^^



Stern-Gerlach Experiment
------------------------

**(Brilliant experimentally, wrong theoretically)**



Otto Stern "hated" Bohr's model so much (Calling it Bohr's nonsence) that he set up an experiment to prove it wrong.
While doing so, he created one of the most elegant ways to prove it right.
Performed at 1922, this experiment became on of the most fundamental experiments even done in quantum mechanics.

Bohr's model suggested that electrons orbit the nucleus in a discrete, quantized orbits. As electrons are charged and
moving charges created magnetic field, Otto Stern set the experiment to test whether orbital momentum and the arising magnetic fields
were quantized or not, with initial expectation that they would not.

.. image:: images/apparatus.png

The apparatus was simple, featuring a furnace to heat up silver and emit electrons and inhomogeneous magnetic field to
generate predicted normal distribution.
However, they got the contrary they expected and exactly as Bohr's model predicted: quantized distribution.

.. raw:: html

   <div style="display: flex; gap: 20px;">

.. image:: images/expectation.png
   :width: 100%

.. image:: images/reality.png
   :width: 100%

.. raw:: html

   </div>

As in 1922, the spin had not been discovered yet, they concluded their experiment with "Space Quantization" of angular momentum
which then later, would have become known as spin. The experiment was the first to prove that on atomic level, angular momentum
and resulting magnetic moment are "quantized"


.. image:: images/result.png
The image is taken from the Stanford Encyclopedia of Philosophy [1]_.


.. admonition:: Nobel Prize
   :class: nobel

   .. container:: nobel-content

      .. container:: nobel-text

         The 1943 Nobel prize was awarded to Otto Stern "for
         his contribution to the development of the molecular ray method
         and his discovery of the magnetic moment of the proton"

      .. image:: /_static/Nobel_Prize.png
         :class: nobel-medal
         :alt: Nobel Prize medal



https://physicsworld.com/a/how-the-stern-gerlach-experiment-made-physicists-believe-in-quantum-mechanics/
https://plato.stanford.edu/entries/physics-experiment/app5.html
https://www.youtube.com/watch?v=pcGIBacW-q0
https://www.youtube.com/watch?v=PH1FbkLVJU4
https://www.youtube.com/watch?v=QP3SfF9H1MY




Pauli Exclusion Principle
-------------------------

Pauli came up with the idea of two possible values of the spin of the electrons: "spin up" or "spin down", and further
formulated that two electrons can't have the same spin values, known as Pauli exclusion principle.




.. admonition:: Nobel Prize
   :class: nobel

   .. container:: nobel-content

      .. container:: nobel-text

         The 1945 Nobel prize was awarded to Wolfgang Pauli for discovery of
         the exclusion principle: a fundamental principle in quantum mechanics, stating
         that no two electrons in an atom can have the same set of quantum numbers.

      .. image:: /_static/Nobel_Prize.png
         :class: nobel-medal
         :alt: Nobel Prize medal


The Birth of Nuclear Magnetic Resonance: NMR
--------------------------------------------

**Isidor's Rabi's extension of Stern-Gerlach experiment**


The most significant step laying the groundwork for "resonance" aspect of MRI and NMR (same R), was performed by Isidor Rabi at 1937.
He modified the Stern-Gerlach setup by adding an oscillating magnetic field and showing that they are able to change the spins.
Instead of silver atoms originally used by Stern-Gerlach, he used Lithium Chloride (LiCl). His contribution was adding a radiofrequency
coil to modify the magnetic field and then observed that it led to change in observed proportions of spin up and down electrons on the
photo plate.

With this results he claimed that it would be possible to identify individual atoms by their characteristic pattern of resonant frequency.

.. image:: images/rabi.png
The image is taken from the Questions and Answers in MRI [2]_.

The simple figure shows significant decrease in beam intensity at resonant frequency, which was achieved by controlling the
amperage of radiofrequency coil (magnetic field induced by RF coil was proportional to current).

.. admonition:: Nobel Prize
   :class: nobel

   .. container:: nobel-content

      .. container:: nobel-text

         The 1944 Nobel prize was awarded to Isidor Isaac Rabi "for his resonance method for recording the magnetic properties
         of atomic nuclei".

      .. image:: /_static/Nobel_Prize.png
         :class: nobel-medal
         :alt: Nobel Prize medal


Rabi also became the first to use the term Nuclear Magnetic Resonance (NMR), which then became irreplacable technique in chemistry to understand
molecular structures.

In simpler terms the idea of magnetic resonance or resonance phenomenon in general, can be explained using a simpler analogy from
*Home Alone* movie.

.. image:: images/home_alone.png

When the same question is asked by the villain, Kevin gives no response, because the Villain's voice is different than a trusted
person, such as mother, to whom he gives a response. As the frequency is fundamental characteristics of the voice, we can tell that ``wrong frequency`` led ``no response``.
And similarly, when the mother "generates" the ``right frequency`` a ``response is received``.



Moving from isolated gas-phase atoms to solids and liquids (bulk material)
--------------------------------------------------------------------------

Magnetic resonance in individual atoms was already quite fascinating phenomenon, but not of quite applicability, as in daily life
we dont come across with individual atoms. Thus it was important to test on bulk matter (liquids, solids) and understand whether the same
phenomenon applies on macroscopic levels or not.

The same experiment was independently done by Felix Bloch (Standford University) and Edward Mills Purcell at MIT, where they did the experiment
with Water (Purcell's group) and paraffin (Bloch's group).

.. raw:: html

   <div style="display: flex; gap: 20px;">

.. image:: images/Purcell.png
   :width: 100%

.. image:: images/Bloch.png
   :width: 100%

.. raw:: html

   </div>

The image is taken from the Questions and Answers in MRI [2]_.

.. admonition:: Nobel Prize
   :class: nobel

   .. container:: nobel-content

      .. container:: nobel-text

         The 1952 Nobel prize was awarded to jointly to Felix Felix Bloch
         and Edward Mills Purcell "for their development of new methods for
         nuclear magnetic precision measurements and discoveries in connection therewith"

      .. image:: /_static/Nobel_Prize.png
         :class: nobel-medal
         :alt: Nobel Prize medal

Its worth to appreciate the simplicity of design featured in Bloch's notebook, which featured Nobel Prize winning research.

.. image:: images/Notebook.png


.. rubric:: References

.. [1] Stanford Encyclopedia of Philosophy. *Physics Experiment, App 5*.
   <https://plato.stanford.edu/entries/physics-experiment/app5.html>_
.. [2] Questions and answers in MRI. *The discovery of NMR*.
   <https://mriquestions.com/who-discovered-nmr.html>_