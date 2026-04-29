import os
import time
import helpers as h

from dotenv import load_dotenv
load_dotenv()

ssk_dload_path   = os.getenv("SSK_DLOAD_PATH")      # complete/"user"/"album"/"file"
destination_path = os.getenv("DESTINATION_PATH")    # transfer/"album"/["mp3" || "wav"]/"file"

mp3_counter = wav_counter = flac_counter = aiff_counter = m4a_counter = 0

start_time = time.perf_counter()
for dirpath, _, filenames in os.walk(ssk_dload_path): 
    for filename in filenames:

        curr_file_path            = os.path.join(dirpath, filename)
        destination_folder_path   = os.path.join(destination_path, os.path.basename(dirpath)) # curr folder @ destination:
        file_name, file_extension = os.path.splitext(filename) # filename has extention, file_name does not;
        file_extension = file_extension.lower()

        if file_extension   == ".mp3": 
            mp3_counter = h.mp3_manager(curr_file_path, destination_folder_path, filename, mp3_counter)

        elif file_extension == ".wav": 
            wav_counter = h.wav_manager(curr_file_path, destination_folder_path, file_name, wav_counter)

        elif file_extension == ".flac":
            flac_counter = h.flac_manager(curr_file_path, destination_folder_path, file_name, flac_counter)

        elif file_extension == ".aiff":
            aiff_counter = h.aiff_manager(curr_file_path, destination_folder_path, file_name, aiff_counter)
        
        elif file_extension == ".m4a":
            m4a_counter = h.m4a_manager(curr_file_path, destination_folder_path, file_name, m4a_counter)
        
        else:
            if file_extension not in ("", ".ini"):
                print(f"{curr_file_path}")

print(f"\nmp3:  {mp3_counter}\nm4a:  {m4a_counter}\nwav:  {wav_counter}\nflac: {flac_counter}\naiff: {aiff_counter}")

for dirpath, dirnames, _ in os.walk(ssk_dload_path, topdown=False):
    for dirname in dirnames:
        
        folder_path = os.path.join(dirpath, dirname)
        os.rmdir(folder_path)

end_time = time.perf_counter()
print(f"\ntime: {end_time - start_time}\n")

