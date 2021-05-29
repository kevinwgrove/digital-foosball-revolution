# Digital Foosball Revolution

![Foosball Table](https://images.thdstatic.com/productImages/3881eef3-44c1-4e8b-afbb-6c3e7b35366e/svn/sunnydaze-decor-foosball-tables-eg-701-64_600.jpg)

#### **Welcome to the Digital Foosball Age!**

This is an open source program that allows you to retro fit your foosball table with a digital scoring system. This is a major DIY project that requires a large amount of preparation, tools, hardware and materials. I will be posting hardware, equipment, tutorials, walkthroughs and videos on the host [site](https://www.digitalfoosballrevolution.com) once I get it up and running. But for now, I'll provide a simple list of items needed to get set up. You can also check out my [YouTube](https://www.youtube.com/channel/UC9bkXmpMcpCEUwjpWFhHVtw) channel to see if I've uploaded any new videos.

## **Overview**
This is a pretty intense DIY project (not for the faint of heart). If you are passionate about sensors, microcontrollers, or foosball itself, this project is for you. If I were to rate this on a difficulty scale from 1-5, I'd probably give it a 3 or 4. But I'm not one to judge, this is my first major project in a while, and it is totally achievable. 

There are 2 game modes that are included in this system:
1. **Classic**
    * Editable Parameters:
        1. Home Team Score
            - Default: 0
        2. Away Team Score:
            - Default: 0
        3. Best of: (This a best of series: i.e. first player to win 2 games in a best of 3 series wins)
            - Default: 1
                * Note: Switch sides after every game
        4. First to: (This sets the score to reach in order to win)
            - Default: 10 

2. **Timed Halves**
    * Editable Parameters:
        1. Player 1 Score:
            - Default: 0
        2. Player 2 Score:
            - Default: 0
        3. Half times: (Sets the length of halves in 15 second increments/decrements)
            - Default: 5:00
        4. Legs: (Like best of, this is a 2 game series. Each player has a turn being Home/Away team. If it ends in a tie of accumulative goals at the end of the second game, it enters a "Golden Goal" rule; which means the next person to score wins.)
            - Default: Off
        5. Player 1 Ratio: (Sets how many goals player 1 must score in order to earn a goal, i.e. 3:1; player on must score 3 goals to register a goal)
            - Default: 1
        6. Player 2 Ratio:
            - Default: 1

### **Buttons**
![Control/Housing Unit](https://github.com/kevinwgrove/digital-foosball-revolution/blob/main/photos_videos/IMG_2234.jpg)

![Buttons](https://github.com/kevinwgrove/digital-foosball-revolution/blob/main/photos_videos/IMG_2232.jpg)
1. **Increase/Next** (Black)
    * Used to increase amounts in the "Edit Mode" screen. It is also used to cycle through the "Game Mode" screen when the system powers on.
2. **Decrease/Previous** (Black)
    * Used to decrease amounts in the "Edit Mode" screen. It is also used to cycle through the "Game Mode" screen when the system powers on.
3. **Enter/Select** (Green)
    * Used to select the game mode. Also used to get out of "Edit Mode"
4. **Edit Mode** (Yellow)
    * Used to enter "Edit Mode" once game mode is selected. This allows the user to customize all parameters of "Edit Mode". 
        * **Use this button to cycle through "Edit Mode" parameters**
5. **Reset/Back** (Red)
    * Used to reset a game if a game is currently being played, or is used to exit the game mode and return to the previous screen.
6. **Home/Away LED Button**
    * **Classic Mode**:
        * Before the start of each game, both players must press the lit LED button in order to start game play. These buttons will be lit, indicating that they need to be pressed.
    * **Timed Halves Mode**:
        * Before the start of each game, both players must press the lit LED button in order to start game play. These buttons will be blinking, indicating that they need to be pressed.
        * Pressing the LED button during game play pauses the timer and pauses game play. Both players must press they're respective LED button to start game play again. (the LEDs will turn off once the system registers that the button has been pressed)
        * The LED button is also used as a backup way to start game play and the clock after each goal. If the sensor in the ball return does not register that the ball has reached the ball return, the LED button can be pressed to override this feature.

### **Sensors**
1. **Ball Return Sensors**
    * Each side has a ball return that are equipped with a pressure sensitive resistor. After a goal the ball enters the ball return, and if the sensor has registered that the ball is in the ball return, the clock and game play will start again automatically. If this doesn't happen, the Home/Away LED Button will be lit and can be used as a backup game play restarter.
2. **Goal Sensors**
    * Each goal has a total of 5 sensors that line the inside of the goal. Once a ball enters the goal, the sensors SHOULD register that a goal has been scored. If it doesn't register, you have to go into "Edit Mode" and manually change the score.

## **Code Options**

I set this up in a way that you can load the code directly on to the microcontroller and run it from its processor, or you can load the code onto a microSD card and run it from the SD card slot on an [Adafruit Grand Central M4 Express](https://www.adafruit.com/product/4064). The option is yours!

However, you will need to use the correct folder(s) depending on which route you take.

**Before you get started** visit the [Grand Central CircuitPython Download Page](https://circuitpython.org/board/grandcentral_m4_express/) and load the downloaded file onto your microcontroller. **This is SUPER important!**

### *Direct to microcontroller: Directions*
The folder you will use from this repo is the 'direct' folder. All you need to do is load its contents directly to your microcontroller.

### *SD Card: Directions*
You will have to load the contents of the 'w_sdmount' folder to your microcontroller, then load the contents of 'sd_files' onto a microSD card. Anything over 2G should be enough (I doubt you'd need that much). I use a 256G card, only because I plan on setting up a logger in the future to keep track of bugs.

#### **Pinouts**
Pinouts are listed in the 'code.py' files in each version of code.

### **Hardware List**
*   (1) [Adafruit Grand Central M4 Express](https://www.adafruit.com/product/4064), or an equivalent microcontroller that has 24+ pinouts (if you don't want the "special" button or audio; in which case 26+).
    *   Disclaimer: My childish friend who is allowing me to retro fit his foosball table said the only way I could do this is if I had audio and a fart button, so... the option is yours. You can just leave those pinouts disconnected, you don't have to delete any code to make it functional.

*   (1) Any size breadboard, but I used a [half-size breadboard](https://www.adafruit.com/product/64)

*   (1) [64x32 RGB LED Matrix - 5mm pitch](https://www.adafruit.com/product/2277). LED Matrix
    *   (1) You'll also need an [Adafruit RGB Matrix Shield for Arduino](https://www.adafruit.com/product/2601), a [5V 2A (2000mA) switching power supply - UL Listed](https://www.adafruit.com/product/276), and a [Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368) for your LED Matrix

*   (4-6) [FSR Model 408 (200mm length)](https://buyinterlinkelectronics.com/collections/new-standard-force-sensors/products/fsr-model-408-200mm-length) or [FSR Model 408 (100mm length)](https://buyinterlinkelectronics.com/collections/new-standard-force-sensors/products/copy-of-fsr-model-408-100mm-length). You will have to measure the width of your goal to determine which length sensor you'll need. 2-3 sensors will line the back of each goal.
    *   Note: These sensors can be cut to size. However, they should not be cut less than 5mm from the connector. 

*   (4-6) [FSR Model 406](https://buyinterlinkelectronics.com/collections/new-standard-force-sensors/products/fsr-model-406). I say 4-6, because it really depends on how your goal is designed. I put 2 of these sensors on the bottom inner lining of each goal as a fail safe, in case the above sensors don't register a goal. The 3rd I put inside the ball slot (where the ball goes after a goal). When a goal is detected, the ball slot sensor tells the program it is kickoff time again. An LED button is also there as backup.
    *   If the ball is in the ball slot and the LED button is lit, then the ball slot sensor wasn't triggered to tell the program it is ready for kickoff again. In which case you will need to either hit the ball slot sensor, or press the button.

*   (2) [Arcade Button with LED - 30mm Translucent Red](https://www.adafruit.com/product/3489). This is used as a ready button for both Home(Player 1) and Away(Player 2) Teams. Before initiating the game (kickoff), both buttons will flash until pressed. Once both are pressed, then you can start playing. This button also acts as a backup kickoff indicator after each goal. **See above**

*   (2) [16mm Panel Mount Momentary Pushbutton - Black](https://www.adafruit.com/product/1505). These are the increment(next)/decrement(back) buttons. Used for cycling through menus and editing score/time/best_of/high_score/goal_ratio/etc.

*   (1) [16mm Panel Mount Momentary Pushbutton - Green](https://www.adafruit.com/product/1504). Enter(select) button.

*   (1) [16mm Panel Mount Momentary Pushbutton - Yellow](https://www.adafruit.com/product/1502). Edit button.

*   (1) [16mm Panel Mount Momentary Pushbutton - Red](https://www.adafruit.com/product/1445). Reset(back) button.

*   (1) [19mm Brown Waterproof Momentary Type Stainless Steel Metal Push Button Switch High Flush](https://www.amazon.com/gp/product/B013ZDOI5G/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1). Fart button (not necessary)

### **Audio Parts**
*   (1) [Gikfun Upgraded USB Mini Amplifier Electronic Transparent Stereo Speaker Box Sound Amplifier DIY Kit for Arduino](https://www.amazon.com/gp/product/B07GP9MLS8/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1). Speakers

*   (1) [Stereo 3.7W Class D Audio Amplifier - MAX98306](https://www.adafruit.com/product/987)

*   (1) [Panel Mount Right Angle 10K Linear Potentiometer w/On-Off Switch - 10K Linear w/ Switch](https://www.adafruit.com/product/3395). You can get any potentiometer you'd like. I just like this one because it mounts flat on the breadboard and it's more manageable when soldering the wires and making the connections.

## **References**
[Adafruit Grand Central M4 Express](https://learn.adafruit.com/adafruit-grand-central/overview)

[Pressure Sensitive Resistors](https://buyinterlinkelectronics.com/collections/new-standard-force-sensors)

[CircuitPython Tutorial](https://learn.adafruit.com/welcome-to-circuitpython)

[CircuitPython Essentials for the M4 Express](https://learn.adafruit.com/adafruit-grand-central/circuitpython-essentials)

[CircuitPython Downloads for your board](https://circuitpython.org/downloads)

[LED Matrix Setup](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix/connecting-using-rgb-matrix-shield)

[SD Card tutorial](https://learn.adafruit.com/micropython-hardware-sd-cards/code-storage-on-sd-card)

**Special thanks to Piero Madar(Tech Guru) for being there to lean on when I was stuck or needed a little extra guidance and resources when I couldn't get something to work.**


I will be updating this README as I go along with any new information. Please feel free to reach out to me with any questions, concerns, suggestions, etc. Thanks and enjoy!

Kevin
