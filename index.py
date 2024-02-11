def medical_checkup(age, height, weight, blood_pressure, blood_sugar, cholesterol):
    # Aturan sederhana berdasarkan data rata-rata penderita penyakit
    diseases = []
    
    # Check tinggi badan dan berat badan
    beratKurang = "berat anda kurang"
    beratLebih = "berat anda berlebih"
    berat = "normal"
    td = "normal"
    gd = "normal"
    kl = "normal"
    if height > 150 and height <= 155:
        if weight < 45:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 58:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 155 and height <= 160:
        if weight < 49:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 63:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 160 and height <= 165:
        if weight < 53:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 68:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 165 and height <= 170:
        if weight < 57:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 73:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 170 and height <= 175:
        if weight < 61:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 78:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 175 and height <= 180:
        if weight < 65:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 83:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 180 and height <= 185:
        if weight < 70:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 88:
            berat = "l"
            diseases.append(beratLebih)
    elif height > 185 and height <= 190:
        if weight < 74:
            berat = "k"
            diseases.append(beratKurang)
        elif weight > 93:
            berat = "l"
            diseases.append(beratLebih)
    

    # Check tekanan darah
    if (blood_pressure > 140):
        td = "l"
        diseases.append("Tekanan darah tinggi")
    elif ( blood_pressure < 90):
        td = "k"
        diseases.append("Tekanan darah rendah")
        
        
    # Check kadar gula darah
    if (blood_sugar) > 100:
        gd = "l"
        diseases.append("Gula darah tinggi")
    elif (blood_sugar < 70):
        gd = "k"
        diseases.append("Gula darah rendah")
        

    # Check kadar kolestrol
    if (cholesterol >= 200 and cholesterol < 240):
        kl = "l"
        diseases.append("Kolesterol anda tinggi")
    elif (cholesterol >= 240 ):
        kl = "l"
        diseases.append("Kolesterol anda sangat tinggi")
    elif ( cholesterol < 50 ):
        diseases.append("Kolestrol anda sangat rendah")
        
        

    return diseases, berat, td, gd, kl

def kemungkinan_penyakit(r1,r2,r3,r4):
    
    if ( r1 == "l"):
        print("obesitas")
    elif( r1 == "k"):
        print("cungkring")
    
    if ( r2 == "l"):
        print("hipertensi")
    elif ( r2 == "k"):
        print("hipotensi")
        
    if ( r3 == "l"):
        print("diabetes")
    elif ( r3 == "k"):
        print("hipoglikemia")
        
    if ( r4 == "l"):
        print("jantung koroner")
    

height = float(input("Tinggi badan (cm): "))
weight = float(input("Berat badan (kg): "))
age = int(input("Umur: "))
blood_pressure = int(input("Tekanan darah: "))
blood_sugar = int(input("Kadar gula darah (pastikan anda sedang berpuasa): "))
cholesterol = int(input("Kadar kolestrol: "))

result = medical_checkup(age, height, weight, blood_pressure, blood_sugar, cholesterol)
r1 = result[1]
r2 = result[2]
r3 = result[3]
r4 = result[4]


if not result[0]:
    print("Anda dalam kondisi ideal!")
else:
    print("Anda mengalami:")
    for disease in result[0]:
        print(f"- {disease}")
        
print("penyakit yang mungkin bisa anda alami :")
print(kemungkinan_penyakit(r1,r2,r3,r4))

# if (age > 40 and blood_pressure > 140):
#     diseases.append("anda mengalami hipertensi tahap 1")