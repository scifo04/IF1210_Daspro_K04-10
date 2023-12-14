# File: main.py
import data
import argparse
import os.path
import commands

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", type=str, nargs='?', default='')
args = parser.parse_args()
folder = args.nama_folder
if folder == '':                        # jika tidak ada masukan nama folder
    print("Tidak ada nama folder yang diberikan!\n")
    print("Usage: python main.py <nama_folder>")
    goplay = False
    quit()
elif os.path.exists(folder) == True:    # jika foldernya ada
    print("Loading...")
    commands.load(folder)
    print("Selamat datang di program “Manajerial Candi”")
    print("Silahkan masukkan username Anda")
elif os.path.exists("./save/"+folder+"/") == True:
    print("Loading...")
    commands.load("./save/"+folder+"/")
    print("Selamat datang di program “Manajerial Candi”")
    print("Silahkan masukkan username Anda")
else:                                   # jika foldernya tidak ada
    print(f"Folder “{folder}” tidak ditemukan.")
    quit()

while True:
    masukan = input(">>> ")
    commands.run(masukan)
    if data.endthis == True:
        break