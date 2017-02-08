# Raspberry Pi Zero Timelapse Camera

In this resource you will make a wearable timelapse camera using a Raspberry Pi Zero.

## Deciding on your wearable

First, you need to decide what kind of wearable you would like to make. The Raspberry Pi Zero is very small and portable so you can wear it in a variety of different ways. Here are two examples of wearable timelapse cameras you could make with a Raspberry Pi Zero:

1. You could use a lanyard to make a wearable camera that hangs around your neck. Your USB power pack could be stored in a shirt pocket near to the camera.

  ![Lanyard timelapse cam](images/james-timelapse.png)

1. You could attach your timelapse camera to a pair of sunglasses so that it can literally see what you see.

  ![Timelapse cam as glasses](images/timelapse-specs.png)

1. Or, you may have your own idea for how you would like to wear your timelapse camera! The most important thing to remember is that your wearable timelapse camera will *not* be waterproof, so don't wear it outside in the rain (or in the shower).

## Attaching a header to the Raspberry Pi Zero

If you would like to include the optional lights on your wearable using the Blinkt, your Raspberry Pi Zero will need a male header for the Blinkt to attach to, which must be soldered on. (If you don't want to solder, you could try the [hammer header](https://shop.pimoroni.com/products/gpio-hammer-header) instead.)

1. If your header is longer than the number of pins needed, carefully break it off to the right length. Insert the header into the holes in the Raspberry Pi Zero with the longer pins facing upwards.

  ![Pi zero front](images/pi-zero-front.png)

1. Keeping the header pressed in, turn both the Raspberry Pi Zero and the header over. To make soldering easier, put a blob of blue tack under the Raspberry Pi Zero on the long edge opposite the header to keep it level and stop it from moving around whilst you solder. Make sure the Raspberry Pi Zero is flush with the header before beginning to solder.

1. Using a soldering iron, carefully solder each of the pins on the header to the Raspberry Pi Zero, making sure there is enough solder to create a good connection for each one.

  ![Pi zero back](images/pi-zero-back.png)

## Setting up the software

If you are using the optional Blinkt, you will need to install the library code on your Raspberry Pi Zero, which requires an internet connection.

You can either:

- Connect the Raspberry Pi Zero to the internet using a USB to Ethernet dongle
- If you have a Raspberry Pi with an internet connection you could put your SD card into that to install the libraries, then transfer it back to the Raspberry Pi Zero.

Once you are connected to the internet, run the following command in the terminal:

```bash
sudo apt-get install python3-blinkt
```

## Attaching the camera

The Raspberry Pi Zero has a smaller camera port than a standard Raspberry Pi, so you will need a special camera cable with one narrower end to attach the camera for your wearable make. You can see the difference between the two cables below:

  ![Camera cables](images/camera-cables.png)

1. On the PiCamera, locate the clip where the camera cable is attached and pull it up to release the cable. The clip works just like the one you usually use to attach the camera to the Raspberry Pi.

  ![Camera without cable](images/camera-no-cable.png)

1. Insert the wider end of the Raspberry Pi Zero camera cable into the camera, with the exposed metal connectors facing towards the front of the camera. Push down the clip to secure the cable in place.

  ![Camera attached to Pi Zero cable](images/camera-attached.png)

1. Pull up the camera clip on the Raspberry Pi Zero and insert the narrower end of the camera cable, with the exposed metal connectors facing the underside of the Pi Zero. Push down the clip to secure the cable.

  ![Pull up the clip](images/pull-up-clip.png)

## Checking your camera

1. Check that your camera is working by opening the terminal and typing the following command:

  ```bash
  raspistill -k
  ```

1. You should see a camera preview. Press the Enter key to take a picture and exit. If you do not see a camera preview and instead receive an error message, check that your camera is properly connected to the Raspberry Pi Zero. Also ensure that your camera is enabled by opening the Raspberry Pi configuration menu under "Preferences":

  ![Raspberry Pi config menu](images/raspi-config-menu.png)

1. Check that the camera is set to "Enabled". If it is not, change the setting to "Enabled", press OK and then reboot your Raspberry Pi Zero before trying again to take a picture with the `raspistill -k` command.

  ![Set camera to enabled](images/raspi-config.png)

## Coding the timelapse

1. Once the camera is set up, we need to write some code to take regular pictures. Firstly open the file explorer and right click on a blank area. Select `Create new` and then click `Folder`

  ![Create folder menu](images/create-folder.png)

1. Type in the name of the folder where you will store the code and the photographs. We chose to call ours `timelapse`. Make a note of the path to this folder which is displayed in the bar at the top. Ours was `/home/pi/timelapse`

  ![Timelapse folder](images/timelapse-folder.png)

1. From the "Programming" menu, open up "Python 3"

  ![Open Python 3](images/python3-app-menu.png)

1. Create a new Python file by clicking on `File` > `New File`.

1. Click on `File` > `Save` and save your file into the `timelapse` folder you just created, with the filename `timelapse.py`.

1. Add the following code to set up your PiCamera. We have deliberately set the resolution of the camera at 1024 x 768 so that the images are captured at a lower resolution. This is in case you wish to make an animated gif of your timelapse photographs later, so the file size of the gif will not be too large. If you would prefer higher or lower resolution photographs, you can change this setting accordingly.

  ```python
  import time
  import picamera

  with picamera.PiCamera() as camera:
      camera.resolution = (1024, 768)
  ```

1. We need the camera to capture an unspecified number of photographs as the program runs continuously. To do this, we will use the `capture_continuous` method from the picamera library. Add three lines to your code so that it looks as follows:

    ```python
    WAIT_TIME = 30

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        for filename in camera.capture_continuous('/home/pi/timelapse/img{timestamp:%H-%M-%S-%f}.jpg'):
            time.sleep(WAIT_TIME)
  ```

  Let's look at what these three lines do:
  - `WAIT_TIME = 30` - sets how long we would like to wait between shots, in seconds
  - `for filename in camera.capture_continuous(` - creates an "infinite iterator" or in other words, the code will keep taking photos forever until the program is stopped
  - `'/home/pi/timelapse/img{timestamp:%H-%M-%S-%f}.jpg'` - the filename of the picture. Notice the interesting part - `{timestamp:%H-%M-%S-%f}` - this makes the file name of the picture contain the current time (including milliseconds), so that the pictures can be organised easily into a sequence, and so that it is extremely unlikely that two pictures would have the same file name.
  - `time.sleep(WAIT_TIME)` - Wait for the number of seconds you specified earlier

1. Press F5 to run your program, and check that it continuously takes pictures every 30 seconds. You should be able to find the pictures in the folder `/home/pi/timelapse`.

## Coding the lights

This part is optional - if you don't have a Blinkt or don't want to put lights on your timelapse camera, you can skip this section.

1. If you have not done so already, attach the Blinkt to your Raspberry Pi Zero, ensuring that it is powered off first. The Blinkt *must* be attached with the curved edges matching the curved edges of the Raspberry Pi Zero to avoid permanently damaging it.

  ![Attach the Blinkt](images/attach-blinkt.png)

1. Once the Blinkt is attached and the Raspberry Pi Zero is switched on, you can add some code to your program to control the lights.

1. Add a new line of code with the other `import` statements to import the functions we need from the blinkt library:

  ```python
  from blinkt import set_pixel, set_brightness, show, clear
  ```

1. Immediately after this line, create a function:

  ```python
  def lights():
    # Code will go here
  ```

1. Inside this function you can put the code for your own light show. Here's a very simple example:

  ```python
  def lights():
    set_brightness(0.1)
    clear()
    set_pixel(0, 255, 0, 0)
    show()
  ```

  This code does the following:
  - `set_brightness(0.1)` - the lights are pretty bright, so we turned them down a bit
  - `clear()` - clears any lights which may be on
  - `set_pixel(0, 255, 0, 0)` - Sets pixel 0 (the pixels are numbered 0-7 starting on the left) to red. The first number is which pixel to set, and the last three numbers are a colour in RGB format.
  - `show()` - Shows the pixels in the colours you just set.

1. Add a line of code to call the function which shows the lights when a new picture is taken:

  ```python
  for filename in camera.capture_continuous('/home/pi/timelapse/img{timestamp:%H-%M-%S-%f}.jpg'):
      lights()    # Add this line to call the light show
      time.sleep(WAIT_TIME)
  ```

1. Add your own code for a light show. When writing the code for your light sequence, make sure that you do *not* include an infinite loop (`while True:`) within the function. If you do this, the flow of control within your program will get stuck within this loop and your camera will not take any more pictures. In the glasses example we used [this code](code/example_lights.py) to cause a red light to move across the screen and back twice.

## Loading the script on boot

Since we will be running the Raspberry Pi Zero as a wearable with a USB power supply (and not with a keyboard, mouse or monitor attached), we need a way of starting the Python script when the Raspberry Pi Zero powers on.

1. Open up a terminal window

1. At the terminal, type the following command:

  ```bash
  sudo nano ~/.config/lxsession/LXDE-pi/autostart
  ```

1. A file will open up, add this line at the bottom of the file to automatically start your timelapse file using Python 3:

  ```bash
  sudo /usr/bin/python3 /home/pi/timelapse/timelapse.py
  ```

1. Press `Ctrl+X` to exit and `y` to save the changes.

1. Now when you reboot your Raspberry Pi, the script should run. You can test this by rebooting and then looking inside the folder `/home/pi/timelapse` to see the photographs appearing. Note that when you reboot, you will not see any window showing that your script is running as Python will be running in the background.

## Creating the wearable

Now that your code works, it's time to work out how you will make your Raspberry Pi Zero wearable! You could make anything ranging from designing a stylish case using a 3D printer to the opposite end of maker chic - a cardboard box and gaffer tape. Here is how we made the glasses, to give you an example:

1. Take a small box that will fit the Raspberry Pi Zero inside - this could be a match box, or we found this old headphone box:

  ![Small box](images/small-box.png)

1. Using a craft knife, carefully cut a hole in the box big enough for the lights to show through, if you are using them.

  ![Cut hole for lights](images/cut-a-hole.png)

1. Also cut holes in the box to access the ports on the Raspberry Pi Zero, and two holes on the back for the arm of the glasses. Insert the arm of the glasses through the hole to attach it to the box, being careful not to bend it too much. We also covered the box with black gaffer tape to make it look cool and futuristic.

  ![Cut hole for glasses](images/glasses-through.png)

1. Put the Raspberry Pi Zero inside the box and close the ends. You can feed the camera cable through the closed flap and secure it onto the front of the box using more gaffer tape.

  ![Camera on front](images/timelapse-specs.png)

1. Attach your USB power pack through the hole you cut in the bottom of the box and turn it on to boot up the pi and start your timelapse wearable.

## What's next?

- You can see the pictures your timelapse wearable took by attaching your monitor, keyboard and mouse to the Raspberry Pi Zero and navigating to the folder `/home/pi/timelapse`
- Perhaps you could create a [gif out of your timelapse pictures](https://www.raspberrypi.org/learning/timelapse-setup/)?
- Instead of lights, could you incorporate a sensor into your project to intead take a photograph only when the sensor is triggered?
