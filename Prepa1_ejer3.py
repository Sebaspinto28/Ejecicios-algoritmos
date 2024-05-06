dia=int(input(" escriba el dia:"))
mes=int(input(" escriba el mes:"))
a=int(input(" escriba el año:"))
linea_mes=""
esvalido = True
if mes==1:
    esvalido=dia<=31
    linea_mes="enero"
elif mes==2:
    esvalido=dia<=28
    linea_mes="febrero"
elif mes==3:
    esvalido=dia<=31
    linea_mes="marzo"
elif mes==4:
    esvalido=dia<=30
    linea_mes="abril"
elif mes==5:
    esvalido=dia<=31
    linea_mes="mayo"
elif mes==6:
    esvalido=dia<=30
    linea_mes="junio"
elif mes==7:
    esvalido=dia<=31
    linea_mes="julio"
elif mes==8:
    esvalido=dia<=31
    linea_mes="agosto"
elif mes==9:
    esvalido=dia<=30
    linea_mes="septiembre"
elif mes==10:
    esvalido=dia<=31
    linea_mes="octubre"
elif mes==11:
    esvalido=dia<=30
    linea_mes="noviembre"
elif mes==12:
    esvalido=dia<=31
    linea_mes="diciembre"

else:
    esvalido=False

if a<0 or a>2024:
    esvalido=False


if esvalido:
    print(f"{dia} de {linea_mes} del {a}")
else:
    print("fecha invalida")
