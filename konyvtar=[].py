konyvtar=[]
with open('konyvtar.txt','r',encoding='utf-8') as forras, \
    open('konyvtar_adat.txt','w',encoding='utf-8') as cel:
    fejlec=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        konyv={'szrzo': adat[0], 'cm':adat[1],'kiads':adat[2],'ISBN':adat[3],'allapot':adat[4],}
        konyvtar.append(konyv)
        print(konyv,file=cel)
print(f'{konyvtar}')