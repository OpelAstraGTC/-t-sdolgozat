álózat = []
with open('hálózat.txt', 'r', encoding='utf-8') as forms, \
     open('hálózat_adat.txt', 'w', encoding='utf-8') as cell:  
    fejléc = forms.readline()
    for sor in forms:
        adat = sor.strip().split(';')
        if len(adat) >= 5:
            h_id = {
                'szero': adat[0],
                'cím': adat[1],
                'kiadás': adat[2],
                'ISBN': adat[3],
                'lapoz': adat[4]
            }
            hálózat.append(h_id)
    for h_id in hálózat:
        print(h_id, file=cell)
print(hálózat)
