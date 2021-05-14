# Digital Foosball Revolution

#### **Welcome to the Digital Foosball Age!**

This is an open source program that allows you to retro fit your foosball table with a digital scoring system. This is a major DIY project that requires a large amount of preparation, tools, hardware and materials. I will be posting hardware, equipment, tutorials, walkthroughs and videos on the host [site](https://www.digitalfoosballrevolution.com) once I get it up and running. But for now, I'll provide a simple list of items needed to get up and running. You can also check out my [YouTube](https://www.youtube.com/channel/UC9bkXmpMcpCEUwjpWFhHVtw) channel to see if I've uploaded any new videos.

## **Code Options**

I set this up in a way that you can load the code directly on to the microcontroller and run it from its processor, or you can load the code onto a microSD card and run it from the SD card slot on an [Adafruit Grand Central M4 Express](https://www.adafruit.com/product/4064). The option is yours!

However, you will need to use the correct folder(s) depending on which route you take.

### *Direct to microcontroller: Directions*
The folder you will use from this repo is the 'direct' folder. All you need to do is load its contents directly to your microcontroller.

### *SD Card: Directions*
You will have to load the contents of the 'w_sdmount' folder to your microcontroller, then load the contents of 'sd_files' onto a microSD card. Anything over 2G should be enough (I doubt you'd need that much). I use a 256G card, only because I plan on setting up a logger in the future to keep track of bugs.

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


I will be updating this README as I go along with any new information. Please feel free to reach out to me with any questions, concerns, suggestions, etc. Thanks and enjoy!

Kevin
