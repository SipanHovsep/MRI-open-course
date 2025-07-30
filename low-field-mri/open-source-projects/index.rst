Open source projects
====================

MaRCoS
------

The Magnetic Resonance Control System (MaRCoS) uses the same versatile
hardware; however, its software, firmware, and FPGA firmware have been replaced
to go beyond the limitations of OCRA, which included constraints on sequence
length, complexity, and timing precision, as well as being written in low‑level
``assembly``‑style sequence programming. MaRCoS represents a complete rewrite of
the server, FPGA firmware, and client software, based on a MessagePack
(``msgpack``)‑based protocol that also supports the open‑source PulSeq
hardware‑independent sequencing language. The core of MaRCoS is the Red
Pitaya SDRlab 122–16, a commercial board with two analog inputs for digitizing
received data and two analog outputs for generating RF transmit waveforms, with
a bandwidth of around 50 MHz, making it suitable for proton MRI at field
strengths of up to 1.17 Tesla.


