## Starting the time-lapse on boot

We will be running the Pi Zero as a wearable with a USB power supply (and not with a keyboard, mouse or monitor attached), so we need a way of starting the Python script when the Zero powers on.

- Open up a terminal window

- At the terminal, type the following command:

  ```bash
  sudo nano ~/.config/lxsession/LXDE-pi/autostart
  ```

- A file will open up, add this line at the bottom of the file to automatically start your time-lapse file using Python 3:

  ```bash
  sudo /usr/bin/python3 /home/pi/time-lapse/time-lapse.py
  ```

- Press `Ctrl+X` to exit and `y` to save the changes.

- When you reboot your Raspberry Pi, the script should run. You can test this by rebooting and then looking inside the folder `/home/pi/time-lapse` to see the photographs appearing. Note that when you reboot, Python will be running in the background. You will not see any window showing that your script is running.

