# The Theory

Closed-circuit-analogue-cameras (CVBS) transmit uncompressed video over unshielded (or poorly shielded) coaxial cables.
- The baseband composite video signal (CVBS) occupies roughly 0-6 MHz:
  * Sync pulses at ~15.6 kHz (line) and 50/60 Hz (frame).
  * Luminance (Y) up to ~4.2 MHz.
  * Chrominance (C) on a colour subcarrier at 3.58 MHz (NTSC) or 4.43 MHz (PAL).
- A coaxial cable acts as an unintentional antenna if poorly shielded or improperly terminated.
- This leakage can radiate into the environment, allowing side-channel capture using sensitive radio receivers.

## My Hypothesis

If wireless camera emissions can be intercepted and reconstructed (refer to the article below), then wired analogue CVBS over coax should likewise leak sufficient RF energy to permit reconstruction of *(albeit degraded but recognisable)* video frames.

## Reference
An article on the research from Northeasten University: https://news.northeastern.edu/2024/02/08/security-camera-privacy-hacking/
