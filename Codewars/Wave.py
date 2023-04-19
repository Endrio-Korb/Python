def wave(people):
    frase = ""
    lista = []

    frase = str(people[0])
    frase = frase.strip()
    
    for letra in frase:
        letra2 = letra
        letra = letra.upper()

        frasenova = frase.replace(letra2, letra)
        lista.append(frasenova)
    
    return lista
        
# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
# not working

if __name__ == "__main__":

    people = ["  gap  "]

    print(wave(people))