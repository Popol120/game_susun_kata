import random
import time

def acak_kata(kata):
    """Mengacak huruf-huruf dalam sebuah kata"""
    huruf = list(kata)
    random.shuffle(huruf)
    return ''.join(huruf)

def main():
    print("""
    ==================================
          GAME SUSUN KATA (WORD SCRAMBLE)
    ==================================
    """)
    
    # Daftar kata untuk game
    daftar_kata = [
        "python", "program", "komputer", "algorithm", "developer",
        "function", "variable", "string", "integer", "boolean",
        "loop", "dictionary", "list", "tuple", "syntax",
        "debug", "compile", "runtime", "exception", "module"
    ]
    
    skor = 0
    level = 1
    maks_level = 5
    
    while level <= maks_level:
        # Pilih kata secara acak
        kata_asli = random.choice(daftar_kata)
        kata_acak = acak_kata(kata_asli)
        
        print(f"\nLevel {level} dari {maks_level}")
        print(f"Susunlah huruf-huruf ini menjadi kata yang benar: {kata_acak}")
        
        mulai_waktu = time.time()
        tebakan = input("Jawaban Anda: ").lower().strip()
        waktu_selesai = time.time()
        waktu_bermain = waktu_selesai - mulai_waktu
        
        if tebakan == kata_asli:
            # Hitung skor berdasarkan kecepatan (max 100 poin per level)
            poin = max(0, 100 - int(waktu_berplaying * 10))
            skor += poin
            print(f"Benar! 🎉 Anda mendapatkan {poin} poin. Skor total: {skor}")
            level += 1
        else:
            print(f"Salah! 😢 Kata yang benar adalah: {kata_asli}")
            print(f"Skor Anda tetap: {skor}")
            # Tidak naik level jika salah
    
    print("\n==================================")
    print(f"Selamat! Anda menyelesaikan semua level!")
    print(f"Total skor Anda: {skor}")
    print("==================================")

if __name__ == "__main__":
    main()
