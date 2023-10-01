# OVPN Exterminator - geschreven door Michael van der Heiden
# Laatste aanpassing op 01-10-2023 (DD:MM:YYYY)
# STUDENT AAN NOVI HOGESCHOOL UTRECHT

import os

def delete_files_by_extension(folder_path, file_extension):
    try:
        # Zeker weten  dat de folder bestaat
        if os.path.exists(folder_path):
            found_files = False  # flag om te checken of er files bestaan
            # de complete folder checken wat erin staat
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)

                # Valideren dat er bestanden aanwezig zijn met de juiste extensie om te verwijderen
                if os.path.isfile(file_path) and filename.endswith(file_extension):
                    os.remove(file_path)
                    print(f"'{file_extension}' gevonden en verwijderd.")
                    found_files = True
            
            # Valideren dat de folder locatie klopt en of er errors zijn, anders laten zien dat er niks is gevonden
            if not found_files:
                print(f"'{file_extension}' niet gevonden of verwijderd")
        else:
            print(f"Download folder '{folder_path}' bestaat niet, zet het juiste pad in de exterminator!")
    except Exception as e:
        print(f"Iets is niet goed gegaan: {e}")

if __name__ == "__main__":
    # Pad naar de Downloads folder
    download_folder = "/home/kali/Downloads"
    
    # Welke extensie wil je verwijderen?
    file_extension_to_delete = ".ovpn"
    
    # Functie om de bestanden te wissen met de juiste extensie
    delete_files_by_extension(download_folder, file_extension_to_delete)
