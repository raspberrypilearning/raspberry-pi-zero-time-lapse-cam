from blinkt import set_pixel, set_brightness, show, clear

set_brightness(0.1)
clear()
# Display the light pattern
def lights():

    # Set up for the pi-lon
    speed = 0.1

    # Light cycle (repeat the pattern twice)
    for i in range(2):
        i = 0

        # Set pixels to move along from the left to the right...
        while i <= 7:
            clear()
            set_pixel(i, 255, 0, 0)
            if i < 7:
                set_pixel(i+1, 255, 0, 0)
            if i < 6:
                set_pixel(i+2, 255, 0, 0)
            show()
            time.sleep(speed)
            i+=1
        i = 7

        # Once the end is reached, move the pixel back again
        while i >= 0:
            clear()
            set_pixel(i, 255, 0, 0)
            if i > 0:
                set_pixel(i-1, 255, 0, 0)
            if i > 1:
                set_pixel(i-2, 255, 0, 0)
            show()
            time.sleep(speed)
            i-=1
    clear()
    show()


# Call the function
lights()
