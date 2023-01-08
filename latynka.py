

abetka_k = "А,а,Б,б,В,в,Г,г,Ґ,ґ,Д, д, Е, е, Є, є, Ж, ж, З, з, И, и, І, і, Ї, ї, Й, й, К, к, Л, л, М, м, Н, н, О, о, П, п, Р, р, С, с, Т, т, У, у, Ф, ф, Х, х, Ц, ц, Ч, ч, Ш, ш, Щ, щ, ь, Ю, ю, Я, я, '"
abetka_l = "A,a,B,b,V,v,G,g,Ĝ,ĝ,D, d, E, e, Je, je, Ž, ž, Z, z, Y, y, I, i, Ji, ji, J, j, K, k, L, l, M, m, N, n, O, o, P, p, R, r, S, s, T, t, U, u, F, f, H, h, C, c, Č, č, Š, š, Šč, šč, ', Ju, ju, Ja, ja, ’"

list_k = abetka_k.split(",")
list_l = abetka_l.split(",")
list_k_s = [i.replace(" ", "") for i in list_k]
list_l_s = [i.replace(" ", "") for i in list_l]
prygolosni = "цкнгшщзхфврплджчсмтб"

def replace_forward(ukr):
    lat = ""
    count = 0
    for symbol in ukr:
        idx = abetka_k.find(symbol)
        if idx == -1 or symbol == " " or symbol == ",":
            lat += symbol
        elif symbol == "ь" and ukr[count +1] == "о":
            if symbol.islower():
                lat += "j".lower()
            else:
                lat += "j".upper()
        else:
            if symbol == "й" and ukr[count + 1] == "о":
                if prygolosni.find(ukr[count - 1].lower()) != -1:
                    lat += "\'"
            idx = list_k_s.index(symbol)
            if symbol.isupper():
                if ukr.isupper():
                    lat += list_l_s[idx].upper()
                elif count+1 < len(ukr):
                    if ukr[count +1].isupper():
                        lat += list_l_s[idx].upper()
                    else:
                        lat += list_l_s[idx]
                elif count+1 == len(ukr):
                    if ukr[count - 1].isupper():
                        lat += list_l_s[idx].upper()
                    else:
                        lat += list_l_s[idx]
            else:
                lat += list_l_s[idx]
        count += 1
    return lat

if __name__ == '__main__':
    print(replace_forward("""Йоркширський тер'єр йодль койот курйоз
сьогодні
Дяка
Мойот
Ллє
Йод
Кйо
йойк
йойкати
йойкотати
йойкотня
йойлик"""))
