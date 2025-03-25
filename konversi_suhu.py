import re

# Struktur Data
SATUAN_SUHU = ("Celsius", "Fahrenheit", "Kelvin")
VALID_SATUAN = set(SATUAN_SUHU)  

def konversi_suhu(nilai: float, dari: str, ke: str) -> float:
    if dari == ke:
        return nilai
    
    # Konversi melalui Celsius sebagai pivot
    if dari == "Celsius":
        if ke == "Fahrenheit":
            return (nilai * 9/5) + 32
        elif ke == "Kelvin":
            return nilai + 273.15
    elif dari == "Fahrenheit":
        if ke == "Celsius":
            return (nilai - 32) * 5/9
        elif ke == "Kelvin":
            return (nilai - 32) * 5/9 + 273.15
    elif dari == "Kelvin":
        if ke == "Celsius":
            return nilai - 273.15
        elif ke == "Fahrenheit":
            return (nilai - 273.15) * 9/5 + 32
    
    raise ValueError("Konversi tidak valid!")

def validasi_angka(input_str: str) -> float:
    """
    Validasi input nilai suhu menggunakan regex.
    Format: Angka (positif/negatif) dengan optional desimal.
    """
    pola = re.compile(r"^-?\d+(\.\d+)?$")
    if not pola.match(input_str):
        raise ValueError("Input harus berupa angka!")
    return float(input_str)

def main():
    print("=== KONVERTER SUHU ===")
    print(f"Satuan yang tersedia: {', '.join(SATUAN_SUHU)}\n")
    
    while True:
        try:
            # Input nilai suhu
            nilai_str = input("Masukkan nilai suhu: ").strip()
            nilai = validasi_angka(nilai_str)
            
            # Input satuan asal
            dari = input(f"Konversi dari satuan ({'/'.join(SATUAN_SUHU)}): ").strip().capitalize()
            if dari not in VALID_SATUAN:
                print(f"Error: Satuan '{dari}' tidak valid!")
                continue
            
            # Input satuan tujuan
            ke = input(f"Ke satuan ({'/'.join(SATUAN_SUHU)}): ").strip().capitalize()
            if ke not in VALID_SATUAN:
                print(f"Error: Satuan '{ke}' tidak valid!")
                continue
            
            # Proses konversi
            hasil = konversi_suhu(nilai, dari, ke)
            print(f"\nHasil: {nilai} {dari} = {hasil:.2f} {ke}\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        
        except KeyboardInterrupt:
            print("\nProgram dihentikan.")
            break
        
        # Tanya user apakah ingin lanjut
        lanjut = input("Konversi lagi? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Terima kasih!")
            break

if __name__ == "__main__":
    main()