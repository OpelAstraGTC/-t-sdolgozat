halozat = []
with open('hálózat.txt', 'r', encoding='utf-8') as forms, \
     open('hálózat_adat.txt', 'w', encoding='utf-8') as cell:  
    fejlec = forms.readline()
    for sor in forms:
        adat = sor.strip().split(';')
        if len(adat) >= 5:
            h_id = {
                'szero': adat[0],
                'cím': adat[1],
                'kiadas': adat[2],
                'ISBN': adat[3],
                'lapoz': adat[4]
            }
            halozat.append(h_id)
    for h_id in halozat:
        print(h_id, file=cell)
print(halozat)
