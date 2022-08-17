hora = int(input("sigite a hora atual"))
minutos = int(input("digite os minutos atuais"))
segundos = int(input("digite os segundos atuais"))

minutosseg = minutos*60
horamin = minutosseg*60
horaseg = minutosseg*horamin
totalseg = segundos + minutosseg + horaseg
totalmin = horamin + minutos

print("Foram decorridos: " + str(totalmin) + " minutos hoje" )
print("Foram decorridos: " + str(totalseg) + " segundos hoje")
