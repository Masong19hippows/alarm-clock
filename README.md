# alarm-clock
Alarm clock that plays simon says when it triggers


This was a project for a friend. We used two oled display to display time. We also had buttons to change settings and to play simon says. The time is save din an rtc and we used a buzzer for an alarm like sound. This was made in a way that could easily be expandable. In the future, I plan to add more buttons, more ringtones for the alarm, and more displays for a more customizable look.

## Install

The install was made for a raspberry pi pico. You just need to upload the entire respoitory to a pico, and then it should run on boot.

## Buttons

Here is a list of what the buttons did in order. To activate these buttons, the first button needs to be held untill the first part like shown in the picture below. After that, you just need to tap the button that correlates with what setting you want to change.

### Button 1

This button is an all purpose button. You must hold this button in order to change any settings. If you hold this button, the first digit of the clock should always invert untill you let go or another button is pressed.

### Button 2

The first button will let you change between 24 hour format and 12 hour format for the clock. Once this settings is selected, you can switch between the modes with the same button. When you are at a setting that you would like, just hold down button #1 untill the first digit inverts, then just tap the second button for the last time. 

### Button 3

This button is used to change when the alarm goes off. Due to there being no am or pm selection yet; you must input this time in 24 hour format. Once you have the desired time, just hold the first button down untill the first digit inverts, then tap the third button one last time.

### Button 4

This button changes the time and saves it to the rtc. Due to there being no am or pm selection yet; you must input this time in 24 hour format. Once you have the desired time, just hold the first button down untill the first digit inverts, then tap the fourth button one last time. 

# Thats All. Have Fun!!!
