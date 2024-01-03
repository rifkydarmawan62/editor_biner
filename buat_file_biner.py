from tkinter.filedialog import asksaveasfilename as simpan_file
from subprocess import run
from colorama import Fore

try:
    while True:
        try:
            ukuran_memori_byte = int(input(f"{Fore.RESET}Masukkan jumlah ukuran memori byte : "))
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Input harus berupa angka!")
        else:
            if ukuran_memori_byte > 0:
                print(f"{Fore.LIGHTBLUE_EX}Tekan Alt + Tab untuk membuka jendela baru")
                file_disimpan = simpan_file(title = "Simpan file", confirmoverwrite = True, filetypes = [("File biner", ".bin")], initialfile = ".bin")
                if file_disimpan:
                    data_heksadesimal : str = ""
                    for alamat_memori_byte in range(ukuran_memori_byte):
                        alamat_memori_byte = "0" + hex(alamat_memori_byte)[2:] if len(hex(alamat_memori_byte)[2:]) == 1 else hex(alamat_memori_byte)[2:]
                        while True:
                            try:
                                nilai_desimal = int(input(f"{Fore.RESET}Alamat memori byte {alamat_memori_byte} | Masukkan nilai desimal [0-255] : "))
                            except ValueError:
                                print(f"{Fore.LIGHTRED_EX}Input harus berupa angka!")
                            else:
                                if nilai_desimal >= 0 and nilai_desimal <= 255:
                                    data_heksadesimal_baru = "0" + hex(nilai_desimal)[2:] if len(hex(nilai_desimal)[2:]) == 1 else hex(nilai_desimal)[2:]
                                    print(f"{Fore.LIGHTBLUE_EX}nilai desimal {nilai_desimal} = nilai heksadesimal {data_heksadesimal_baru}")
                                    data_heksadesimal += data_heksadesimal_baru
                                    break
                                else:
                                    print(f"{Fore.LIGHTRED_EX}Input harus dalam jangkauan angka 0 - 255!")
                    print(f"{Fore.LIGHTGREEN_EX}Menyimpan file ...")
                    with open(file_disimpan, "wb") as kode_biner:
                        kode_biner.write(bytes.fromhex(data_heksadesimal))
                    PERINTAH_POWERSHELL = ["PowerShell", f"format-hex \"{file_disimpan}\""]
                    print(f"{Fore.LIGHTGREEN_EX}File biner disimpan!\n{Fore.LIGHTYELLOW_EX}Menjalankan perintah PowerShell [{PERINTAH_POWERSHELL[1]}] ...{Fore.LIGHTBLUE_EX}")
                    run(PERINTAH_POWERSHELL, shell = True); print(Fore.RESET, end = None)
                    break
                else:
                    print(f"{Fore.LIGHTRED_EX}File tidak disimpan!")
                    argumen = input(f"{Fore.RESET}Lanjut [1|0] (default = keluar) : ")
                    if argumen.strip() == "1":
                        continue
                    else:
                        print("Program ditutup!")
                        break
            else:
                print(f"{Fore.LIGHTRED_EX}Angka harus lebih dari nol!")
except KeyboardInterrupt:
    print("Program ditutup!")