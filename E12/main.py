import argparse
import detectSpanish

abc = {
    'A':'E', 'B':'F', 'C':'G', 'D':'H', 'E':'I',
    'F':'J', 'G':'K', 'H':'L', 'I':'M', 'J':'N',
    'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
    'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X',
    'U':'Y', 'V':'Z', 'W':'A', 'X':'B', 'Y':'C',
    'Z':'D'
}

def Encriptar(mensaje):
    mensaje = mensaje.upper()
    FraseEnc = '' #str vacio
    for letra in mensaje: #recorro Frase letra por letra
        encontrado = False
        for x,y in abc.items():
            if letra == x:
                FraseEnc += y #fraseEnc.append(y)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseEnc += letra
    print("Mensaje Encriptado:", FraseEnc)


def Desencriptar(mensaje):
    mensaje = mensaje.upper()
    FraseDes = ''
    for letra in mensaje:
        encontrado = False
        for x,y in abc.items():
            if letra == y:
                FraseDes += x #fraseEnc.append(x)
                encontrado = True
        if not encontrado: #if encontrado == False
            FraseDes += letra
    print("Mensaje Desencriptado:", FraseDes)

def cipher_encrypt(message, clave):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("Mensaje Encriptado:", translated)

def cipher_decrypt(message, clave):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("Mensaje Desencriptado:", translated)

def Cracker(message):
    # Caesar Cipher Hacker
    # https://www.nostarch.com/crackingcodes (BSD Licensed)
    # LspeAqyrhsAqyrhmep
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''
        # The rest of the program is almost the same as the original program:
        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol
        # Display every possible decryption:
        print('Key #%s: %s' % (key, translated))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m","-modo", dest="modo",help = "(e)Encriptar (d)Desencriptar (c)Crackear")
    parser.add_argument("-mensaje", dest = "mensaje", help = "Especifica el mensaje a cifrar,desencriptar o crackear")
    parser.add_argument("-key",dest = "key", help = "Argumento opcional para cuando el proceso a realizar es de Cifrar o descifrar")
    args = parser.parse_args()
    #Encript mode
    if args.modo == "e" and args.mensaje and not args.key:
        detectSpanish.isSpanish(args.mensaje)
        Encriptar(args.mensaje)
    #Decript mode
    if args.modo == "d" and args.mensaje and not args.key:
        detectSpanish.isSpanish(args.mensaje)
        Desencriptar(args.mensaje)
    #Encript with key
    if args.modo == "e" and args.key:
        detectSpanish.isSpanish(args.mensaje)
        cipher_encrypt(args.mensaje, args.key)
    #Decript with key
    if args.modo == "d" and args.key:
        detectSpanish.isSpanish(args.mensaje)
        cipher_decrypt(args.mensaje, args.key)
    #Cracker mode
    if args.modo == "c":
        detectSpanish.isSpanish(args.mensaje)
        Cracker(args.mensaje)

if __name__ == "__main__":
    main()
