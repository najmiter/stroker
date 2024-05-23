from pynput import keyboard
import pygame
import os

pygame.mixer.init()

sound_effect = 'stroke2.mp3'
is_recording = True

# Function to play sound effect
def play_sound_effect():
    pygame.mixer.music.load(sound_effect)
    pygame.mixer.music.play()

def on_press(key):
    global is_recording

    if not is_recording:
        return

    play_sound_effect()

    if key == keyboard.Key.esc:
        print('Stopping recording...')
        is_recording = False
        return False

with keyboard.Listener(on_press=on_press) as listener:
    print('Press any key to record keystroke sounds. Press ESC to stop.')
    listener.join()
