## What you will make

In this resource you will make a wearable time-lapse camera using a Raspberry Pi Zero.

--- collapse ---
---
title: What you will learn
---
By creating the time-lapse camera with your Raspberry Pi Zero you will learn:

- How to set up a Raspberry Pi Camera Module
- How to take pictures automatically
- How to control GPIO pins on the Raspberry Pi Zero
- How to set up a script to run automatically on boot

This resource covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](https://www.raspberrypi.org/curriculum/):

- [Design basic 2D and 3D assets](https://www.raspberrypi.org/curriculum/design/creator)
- [Combine programming constructs to solve a problem](https://www.raspberrypi.org/curriculum/programming/builder)
- [Combine inputs and/or outputs to create projects or solve a problem](https://www.raspberrypi.org/curriculum/physical-computing/builder)
- [Can use and manipulate upcycled materials for use in prototypes](https://curriculum.raspberrypi.org/manufacture/creator/)
--- /collapse ---

--- collapse ---
---
title: What you will need
---
### Hardware

* Raspberry Pi Zero with soldered on header
* Blinkt (optional)
* Micro USB power pack
* Pi Camera or Pi NoIR Camera
* Pi Zero compatible camera cable

### Software

If you are using the optional Blinkt, you will need to install the library code on your Raspberry Pi Zero. This requires an internet connection.

If you are using a Raspberry Pi Zero without wireless connectivity, you can either:

1. Connect the Raspberry Pi Zero to the internet using a USB dongle

1. Transfer your SD card into a Raspberry Pi with an internet connection to install the libraries, then transfer it back to the Raspberry Pi Zero.

Once you are connected to the internet, run the following command in the terminal:

```bash
sudo apt-get install python3-blinkt
```
More information can be found on the [Getting started with Blinkt](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt) page on the Pimoroni website.

--- /collapse ---
