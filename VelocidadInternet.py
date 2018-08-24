

x = "si"
while (x == "si"):
    VelSubida = float(input("Cual es tu velocidad de subida en megabits? "))
    Conversion = (VelSubida * 1000000)
    Pregunta = str(input("Tu archivo se mide en Petabytes, Terabytes, Gigabytes, Megabytes o Kilobytes?"))

    if Pregunta == "Petabytes":
        Peta = int(input("Cuanto pesa tu archivo?"))
        TamPeta = (Peta * 8000000000000000)
        DivisionPeta = (TamPeta / Conversion)

        respuesta = "Tu archivo tarda "
        print(respuesta + str(DivisionPeta))
        # Conversiones
        SegaMinutosPeta = float(input("Quieres convertirlo a minutos? 1=si 2=no "))
        DivisionPeta2 = (DivisionPeta / 60)
        if SegaMinutosPeta == 1:
            print(respuesta + str(DivisionPeta2))

        MinsaHorasPeta = float(input("Quieres convertirlo a horas? 1=si 2=no "))
        DivisionPeta3 = (DivisionPeta2 / 60)
        if MinsaHorasPeta == 1:
            print(respuesta + str(DivisionPeta3))

        HorasaDiasPeta = float(input("Quieres convertirlo a dias? 1=si 2-no"))
        DivisionPeta4 = (DivisionPeta3 / 24)
        if HorasaDiasPeta == 1:
            print(respuesta + str(DivisionPeta4))

        DiasaanosPeta = int(input("Quieres convertirlo a años? 1=si 2-no"))
        DivisionPeta5 = (DivisionPeta4 / 365)
        if DiasaanosPeta == 1:
            print(respuesta + str(DivisionPeta5))

    elif Pregunta == "Terabytes":
        Tera = float(input("Cuanto pesa tu archivo?"))
        TamTera = (Tera * 8000000000000)
        DivisionTera = (TamTera / Conversion)

        respuesta = "Tu archivo tarda "
        print(respuesta + str(DivisionTera))
        # Conversiones
        SegaMinutosTera = float(input("Quieres convertirlo a minutos? 1=si 2=no "))
        DivisionTera2 = (DivisionTera / 60)
        if SegaMinutosTera == 1:
            print(respuesta + str(DivisionTera2))

        MinsaHorasTera = float(input("Quieres convertirlo a horas? 1=si 2=no "))
        DivisionTera3 = (DivisionTera2 / 60)
        if MinsaHorasTera == 1:
            print(respuesta + str(DivisionTera3))

        HorasaDiasTera = float(input("Quieres convertirlo a dias? 1=si 2-no"))
        DivisionTera4 = (DivisionTera3 / 24)
        if HorasaDiasTera == 1:
            print(respuesta + str(DivisionTera4))

        DiasaanosTera = int(input("Quieres convertirlo a años? 1=si 2-no"))
        DivisionTera5 = (DivisionTera4 / 365)
        if DiasaanosTera == 1:
            print(respuesta + str(DivisionTera5))

    elif Pregunta == "Gigabytes":
        Giga = float(input("Cuanto pesa tu archivo?"))
        TamGiga = (Giga * 8000000000)
        DivisionGiga = (TamGiga / Conversion)

        respuesta = "Tu archivo tarda "
        print(respuesta + str(DivisionGiga) + " segundos")
        # Conversiones
        SegaMinutosGiga = float(input("Quieres convertirlo a minutos? 1=si 2=no "))
        DivisionGiga2 = (DivisionGiga / 60)
        if SegaMinutosGiga == 1:
            print(respuesta + str(DivisionGiga2))

        MinsaHorasGiga = float(input("Quieres convertirlo a horas? 1=si 2=no "))
        DivisionGiga3 = (DivisionGiga2 / 60)
        if MinsaHorasGiga == 1:
            print(respuesta + str(DivisionGiga3))

        HorasaDiasGiga = float(input("Quieres convertirlo a dias? 1=si 2-no"))
        DivisionGiga4 = (DivisionGiga3 / 24)
        if HorasaDiasGiga == 1:
            print(respuesta + str(DivisionGiga4))

        DiasaanosGiga = int(input("Quieres convertirlo a años? 1=si 2-no"))
        DivisionGiga5 = (DivisionGiga4 / 365)
        if DiasaanosGiga == 1:
            print(respuesta + str(DivisionGiga5))

    elif Pregunta == "Megabytes":
        Mega = float(input("Cuanto pesa tu archivo?"))
        TamMega = (Mega * 8000000)
        DivisionMega = (TamMega / Conversion)

        respuesta = "Tu archivo tarda "
        print(respuesta + str(DivisionMega))
        # Conversiones
        SegaMinutosMega = float(input("Quieres convertirlo a minutos? 1=si 2=no "))
        DivisionMega2 = (DivisionMega / 60)
        if SegaMinutosMega == 1:
            print(respuesta + str(DivisionMega2))

        MinsaHorasMega = float(input("Quieres convertirlo a horas? 1=si 2=no "))
        DivisionMega3 = (DivisionMega2 / 60)
        if MinsaHorasMega == 1:
            print(respuesta + str(DivisionMega3))

        HorasaDiasMega = float(input("Quieres convertirlo a dias? 1=si 2-no"))
        DivisionMega4 = (DivisionMega3 / 24)
        if HorasaDiasMega == 1:
            print(respuesta + str(DivisionMega4))

        DiasaanosMega = int(input("Quieres convertirlo a años? 1=si 2-no"))
        DivisionMega5 = (DivisionMega4 / 365)
        if DiasaanosMega == 1:
            print(respuesta + str(DivisionMega5))

    elif Pregunta == "Kilobytes":
        Kilo = float(input("Cuanto pesa tu archivo?"))
        TamKilo = (Kilo * 8000)
        DivisionKilo = (TamKilo / Conversion)

        respuesta = "Tu archivo tarda "
        print(respuesta + str(DivisionKilo))
        # Conversiones
        SegaMinutosKilo = float(input("Quieres convertirlo a minutos? 1=si 2=no "))
        DivisionKilo2 = (DivisionKilo / 60)
        if SegaMinutosKilo == 1:
            print(respuesta + str(DivisionKilo2))

        MinsaHorasKilo = float(input("Quieres convertirlo a horas? 1=si 2=no "))
        DivisionKilo3 = (DivisionKilo2 / 60)
        if MinsaHorasKilo == 1:
            print(respuesta + str(DivisionKilo3))

        HorasaDiasKilo = float(input("Quieres convertirlo a dias? 1=si 2-no"))
        DivisionKilo4 = (DivisionKilo3 / 24)
        if HorasaDiasKilo == 1:
            print(respuesta + str(DivisionKilo4))

        DiasaanosKilo = int(input("Quieres convertirlo a años? 1=si 2-no"))
        DivisionKilo5 = (DivisionKilo4 / 365)
        if DiasaanosKilo == 1:
            print(respuesta + str(DivisionKilo5))
    x = input("quieres hacer otra conversion?")







