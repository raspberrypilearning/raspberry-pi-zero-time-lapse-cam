## What you will need

### Hardware

* Raspberry Pi Zero with soldered on header
* Blinkt (optional)
* Micro USB power pack
* Pi Camera or Pi NoIR Camera
* Pi Zero compatible camera cable

### Software

#### Software Installation

If you are using the optional Blinkt, you will need to install the library code on your Raspberry Pi Zero. This requires an internet connection.

If you are using a Raspberry Pi Zero without wireless connectivity, you can either:

1. Connect the Raspberry Pi Zero to the internet using a USB dongle

1. Transfer your SD card into a Raspberry Pi with an internet connection to install the libraries, then transfer it back to the Raspberry Pi Zero.

Once you are connected to the internet, run the following command in the terminal:

```bash
sudo apt-get install python3-blinkt
```
More information can be found on the [Getting started with Blinkt](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt) page on the Pimoroni website.
