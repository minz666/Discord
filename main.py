import requests
import random
import time
import os
from colorama import Fore, init

# Inisialisasi colorama
init(autoreset=True)

print("MMMMMMMM               MMMMMMMM  iiii                   ZZZZZZZZZZZZZZZZZZZ")
print("M:::::::M             M:::::::M i::::i                  Z:::::::::::::::::Z")
print("M::::::::M           M::::::::M  iiii                   Z:::::::::::::::::Z")
print("M:::::::::M         M:::::::::M                         Z:::ZZZZZZZZ:::::Z ")
print("M::::::::::M       M::::::::::Miiiiiiinnnn  nnnnnnnn    ZZZZZ     Z:::::Z  ")
print("M:::::::::::M     M:::::::::::Mi:::::in:::nn::::::::nn          Z:::::Z    ")
print("M:::::::M::::M   M::::M:::::::M i::::in::::::::::::::nn        Z:::::Z     ")
print("M::::::M M::::M M::::M M::::::M i::::inn:::::::::::::::n      Z:::::Z      ")
print("M::::::M  M::::M::::M  M::::::M i::::i  n:::::nnnn:::::n     Z:::::Z       ")
print("M::::::M   M:::::::M   M::::::M i::::i  n::::n    n::::n    Z:::::Z        ")
print("M::::::M    M:::::M    M::::::M i::::i  n::::n    n::::n   Z:::::Z         ")
print("M::::::M     MMMMM     M::::::M i::::i  n::::n    n::::nZZZ:::::Z     ZZZZZ")
print("M::::::M               M::::::Mi::::::i n::::n    n::::nZ::::::ZZZZZZZZ:::Z")
print("M::::::M               M::::::Mi::::::i n::::n    n::::nZ:::::::::::::::::Z")
print("M::::::M               M::::::Mi::::::i n::::n    n::::nZ:::::::::::::::::Z")
print("MMMMMMMM               MMMMMMMMiiiiiiii nnnnnn    nnnnnnZZZZZZZZZZZZZZZZZZZ\n")
print("===========================================================================\n")
Script = "       Discord Bot Type Messages (NO DELETE VERSION)\n"
print("Script       : " + Script)
Github = "       https://github.com/minz666/Discord\n"
print("Github       : " + Github)
print("===========================================================================\n")
print('WARNING   :        DONT SELL THIS CODE! \n')
print("WARNING   :        ALL RISKS ARE DRNE BY THE USER!\n")
print("===========================================================================\n")

time.sleep(1)

channel_id = input("Enter Channel ID (Not Server)        :   ")
time2 = int(input("Set the time to send the messages (seconds) :   "))
target_messages = int(input("Set target total messages to send           :   "))

time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

# Baca daftar pesan dari message.txt
with open("message.txt", "r", encoding="utf-8") as f:
    words = [w.strip() for w in f.readlines() if w.strip()]

if not words:
    print(Fore.RED + "File message.txt kosong atau tidak ada pesan yang valid.")
    exit()

# Baca token dari token.txt
with open("token.txt", "r", encoding="utf-8") as f:
    authorization = f.readline().strip()

if not authorization:
    print(Fore.RED + "Token di token.txt kosong. Isi dengan BOT TOKEN kamu.")
    exit()

channel_id = channel_id.strip()

# === COUNTER PESAN ===
message_count = 0

while True:

    # Stop bila sudah mencapai target
    if message_count >= target_messages:
        print(Fore.GREEN + f"\nTarget {target_messages} pesan telah tercapai!")
        print(Fore.GREEN + "Program selesai.\n")
        break

    # Pilih pesan random dari file
    payload = {
        'content': random.choice(words)
    }

    headers = {
        'Authorization': authorization
    }

    # Kirim pesan ke channel
    r = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        data=payload,
        headers=headers
    )

    if r.status_code in (200, 201):
        message_count += 1
        print(Fore.WHITE + f"\nSent message: {message_count}/{target_messages}")
        print(Fore.YELLOW + payload['content'])
    else:
        print(Fore.RED + f"Failed to send message: {r.status_code}")
        try:
            print(Fore.RED + r.text)
        except:
            pass

    # === COOLDOWN TETAP DI SATU BARIS ===
    for remaining in range(time2, 0, -1):

        # Hapus baris sebelumnya
        print(" " * 60, end="\r")

        # Tampilkan countdown
        print(
            Fore.CYAN + 
            f"Next message in {remaining} seconds... ({message_count}/{target_messages})",
            end="\r"
        )

        time.sleep(1)

    # Bersihkan baris countdown sebelum lanjut
    print(" " * 60, end="\r")
