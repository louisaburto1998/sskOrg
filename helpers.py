import os
import shutil
from mutagen.mp3 import MP3
from pydub import AudioSegment

def mp3_manager(curr_file_path, destination_folder_path, filename, mp3_counter):

    try:
        song = MP3(curr_file_path)
    except Exception as e:
        print(f"{e}")
        return
    song_bitrate = song.info.bitrate // 1000 # remove 3 digits: 

    mp3_folder_path = os.path.join(destination_folder_path, "mp3") # destination/album/mp3:
    os.makedirs(mp3_folder_path, exist_ok=True)
    shutil.move(curr_file_path, mp3_folder_path)

    curr_song_path = os.path.join(mp3_folder_path, filename) # path @ destination:
    new_song_path  = os.path.join(mp3_folder_path, f"{song_bitrate}_{filename}") # path for rename:
    os.rename(curr_song_path, new_song_path)

    mp3_counter += 1
    return mp3_counter
    

def wav_manager(curr_file_path, destination_folder_path, file_name, wav_counter):

    try:
        song = AudioSegment.from_wav(curr_file_path)
    except Exception as e:
        print(f"{e}")
        return

    mp3_destination_folder = os.path.join(destination_folder_path, "mp3")
    os.makedirs(mp3_destination_folder, exist_ok=True)
    mp3_song_path = os.path.join(mp3_destination_folder, f"320_{file_name}.mp3")
    song.export(mp3_song_path, format="mp3", bitrate="320k")
    
    wav_destination_folder = os.path.join(destination_folder_path, "wav")
    os.makedirs(wav_destination_folder, exist_ok=True)
    shutil.move(curr_file_path, wav_destination_folder)
  
    wav_counter += 1
    return wav_counter
    
    
def flac_manager(curr_file_path, destination_folder_path, file_name, flac_counter):

    try:
        song = AudioSegment.from_file(curr_file_path, format="flac")
    except Exception as e:
        print(f"{e}")
        return

    mp3_destination_folder = os.path.join(destination_folder_path, "mp3")
    os.makedirs(mp3_destination_folder, exist_ok=True)
    mp3_song_path = os.path.join(mp3_destination_folder, f"320_{file_name}.mp3")
    song.export(mp3_song_path, format="mp3", bitrate="320k")
        
    wav_destination_folder = os.path.join(destination_folder_path, "wav")
    os.makedirs(wav_destination_folder, exist_ok=True)
    wav_song_path = os.path.join(wav_destination_folder, f"{file_name}.wav")
    song.export(wav_song_path, format="wav")
        
    os.remove(curr_file_path)

    flac_counter += 1
    return flac_counter
    

def aiff_manager(curr_file_path, destination_folder_path, file_name, aiff_counter):

    try:
        song = AudioSegment.from_file(curr_file_path, format="aiff")
    except Exception as e:
        print(f"{e}")
        return

    mp3_destination_folder = os.path.join(destination_folder_path, "mp3")
    os.makedirs(mp3_destination_folder, exist_ok=True)
    mp3_song_path = os.path.join(mp3_destination_folder, f"320_{file_name}.mp3")
    song.export(mp3_song_path, format="mp3", bitrate="320k")

    wav_destination_folder = os.path.join(destination_folder_path, "wav")
    os.makedirs(wav_destination_folder, exist_ok=True)
    wav_song_path = os.path.join(wav_destination_folder, f"{file_name}.wav")
    song.export(wav_song_path, format="wav")

    os.remove(curr_file_path)

    aiff_counter += 1
    return aiff_counter


def m4a_manager(curr_file_path, destination_folder_path, file_name, m4a_counter):
    
    try:
        song = AudioSegment.from_file(curr_file_path, format="m4a")
    except Exception as e:
        print(f"{e}")
        return
    
    mp3_destination_folder = os.path.join(destination_folder_path, "mp3")
    os.makedirs(mp3_destination_folder, exist_ok=True)
    mp3_song_path = os.path.join(mp3_destination_folder, f"320_{file_name}.mp3")
    song.export(mp3_song_path, format="mp3", bitrate="320k")

    wav_destination_folder = os.path.join(destination_folder_path, "wav")
    os.makedirs(wav_destination_folder, exist_ok=True)
    wav_song_path = os.path.join(wav_destination_folder, f"{file_name}.wav")
    song.export(wav_song_path, format="wav")

    os.remove(curr_file_path)

    m4a_counter += 1
    return m4a_counter
