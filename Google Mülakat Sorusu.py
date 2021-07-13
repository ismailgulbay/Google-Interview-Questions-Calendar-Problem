toplanti={
    "ToplantiSaatleri_1" : [["09:00","10:00"],["12:00","14:00"],["14:00","14:30"],["16:00","18:30"]],
    "ToplantiSaatleri_2" : [["08:30","10:15"],["13:00","14:30"],["15:00","17:30"],["18:00","19:30"],["19:30","20:00"]]

}
mesai_saati = {"MesaiSaati_1" : ["07:00","21:00"],
               "MesaiSaati_2" : ["08:00","21:00"]
}

Musait_saatler_1 = []
Musait_saatler_2 = []
ortak_saatler = []
ortak_saatler2 = []
dakika_araligi = []
#Gun icindeki bos saatleri listeye ekleyip döndürür.
def Musait_saat_hesapla(toplanti,mesai,saatler):
    for i in range(len(toplanti)):
        saatler.append([toplanti[i][1],toplanti[i+1][0]]
                             if 0<i and i<(len(toplanti)-1)
                             else [mesai[0],toplanti[i][0]]
                             if i == 0
                             else [toplanti[i][1],mesai[1]])
    saatler.append([toplanti[0][1],toplanti[1][0]]) # i = 0 iken arada bir aralık kayboluyor, onu ekliyoruz.
    for i in range(len(toplanti)): # Müsait zamanlarda başlangıç ve bitiş aynı ise onları ayırmaya yarar.
        if saatler[i][0] == saatler[i][1]:
            saatler.pop(i)
    return sorted(saatler)
# Iki kişinin de gün içinde boş olduğu saatleri kıyaslar.
def Musait_saatleri_karsilastir(musait1,musait2,sure):
    buyuk_olan = max(len(musait1),len(musait2))
    for i in range(buyuk_olan -1):
        for j in range(buyuk_olan):
            if musait1[i][1] >= musait2[j][0] and musait1[i][0] <= musait2[j][1]:
                ortak_saatler.append([max(musait1[i][0],musait2[j][0]),min(musait1[i][1],musait2[j][1])])
    for i in range(len(ortak_saatler)):
        sonuc = (int(ortak_saatler[i][1][0:2]) - int(ortak_saatler[i][0][0:2]))*60 \
                +int(ortak_saatler[i][1][3:]) - int(ortak_saatler[i][0][3:])
        if sonuc != 0 and sonuc >= sure:
            dakika_araligi.append(sonuc)
            ortak_saatler2.append(ortak_saatler[i])
    print(ortak_saatler2)
toplanti_suresi = int(input("Toplanti dakikası giriniz : "))
#Fonksiyona sırasıyla gün içindeki toplantı saatlerini,mesai saatlerini ve ekleyeceğimiz listeyi gönderiyoruz.
Musait_saat_1 = Musait_saat_hesapla(toplanti["ToplantiSaatleri_1"],mesai_saati["MesaiSaati_1"],Musait_saatler_1)
Musait_saat_2 = Musait_saat_hesapla(toplanti["ToplantiSaatleri_2"],mesai_saati["MesaiSaati_2"],Musait_saatler_2)
#Fonksiyona sırasıyla ilk iki kişinin müsait olduğu saatleri ve kullanicidan aldigimiz toplanti süresini gönderiyoruz.
Musait_saatleri_karsilastir(Musait_saat_1,Musait_saat_2,toplanti_suresi)

