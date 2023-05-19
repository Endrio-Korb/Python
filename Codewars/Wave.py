def wave(people):
    frase = ""
    lista = []
    try:
        frase = str(people[0])
        frase = frase.lower()
        frase = frase.strip()
        
        for letra in frase:
            frasenova = frase.replace(letra, letra.upper())
            lista.append(frasenova)
        
        return lista
    
    except IndexError:
        return lista
        
# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python
# not working

if __name__ == "__main__":

    people = ["tHis is a few words"]

    print(wave(people))