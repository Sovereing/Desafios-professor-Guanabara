valor = float(input("Digite sua medida em metros: "))

km = valor/1000
hm = valor/100
dam = valor/10
dm = valor*10
cm = valor*100
mm = valor*1000

print('A medida {} corresponde a {}km {}hm {}dam {}dm {:.04f}cm {:.0f}mm'.format(valor, km, hm, dam, dm, cm, mm))
