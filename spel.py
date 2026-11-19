#STORYLINE...

import modul_demo 
modul_demo.text

print("Du är den utvalde.")
print("Universum behöver din hjälp.")
while True:
    try:    
        svar = input("Är du redo? [ja/nej]")
        if svar == "Ja" or svar == "ja":
            print("Nu börjar äventyret. Gör dig redo att rädda universum!")
            break
        elif svar == "Nej" or svar == "nej":
            print("game over")
            break

    except:
        print("Något gick fel.")

"""
░██    ░██                                                ░████       ░██    ░██                                    ░██                                   
░██    ░██                                               ░██          ░██    ░██                                    ░██                                   
░██    ░██  ░███████  ░██    ░██    ░██     ░███████  ░████████    ░████████ ░████████   ░███████      ░███████  ░████████  ░██████   ░██░████  ░███████  
░██    ░██ ░██    ░██ ░██    ░██    ░██    ░██    ░██    ░██          ░██    ░██    ░██ ░██    ░██    ░██           ░██          ░██  ░███     ░██        
 ░██  ░██  ░██    ░██  ░██  ░████  ░██     ░██    ░██    ░██          ░██    ░██    ░██ ░█████████     ░███████     ░██     ░███████  ░██       ░███████  
  ░██░██   ░██    ░██   ░██░██ ░██░██      ░██    ░██    ░██          ░██    ░██    ░██ ░██                  ░██    ░██    ░██   ░██  ░██             ░██ 
   ░███     ░███████     ░███   ░███        ░███████     ░██           ░████ ░██    ░██  ░███████      ░███████      ░████  ░█████░██ ░██       ░███████  
                                                                                                                                                          
                                                                                                                                                          
                                                                                                                                                          
"""

        