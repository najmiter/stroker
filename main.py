from pydub import AudioSegment
from pynput import keyboard
import datetime
import pygame
import time

sound_effect = 'stroke2.mp3'
times = []
audio_segments = []

def play_sound_effect():
    pygame.mixer.init()
    pygame.mixer.music.load(sound_effect)
    pygame.mixer.music.play()

def on_press(key):
    global times, audio_segments

    timestamp = datetime.datetime.now()
    times.append(timestamp)

    play_sound_effect()

    if key == keyboard.Key.esc:
        print('Stopping recording...')
        return False



def main():
    with keyboard.Listener(on_press=on_press) as listener:
        print('Press any key to record keystroke sounds. Press ESC to stop.')
        listener.join()

    # it don't work though 🥲
    for _ in range(len(times)):
        audio_segments.append(AudioSegment.from_mp3(sound_effect))

    combined_audio = sum(audio_segments)
    combined_audio.export("combined_audio.mp3", format="mp3")

if __name__ == "__main__":
    main()
