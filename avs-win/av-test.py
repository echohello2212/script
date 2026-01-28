#!/usr/bin/env python3

import platform
import sys
import os
import time
from pathlib import Path


def main():
    # Steg 1: Identifiera operativsystem
    print("[+] Identifierar operativsystem...")
    os_name = platform.system()
    
    if os_name != "Windows":
        print("[!] Detta script är endast avsett för Windows.")
        print(f"[!] Upptäckt OS: {os_name}")
        print("[!] Avslutar utan fel.")
        sys.exit(0)
    
    print(f"[+] Operativsystem: {os_name}")
    
    # Steg 2: Definiera EICAR-teststrängen (notera att backslash måste escape:as)
    print("[+] Definierar EICAR-teststrängen...")
    eicar_string = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    print("[+] EICAR-strängen är definierad.")
    
    # Steg 3: Välj output-plats (Desktop)
    print("[+] Bestämmer output-plats...")
    userprofile = os.environ.get("USERPROFILE")
    if not userprofile:
        print("[!] FEL: Miljövariabeln USERPROFILE hittades inte.")
        sys.exit(1)
    output_dir = Path(userprofile) / "Desktop"
    print(f"[+] Använder Skrivbordet: {output_dir}")
    
    # Skapa katalogen om den inte finns
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        print(f"[+] Katalogen är redo: {output_dir}")
    except PermissionError:
        print(f"[!] FEL: Åtkomst nekad när katalog skulle skapas: {output_dir}")
        sys.exit(1)
    except OSError as e:
        print(f"[!] FEL: Misslyckades att skapa katalog: {e}")
        sys.exit(1)
    
    # Bestäm output-filens sökväg
    output_file = output_dir / "AV-TEST-NOT-DANGEROUS.txt"
    print(f"[+] Output-fil: {output_file}")
    
    # Steg 4: Skriv EICAR-filen
    print("[+] Skriver EICAR-testfilen...")
    try:
        with open(output_file, "w", encoding="ascii", newline="\n") as f:
            f.write(eicar_string)
        print(f"[+] Filen skrevs utan problem: {output_file}")
    except PermissionError:
        print(f"[!] FEL: Åtkomst nekad när filen skulle skrivas: {output_file}")
        sys.exit(1)

    
    # Steg 5: Vänta 3 sekunder så att AV/EDR hinner reagera
    print("[~] Väntar 3 sekunder så att AV/EDR hinner reagera...")
    time.sleep(3)
    print("[+] Väntan klar.")
    
    # Steg 6: Kontrollera filstatus
    print("[?] Kontrollerar filstatus...")
    
    if not output_file.exists():
        print("[!] Filen saknas.")
        print("[!] AV/EDR har troligen tagit bort eller karantänat filen (förväntat beteende).")
        print("[+] Testresultat: Antivirus/EDR är aktiv och upptäckte EICAR-testfilen.")
    else:
        print("[+] Filen finns kvar. Läser innehållet för verifiering...")
        try:
            with open(output_file, "r", encoding="ascii") as f:
                file_content = f.read()
            
            # Jämför innehåll
            if file_content == eicar_string:
                print("[!] Filens innehåll matchar EICAR-strängen exakt.")
                print("[!] Filen ligger kvar och är oförändrad.")
                print("[?] Möjliga orsaker:")
                print("[?]   - Antivirus/EDR kan vara avstängt")
                print("[?]   - Katalogen kanske inte skannas av AV/EDR")
                print("[?]   - AV/EDR kanske inte känner igen EICAR-signaturen")
            else:
                print("[!] Filens innehåll matchar inte EICAR-strängen.")
                print("[!] Innehållet verkar ha ändrats.")
                print("[?] AV/EDR har troligen modifierat filen. Kontrollera AV-loggar för detaljer.")
                print(f"[?] Förväntad längd: {len(eicar_string)}, Faktisk längd: {len(file_content)}")
        
        except PermissionError:
            print("[!] Åtkomst nekad när filen skulle läsas.")
            print("[!] AV/EDR har troligen blockerat åtkomst till filen.")
            print("[+] Testresultat: Antivirus/EDR är aktiv och hanterar filen.")
        except Exception as e:
            print(f"[!] Undantag inträffade vid läsning av filen: {e}")
            print("[!] AV/EDR har troligen hanterat filen på ett oväntat sätt.")
            print("[+] Testresultat: Interaktion med antivirus/EDR upptäcktes.")
    
    print("\n[+] Scriptet är klart.")


if __name__ == "__main__":
    main()
