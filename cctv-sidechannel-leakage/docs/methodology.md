## The Methodology

## Baseline Testing
- Connect a CVBS analogue camera to a monitor via coax
- Place loop antenna 0.5-2m away from the cable
- Configure RTL-SDR in Direct Sampling Q-branch mode
- Tune 0.5-10 MHz, record IQ samples
- Look for recurring line-rate (15.6 kHz) and frame-rate (50/60 Hz) sidebands
  
## Signal Characterisation
- Perform FFT to identify harmonics of sync pulses
- Attempt to decode composite baseband by applying AM/FM demod
- Compare captured signals against the known video source

## Proof of Concept (PoC)
- Reconstruct video using signal processing (even ghostly outlines suffice)
- Perhaps pipe both the original camera footage and the reconstructed camera footage to a neural network and train it to make reconstructed frames more accurate

## References
- [Northeastern University (2024). Security Camera Privacy Risks: Wireless Cameras Leak Video Signals](https://news.northeastern.edu/2024/02/08/security-camera-privacy-hacking/)
- [Cook, M. Practical RF Circuit Design for Modern Wireless Systems](https://uodiyala.edu.iq/uploads/PDF%20ELIBRARY%20UODIYALA/EL96/Artech%20House%20-%20Practical%20Rf%20Circuit%20Design%20For%20Modern%20Wirele.pdf)
- [RTL-SDR Blog. Direct Sampling Mode Explained](https://www.rtl-sdr.com/rtl-sdr-direct-sampling-mode/)
- [ITU-R BT.470-6. Conventional Television Systems](https://www.itu.int/dms_pubrec/itu-r/rec/bt/r-rec-bt.470-6-199811-s!!pdf-e.pdf)
