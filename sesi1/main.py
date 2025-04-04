import random #ini adalah cara untuk memanggil library di python

salam = "SELAMAT DATANG DI CUYPY GAMES!"
cuypy_position = random.randint(1, 4)


print("****************")
print(f"*** {salam} ***")
print("****************")

nama_user = input("masukkan nama anda : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()

goa[cuypy_position - 1] = "dea"

print(f" Halo {nama_user}")
print(f'''
      coba lihat goa dibawah ini!
      {goa_kosong}
    ''')
tebakan = int(input("di goa nomor berapa cuypy berada?"))

confirm = input(f"apakah kamu yakin cuypy berada di goa nomor {tebakan} ?  [y/n] : ")

if confirm == "n":
    print("program dihentikan")
    exit()
elif confirm == "y":
    if tebakan == cuypy_position:
        print(f"{goa}, \n selamat kamu menang ")
    else:
        print(f"{goa}, \n kamu kalah")
else:
    print("maaf jawaban tidak tersedia, silahkan ulangi programnya!")
    exit()


# while True:
# 	tebakan = int(input("Menurut kamu, CUYPY ada di goa nomer berapa?  1/2/3/4:  "))
# 	print()
# 	konfirmasi = input((f"Apakah kamu yakin, Nomor {tebakan} adalah jawabannya? yes/no:"))
# 	print()

# 	if konfirmasi == "yes":
# 		break
# 	elif konfirmasi == "no":
# 		print("Tidak Yakin? coba lagi!")
# 	else:
# 		print("input tidak valid, Silahkan masukkan jawaban yang benar!  yes/no:")

# print()

