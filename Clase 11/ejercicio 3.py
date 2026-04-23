def conversion(segundos):
    horas = segundos // 3600
    resto = segundos % 3600
    minutos = resto // 60
    segs = resto % 60

    h = str(horas)
    m = str(minutos)
    s = str(segs)

    if len(h) < 2: h = "0" + h
    if len(m) < 2: m = "0" + m
    if len(s) < 2: s = "0" + s

    return h + ":" + m + ":" + s

print(conversion(3600))   # 01:00:00
print(conversion(1000))   # 00:16:40
