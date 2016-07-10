import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import time

#soundtrack = simplegui.load_sound(
#        "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
# explosion_sound = simplegui.load_sound(
#         "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
missile_sound = simplegui.load_sound(
         "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
# ship_thrust_sound = simplegui.load_sound(
#         "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")

missile_sound.set_volume(1)
missile_sound.play()
time.sleep(10)