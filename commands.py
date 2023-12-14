import random
import data

def user_read(file):        # + parameter nama file
    user = open(file,'r')   # 
    reader = user.read()
    user_array = [[('') for j in range (3)] for i in range (103)]
    col = 0
    row = 0
    for i in reader:
        if i != ";" and i != "\n":
            user_array[row][col] = user_array[row][col] + i
        elif i == ";":
            col = col+1
        elif i == "\n":
            col = 0
            row = row+1
    data.user_array_globale = user_array
    user.close()            #
    return user_array

def candi_read(file):       # + parameter nama file
    candi = open(file,'r')  # 
    reader = candi.read()
    candi_array = [[('') for j in range (5)] for i in range (101)]
    col = 0
    row = 0
    for i in reader:
        if (i != ";" and i != "\n"):
            candi_array[row][col] = candi_array[row][col] + i
        elif i == ";":
            col = col+1
        elif i == "\n":
            col = 0
            row = row+1
    data.candi_array_globale = candi_array
    candi.close()           #
    return candi_array

def bahanbangunan_read(file):       # + parameter nama file
    bahanbangunan = open(file,'r')  #
    reader = bahanbangunan.read()
    bahanbangunan_array = [[('') for j in range (3)] for i in range (4)]
    col = 0
    row = 0
    for i in reader:
        if i != ";" and i != "\n":
            bahanbangunan_array[row][col] = bahanbangunan_array[row][col] + i
        elif i == ";":
            col = col+1
        elif i == "\n":
            col = 0
            row = row+1
    data.bahanbangunan_array_globale = bahanbangunan_array
    bahanbangunan.close()       #
    return bahanbangunan_array

def candi_row(arr):
    i = 0
    while arr[i][1] != '':
        i += 1
        if i == 101:
            break
    return i

def user_row(arr):
    i = 0
    while arr[i][1] != '':
        i += 1
        if i == 102:
            break
    return i

def isJinPembangun():
    isJinPembangun = False
    for j in range(103):
        if data.username == data.user_array_globale[j][0]:
            if data.user_array_globale[j][2] == "jin_pembangun":
                isJinPembangun = True
    return isJinPembangun

def isJinPengumpul():
    isJinPengumpul = False
    for j in range(103):
        if data.username == data.user_array_globale[j][0]:
            if data.user_array_globale[j][2] == "jin_pengumpul":
                isJinPengumpul = True
    return isJinPengumpul

# ALGORITMA F1
def login():
    if data.logged == True:
        loginno()
    else:
        loginyes()

def loginno():
    print("Login gagal!")
    print("Anda telah login dengan username",data.username,"silahkan lakukan “logout” sebelum melakukan login kembali.")

def loginyes():
    username_local = input("username: ")
    password = input("password: ")
    if data.firstread == True:
        data.bahanbangunan_array_globale[1][0] = "pasir"
        data.bahanbangunan_array_globale[2][0] = "batu"
        data.bahanbangunan_array_globale[3][0] = "air"
        data.bahanbangunan_array_globale[1][1] = "perekat batu"
        data.bahanbangunan_array_globale[2][1] = "struktur bangunan"
        data.bahanbangunan_array_globale[3][1] = "pengeras struktur"
        data.bahanbangunan_array_globale[1][2] = 0
        data.bahanbangunan_array_globale[2][2] = 0
        data.bahanbangunan_array_globale[3][2] = 0
        data.firstread = False
    usernamefound = False
    passwordfound = False
    for i in range (1,103):
        if data.user_array_globale[i][0] == username_local and data.user_array_globale[i][0] != '':
            usernamefound = True
        if data.user_array_globale[i][1] == password and data.user_array_globale[i][1] != '':
            passwordfound = True
    if usernamefound == True and passwordfound == True:
        print("Selamat datang",username_local)
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        data.username = username_local
        data.logged = True
    elif usernamefound == False:
        print("Username tidak terdaftar!")
        loginyes()
    elif passwordfound == False:
        print("Password salah!")
        loginyes()

# ALGORITMA F2
def logout():
    if data.logged == False:
        print("Logout gagal")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        data.logged = False
        data.username = ''

# ALGORITMA F3
def summonjin():
    if data.username == "Bandung":
        if user_row(data.user_array_globale) < 102:
            similare = False
            print("Jenis jin yang dapat dipanggil: ")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi")
            print()
            while True:
                jintype = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
                if jintype == "1" or jintype == "2":
                    break
                else:
                    print('Tidak ada jenis jin bernomor'+' "'+jintype+'" '+"!")
            print()
            print("Memilih jin"+((' "Pengumpul".') if jintype == "1" else (' "Pembangun".')))
            print()
            jinrole = (("jin_pengumpul") if jintype == "1" else ("jin_pembangun"))
            while True:
                similare = False
                jinname = input("Masukkan username jin: ")
                for j in range(103):
                    if data.user_array_globale[j][0] == jinname:
                        similare = True
                if similare == True:
                    print("Username",jinname,"sudah diambil!")
                else:
                    break
            jinpass = ''
            while not 5<=len(jinpass)<=25:
                jinpass = input("Masukkan password jin: ")
                if not 5<=len(jinpass)<=25:
                    print("Password panjangnya harus 5-25 karakter")
                else:
                    break
            print()
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print()
            print("Jin",jinname,"berhasil dipanggil")
            for j in range(103):
                if data.user_array_globale[j][0] == '':
                    data.user_array_globale[j][0] = jinname
                    data.user_array_globale[j][1] = jinpass
                    data.user_array_globale[j][2] = jinrole
                    break
            
        else:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Kamu bukan Bandung")

# ALGORITMA F4
def hapusjin():
    if data.username == "Bandung":
        deleteuser = input("Masukkan username jin: ")
        foundname = False
        nomessage = False
        for j in range(103):
            if data.user_array_globale[j][0] == deleteuser and not data.user_array_globale[j][0] == "Bandung" and not data.user_array_globale[j][0] == "RoroJonggrang":
                yesorno = input("Apakah anda yakin ingin menghapus jin dengan username "+deleteuser+" (Y/N)? ")
                foundname = True
                if yesorno == "Y" or yesorno == "y":
                    data.user_array_globale[j][0] = ''
                    data.user_array_globale[j][1] = ''
                    data.user_array_globale[j][2] = ''
                    for k in range(101):
                        if data.candi_array_globale[k][1] == deleteuser:
                            for l in range(5):
                                data.candi_array_globale[k][l] = ''
                elif yesorno == "N" or yesorno == "n":
                    nomessage = True
        if foundname == False:
            print("Tidak ada jin dengan username tersebut.")
            hapusjin()
        else:
            if nomessage == False:
                print("Jin telah berhasil dihapus dari alam gaib")               

# ALGORITMA F5
def UsernameValid(arr):
    isValid = False
    for i in range (103):
        if arr == data.user_array_globale[i][0]:
            isValid = True
    return isValid

def getrole(arr):
    role = ''
    for i in range (103):
        if arr == data.user_array_globale[i][0]:
            role = data.user_array_globale[i][2]
    return role

def ubahjin():
    if data.username == "Bandung":
        jin = input("Masukkan username jin: ")
        newname = ''
        if UsernameValid(jin):
            if getrole(jin) == "jin_pembangun":
                newname = "jin_pengumpul"
                changerole = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke "Pengumpul" (Y/N)? ')
                if changerole == 'Y':
                    for i in range(103):
                        if data.user_array_globale[i][0] == jin:
                            data.user_array_globale[i][2] = newname
                    print("Role sudah diganti")
            elif getrole(jin) == "jin_pengumpul":
                newname = "jin_pembangun"
                changerole = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke "Pembangun" (Y/N)? ')
                if changerole == 'Y':
                    for i in range(103):
                        if data.user_array_globale[i][0] == jin:
                            data.user_array_globale[i][2] = newname
                    print("Role sudah diganti")
            else:
                print("Username bukan jin")
        else:
            print("Tidak ada jin dengan username tersebut")

# ALGORITMA F6
def bangun():
    if isJinPembangun():
        pembangun_found = False
        pasir = random.randrange(1,6)
        batu = random.randrange(1,6)
        air = random.randrange(1,6)
        for j in range(103):
            if data.user_array_globale[j][2] == "jin_pembangun":
                pembangun_found = True
        if pembangun_found == True:
            if pasir <= int(data.bahanbangunan_array_globale[1][2]) and batu <= int(data.bahanbangunan_array_globale[2][2]) and air <= int(data.bahanbangunan_array_globale[3][2]):
                jumlahpasir = int(data.bahanbangunan_array_globale[1][2])
                jumlahbatu = int(data.bahanbangunan_array_globale[2][2])
                jumlahair = int(data.bahanbangunan_array_globale[3][2])
                jumlahpasir -= pasir
                jumlahbatu -= batu
                jumlahair -= air
                data.bahanbangunan_array_globale[1][2] = str(jumlahpasir)
                data.bahanbangunan_array_globale[2][2] = str(jumlahbatu)
                data.bahanbangunan_array_globale[3][2] = str(jumlahair)
                for j in range(1,101):
                    if data.candi_array_globale[j][0] == '':
                        data.candi_array_globale[j][0] = j
                        data.candi_array_globale[j][1] = data.username
                        data.candi_array_globale[j][2] = pasir
                        data.candi_array_globale[j][3] = batu
                        data.candi_array_globale[j][4] = air
                        break 
                print("Candi terbangun")
                candi_built = 0
                for j in range(1,101):
                    if data.candi_array_globale[j][0] != '':
                        candi_built += 1
                print("Sisa candi yang perlu dibangun",100-candi_built)
            else:
                print("Bahan tidak cukup")

# ALGORITMA F7
def kumpul():
    if isJinPengumpul():
        pasir = random.randrange(1,6)
        batu = random.randrange(1,6)
        air = random.randrange(1,6)
        data.bahanbangunan_array_globale[1][2] = str(int(data.bahanbangunan_array_globale[1][2]) + pasir)
        data.bahanbangunan_array_globale[2][2] = str(int(data.bahanbangunan_array_globale[2][2]) + batu)
        data.bahanbangunan_array_globale[3][2] = str(int(data.bahanbangunan_array_globale[3][2]) + air)
        print("Jin menemukan "+str(pasir)+" pasir, "+str(batu)+" batu, dan "+str(air)+" air.")

# ALGORITMA F8
def batchkumpul():
    if data.username == "Bandung":
        pengumpuls = 0
        totalpasir = 0
        totalbatu = 0
        totalair = 0
        for j in range(1,103):
            if data.user_array_globale[j][2] == "jin_pengumpul":
                pengumpuls += 1
        for j in range(pengumpuls):
            pasir = random.randrange(1,6)
            batu = random.randrange(1,6)
            air = random.randrange(1,6)
            totalpasir += pasir
            totalbatu += batu
            totalair += air
        data.bahanbangunan_array_globale[1][2] = str(int(data.bahanbangunan_array_globale[1][2]) + totalpasir)
        data.bahanbangunan_array_globale[2][2] = str(int(data.bahanbangunan_array_globale[2][2]) + totalbatu)
        data.bahanbangunan_array_globale[3][2] = str(int(data.bahanbangunan_array_globale[3][2]) + totalair)
        if pengumpuls > 0:
            print("Mengerahkan "+str(pengumpuls)+" jin untuk mengumpulkan bahan.")
            print("Jin menemukan total "+str(totalpasir)+" pasir, "+str(totalbatu)+" batu, dan "+str(totalair)+" air.")
        else:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def batchbangun():
    if data.username == "Bandung":
        conti = True
        pembanguns = 0
        totalpasir = 0
        totalbatu = 0
        totalair = 0
        for j in range(1,103):
            if data.user_array_globale[j][2] == "jin_pembangun":
                pembanguns += 1
        if pembanguns > 0:
            builder_identity = [('') for i in range(pembanguns)]
        builder_count = 0
        for j in range(1,103):
            if data.user_array_globale[j][2] == "jin_pembangun":
                builder_identity[builder_count] = data.user_array_globale[j][0]
                builder_count += 1
        pasir = [(random.randrange(1,6)) for k in range(pembanguns)]
        batu = [(random.randrange(1,6)) for k in range(pembanguns)]
        air = [(random.randrange(1,6)) for k in range(pembanguns)]
        for j in range(pembanguns):
            totalpasir += pasir[j]
            totalbatu += batu[j]
            totalair += air[j]
        if pembanguns > 0:
            if (totalpasir-int(data.bahanbangunan_array_globale[1][2])) < 0:
                selisihpasir = 0
            else:
                selisihpasir = (abs(totalpasir-int(data.bahanbangunan_array_globale[1][2])))
            if (totalbatu-int(data.bahanbangunan_array_globale[2][2])) < 0:
                selisihbatu = 0
            else:
                selisihbatu = (abs(totalbatu-int(data.bahanbangunan_array_globale[2][2])))
            if (totalair-int(data.bahanbangunan_array_globale[3][2])) < 0:
                selisihair = 0
            else:
                selisihair = (abs(totalair-int(data.bahanbangunan_array_globale[3][2])))
            if totalpasir <= int(data.bahanbangunan_array_globale[1][2]) and totalbatu <= int(data.bahanbangunan_array_globale[2][2]) and totalair <= int(data.bahanbangunan_array_globale[3][2]):
                print("Mengerahkan "+str(pembanguns)+" jin untuk membangun candi dengan total bahan "+str(totalpasir)+" pasir, "+str(totalbatu)+" batu, dan "+str(totalair)+" air.")
                print("Jin berhasil membangun total "+str(pembanguns)+" candi.")
                jumlahpasir = int(data.bahanbangunan_array_globale[1][2])
                jumlahbatu = int(data.bahanbangunan_array_globale[2][2])
                jumlahair = int(data.bahanbangunan_array_globale[3][2])
                jumlahpasir -= totalpasir
                jumlahbatu -= totalbatu
                jumlahair -= totalair
                data.bahanbangunan_array_globale[1][2] = str(jumlahpasir)
                data.bahanbangunan_array_globale[2][2] = str(jumlahbatu)
                data.bahanbangunan_array_globale[3][2] = str(jumlahair)
                builder_count = 0
                for j in range(1,101):
                    if data.candi_array_globale[j][0] == '':
                        data.candi_array_globale[j][0] = j
                        data.candi_array_globale[j][1] = builder_identity[builder_count]
                        data.candi_array_globale[j][2] = pasir[builder_count]
                        data.candi_array_globale[j][3] = batu[builder_count]
                        data.candi_array_globale[j][4] = air[builder_count]
                        builder_count += 1
                        if builder_count == pembanguns:
                            conti = False
                    if conti == False:
                        break
            else:
                print("Mengerahkan "+str(pembanguns)+" jin untuk membangun candi dengan total bahan "+str(totalpasir)+" pasir, "+str(totalbatu)+" batu, dan "+str(totalair)+" air.")
                print("Bangun gagal. Kurang "+str(abs(selisihpasir))+" pasir, "+str(abs(selisihbatu))+" batu, dan "+str(abs(selisihair))+ " air.")
        else:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

# ALGORITMA F9
def counte(string):
    counte = 0
    for j in range(1,101):
        if data.candi_array_globale[j][1] == string:
            counte += 1
    return counte    

def laporanjin():
    if data.username == "Bandung":
        totaljin = 0
        totaljinpengumpul = 0
        totaljinpembangun = 0
        for j in range(1,103):
            if data.user_array_globale[j][0] != '' and data.user_array_globale[j][0] != 'Bandung' and data.user_array_globale[j][0] != 'RoroJonggrang':
                totaljin += 1
                if data.user_array_globale[j][2] == 'jin_pengumpul':
                    totaljinpengumpul += 1
                elif data.user_array_globale[j][2] == "jin_pembangun":
                    totaljinpembangun += 1
        candi_array_temporary = [[('') for j in range(5)] for i in range(101)]
        for i in range(5):
            for j in range(101):
                candi_array_temporary[j][i]  = data.candi_array_globale[j][i]
        candi_owner_count = [[('') for j in range(2)] for i in range(101)]
        for j in range(1,101):
            if candi_array_temporary[j][1] != '':
                candi_owner_count[j][0] = candi_array_temporary[j][1]
                candi_owner_count[j][1] = counte(candi_array_temporary[j][1])
                for k in range(1,101):
                    if candi_array_temporary[k][1] == candi_owner_count[j][0]:
                        candi_array_temporary[k][0] = ''
                        candi_array_temporary[k][1] = ''
                        candi_array_temporary[k][2] = ''
                        candi_array_temporary[k][3] = ''
                        candi_array_temporary[k][4] = ''
        max_count = 0
        min_count = 102
        candi_max_candidate = [('') for i in range(101)]
        candi_min_candidate = [('') for i in range(101)]
        max_candidate_count = 0
        min_candidate_count = 0
        for j in range(1,101):
            if candi_owner_count[j][0] != '':
                if candi_owner_count[j][1] > max_count:
                    max_count = candi_owner_count[j][1]
                if candi_owner_count[j][1] < min_count:
                    min_count = candi_owner_count[j][1]
        for j in range(1,101):
            if candi_owner_count[j][0] != '':
                if candi_owner_count[j][1] == max_count:
                    candi_max_candidate[max_candidate_count] = candi_owner_count[j][0]
                    max_candidate_count += 1
                if candi_owner_count[j][1] == min_count:
                    candi_min_candidate[min_candidate_count] = candi_owner_count[j][0]
                    min_candidate_count += 1
        most_dilligent = candi_max_candidate[0]
        laziest = candi_min_candidate[0]
        for j in range(100):
            if candi_max_candidate[j] < most_dilligent and candi_max_candidate[j] != '':
                most_dilligent = candi_max_candidate[j]
            if candi_min_candidate[j] > laziest and candi_min_candidate[j] != '':
                laziest = candi_min_candidate[j]
        print("Total Jin:",totaljin)
        print("Total Jin Pengumpul:",totaljinpengumpul)
        print("Total Jin Pembangun:",totaljinpembangun)
        print("Jin Terajin:",most_dilligent)
        print("Jin Termalas:",laziest)
        print("Jumlah Pasir:",data.bahanbangunan_array_globale[1][2],"unit")
        print("Jumlah Air:",data.bahanbangunan_array_globale[2][2],"unit")
        print("Jumlah Batu:",data.bahanbangunan_array_globale[3][2],"unit")

# ALGORITMA F10
def laporancandi():
    if data.username == "Bandung":
        totalcandi = 0
        totalpasir = 0
        totalbatu = 0
        totalair  = 0
        idexpensive = 0
        idcheap = 99999999
        idex = 0
        idch = 0
        for j in range(1,101):
            if data.candi_array_globale[j][0] != '':
                totalcandi += 1
                totalpasir += int(data.candi_array_globale[j][2])
                totalbatu += int(data.candi_array_globale[j][3])
                totalair += int(data.candi_array_globale[j][4])
                price = (int(data.candi_array_globale[j][2])*10000)+(int(data.candi_array_globale[j][3])*15000)+(int(data.candi_array_globale[j][4])*7500)
                if price > idexpensive:
                    idexpensive = price
                    idex = j
                if price < idcheap:
                    idcheap = price
                    idch = j
        print("Total Candi:",totalcandi)
        print("Total pasir yang digunakan:",totalpasir)
        print("Total batu yang digunakan:",totalbatu)
        print("Total air yang digunakan:",totalair)
        if idexpensive != 0:
            print("ID Candi Termahal: "+str(idex)+" (Rp "+str(idexpensive)+")")
        else:
            print("ID Candi Termahal: ")
        if idcheap != 99999999:
            print("ID Candi Termurah: "+str(idch)+" (Rp "+str(idcheap)+")")
        else:
            print("ID Candi Termurah: ")

# ALGORITMA F11
def hancurkancandi():
    if data.username == 'RoroJonggrang':
        found = False
        destroy_candi = input("Masukkan ID candi: ")
        for j in range(101):
            if str(data.candi_array_globale[j][0]) == destroy_candi:
                found = True
                are_you_sure = input("Apakah anda yakin ingin menghancurkan ID: "+destroy_candi+" (Y/N)? ")
                if are_you_sure == "Y" or are_you_sure == "y":
                    data.candi_array_globale[j][0] = ''
                    data.candi_array_globale[j][1] = ''
                    data.candi_array_globale[j][2] = ''
                    data.candi_array_globale[j][3] = ''
                    data.candi_array_globale[j][4] = ''
                    print()
                    print("Candi telah berhasil dihancurkan")
        if found == False:
            print("Tidak ada candi dengan ID tersebut.")
            print()
            hancurkancandi()

# ALGORITMA F12
def ayamberkokok():
    if data.username == "RoroJonggrang":
        data.endthis = False
        totalcandi = 0
        for j in range(1,101):
            if data.candi_array_globale[j][0] != '':
                totalcandi += 1
        print("Jumlah Candi:",totalcandi)
        if totalcandi < 100:
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print()
            print("Roro Jonggrang dikutuk menjadi candi")
        else:
            print("Yah, Bandung Bondowoso memenangkan permainan")
        data.endthis = True

# ALGORITMA F13
def load(folder):
# memuat data yang sesuai dengan struktur data eksternal. 
    user_read(f"{folder}/user.csv")
    candi_read(f"{folder}/candi.csv")
    bahanbangunan_read(f"{folder}/bahan_bangunan.csv")
    return

# ALGORITMA F14
def save():
    if data.username != '':
        print()
        import os.path
        where = input("Masukkan nama folder: ")
        directory = './save/'
        directory2 = where+"/"
        candifile = "candi.csv"
        userfile = "user.csv"
        bahanbangunanfile = "bahan_bangunan.csv"
        user_effective = 0
        candi_effective = 0
        bahanbangunan_effective = 0
        print()
        print("Saving....")
        file_path = os.path.join(directory, directory2, candifile)
        file_path2 = os.path.join(directory, directory2, userfile)
        file_path3 = os.path.join(directory, directory2, bahanbangunanfile)
        saveloc = "save/"+directory2
        if not os.path.isdir(directory):
            os.mkdir(directory)
            print()
            print("Membuat folder save")
            os.mkdir(directory+directory2)
            print("Membuat folder "+saveloc)
        elif not os.path.isdir(directory+directory2):
            print()
            print("Membuat folder "+saveloc)
            os.mkdir(directory+directory2)
        file = open(file_path, "w")
        for j in range(101):
            if data.candi_array_globale[j][0] != '':
                candi_effective += 1
        for j in range(103):
            if data.user_array_globale[j][0] != '':
                user_effective += 1
        for j in range(4):
            if data.bahanbangunan_array_globale[j][0] != '':
                bahanbangunan_effective += 1
        candi_available = 0
        user_available = 0
        bahanbangunan_available = 0
        for j in range(101):
            if data.candi_array_globale[j][0] != '':
                candi_available += 1
                for i in range(5):
                    file.write(str(data.candi_array_globale[j][i]))
                    if i < 4:
                        file.write(";")
                if j < 100 and not candi_available == candi_effective:
                    file.write("\n")
            else:
                if j < 100 and not candi_available == candi_effective:
                    file.write("\n")
            if candi_available == candi_effective:
                break
        file2 = open(file_path2, "w")
        for j in range(103):
            if data.user_array_globale[j][0] != '':
                user_available += 1
                for i in range(3):
                    file2.write(str(data.user_array_globale[j][i]))
                    if i < 2:
                        file2.write(";")
                if j < 102 and not user_available == user_effective:
                    file2.write("\n")
            else:
                if j < 102 and not user_available == user_effective:
                    file2.write("\n")
            if user_available == user_effective:
                break
        file3 = open(file_path3, "w")
        for j in range(4):
            if data.bahanbangunan_array_globale[j][0] != '':
                for i in range(3):
                    file3.write(str(data.bahanbangunan_array_globale[j][i]))
                    if i < 2:
                        file3.write(";")
                if j < 3:
                    file3.write("\n")
            else:
                if j < 3:
                    file3.write("\n")
            bahanbangunan_available += 1
            if bahanbangunan_available == bahanbangunan_effective:
                break
        print("Berhasil menyimpan data di "+saveloc)
        file.close()
        file2.close()
        file3.close()

# ALGORITMA F15
def help():
    if data.username == "Bandung":
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("Untuk memanggil jin")
        print("3. ubahjin")
        print("Untuk mengubah jin")
        print("4. hapusjin")
        print("Menghapus jin tertentu")
        print("5. batchkumpul")
        print("Menyuruh semua jin pengumpul untuk mengumpulkan material")
        print("6. batchbangun")
        print("Menyuruh semua jin pembangun untuk membangun candi")
        print("7. laporanjin")
        print("Memberi laporan terkait jin")
        print("8. laporancandi")
        print("Memberi laporan terkait candi")
        print("9. save")
        print("Menyimpan progres permainan")
        print("10. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif data.username == "RoroJonggrang":
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("Menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. save")
        print("Menyimpan progres permainan")
        print("5. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif isJinPembangun():
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("Untuk membangun candi")
        print("3. save")
        print("Menyimpan progres permainan")
        print("4. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif isJinPengumpul():
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("Untuk mengumpulkan bahan untuk candi")
        print("3. save")
        print("Menyimpan progres permainan")
        print("4. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    else:
        print("1. login")
        print("Untuk masuk menggunakan akun")
        print("2. exit")
        print("Untuk keluar dari program dan kembali ke terminal")

# ALGORITMA F16
def exete():
    wanna_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if wanna_save == "Y" or wanna_save == "y":
        save()
        quit()
    elif wanna_save == "N" or wanna_save == "n":
        quit()
    else:
        exete()

def run(func):
    if func == "bangun":
        bangun()
    elif func == "ubahjin":
        ubahjin()
    elif func == "login":
        login()
    elif func == "logout":
        logout()
    elif func == "summonjin":
        summonjin()
    elif func == "hapusjin":
        hapusjin()
    elif func == "kumpul":
        kumpul()
    elif func == "batchkumpul":
        batchkumpul()
    elif func == "batchbangun":
        batchbangun()
    elif func == "laporanjin":
        laporanjin()
    elif func == "laporancandi":
        laporancandi()
    elif func == "hancurkancandi":
        hancurkancandi()
    elif func == "ayamberkokok":
        ayamberkokok()
    elif func == "save":
        save()
    elif func == "help":
        help()
    elif func == "exit":
        exete()
