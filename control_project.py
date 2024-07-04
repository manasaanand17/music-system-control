import pygame
import pyttsx3
import os

pygame.init()
engine = pyttsx3.init()

music_directory = "C:\\Users\\manas\\OneDrive\\Desktop\\iotproject\\SONGS"

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

pygame.mixer.init()

def select_music(file_index):
    file_path = os.path.join(music_directory, music_files[file_index])
    return os.path.splitext(os.path.basename(file_path))[0]

def play_music(file_index):
    file_path = os.path.join(music_directory, music_files[file_index])
    pygame.mixer.music.load(file_path)
    print('Playing "{}"'.format(os.path.splitext(os.path.basename(file_path))[0]))
    engine.say('Playing {}'.format(os.path.splitext(os.path.basename(file_path))[0]))
    engine.runAndWait()
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def replay_music():
    pygame.mixer.music.rewind()
    pygame.mixer.music.play()

def play_next_song(current_index):
    next_index = (current_index + 1) % len(music_files)
    play_music(next_index)
    return next_index

def play_previous_song(current_index):
    previous_index = (current_index - 1) % len(music_files)
    play_music(previous_index)
    return previous_index

def volume_up():
    new_volume = min(1.0, pygame.mixer.music.get_volume() + 0.02)  # Increase volume by 2%
    pygame.mixer.music.set_volume(new_volume)
    print("Volume increased to:", int(new_volume * 100), "%")

def volume_down():
    new_volume = min(1.0, pygame.mixer.music.get_volume() - 0.02)  # decrease volume by 2%
    pygame.mixer.music.set_volume(new_volume)
    print("Volume increased to:", int(new_volume * 100), "%")

def main():
    first_input = True
    current_song_index = 0

    # play_music(current_song_index)

    while True:
        user_input = input("Enter command (play/pause/replay/next/prev/select/quit/volume up/volume down): ").lower()

        if user_input == "play":
            if first_input:
                first_input = False
                play_music(current_song_index)
            else:
                unpause_music()
        elif user_input == "pause":
            pause_music()
        elif user_input == "replay":
            replay_music()
        elif user_input == "next":
            current_song_index = play_next_song(current_song_index)
        elif user_input == "prev":
            current_song_index = play_previous_song(current_song_index)
        elif user_input == "volume up":
            volume_up()
        elif user_input == "volume down":
            volume_down()
        elif user_input == "select":
            selected_index = int(input("Enter the song No: (1 to {}): ".format(len(music_files)))) - 1
            if 0 < selected_index < len(music_files):
                name = select_music(selected_index)
                pause_music()
                print('Do you want to play "{}"? Enter PLAY to confirm. Else, enter BACK'.format(name))
                engine.say('Do you want to play {}?'.format(name))
                engine.runAndWait()
                option = input().lower()
                if option == "play":
                    play_music(selected_index)
                else:
                    unpause_music()
            else:
                print("Invalid index. Please select a valid index.")
        elif user_input == "quit":
            pygame.mixer.music.stop()
            pygame.quit()
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()