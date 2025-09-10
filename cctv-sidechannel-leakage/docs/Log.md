# NOTES/PROGRESS/UPDATES
I will be logging my progress, or whatever trials/tribulations I face within this document.
Naturally, I'll update this post as progression continues.

### Progress thus far:
- Wired CCTV system set up
- The device has been assembled fully
- I have configured the SDR to direct sampling mode in order to pick up frequencies under 10MHz
- I have found the range in which the leaked EM emissions reside
- I have succesfully received leaked EM messions from the CCTV cables

### Problems:
- I had ordered the wrong BNC adapter for my camera set up: To fix this issue I simply bought the correct Male-Male BNC-RCA adapter the CCTV setup required,
- The wide-band Balun module needed for my loop antenna to function was broken, one of its input SMA ports was loose. After carefully opening the Balun, I came to the unfortunate discovery that the wire that should've been connected to the SMA port was disconnected. After failing to solder the wire to the SMA jack, I then ordered a replacement.
- After countless hours of only receiving noise, I figured something was direly wrong. At first I speculated that it was an issue with GQRX, but after using other spectrum analysis tools and reaching this same point I knew that couldn't have been the case. After my troubleshooting process however, I realised that it was an issue with the antenna. (I had unscrewed the singular loop antenna from the Balun, no difference was made, but when I had unplugged the SDR I would notice that everything I was seeing would disappear, which led me to believe that the issue was solely my antenna). My antenna set-up was fundamentally flawed. I was trying to use a singular loop antenna, this wouldn't work. What I needed to do was to join 2 loop antennas, with the use of a phase inverter box, then to plug in the 1 remaining port from each of the antenna into the Balun. Once I had done this, the set up worked.
- The power source for both the Pi and the display emits EM emissions as well, which the antenna would also pick up. This creates unwanted noise and is a huge problem considering the device I'm making is portable, the powersupply was right on the antenna. I tried to mitigate this issue by placing ferrite chokes on the power cables and also by moving the power source further from the antenna. There is still some inevitable noise, perhaps I could make use of a Faraday cage around the supply, or something similair.

### Next steps
- Reconstructing the image frames in real time using a python program
- Training a neural network to make the reconstructed images more accurate
