def medical_checkup(height, weight, blood_pressure, blood_sugar, cholesterol):
    # Aturan sederhana berdasarkan data rata-rata penderita penyakit
    diseases = []
    
    # Check tinggi badan dan berat badan
    beratKurang = "berat anda kurang"
    beratLebih = "berat anda berlebih"
    if height > 150 and height <= 155:
        if weight < 45:
            diseases.append(beratKurang)
        elif weight > 58:
            diseases.append(beratLebih)
    elif height > 155 and height <= 160:
        if weight < 49:
            diseases.append(beratKurang)
        elif weight > 63:
            diseases.append(beratLebih)
    elif height > 160 and height <= 165:
        if weight < 53:
            diseases.append(beratKurang)
        elif weight > 68:
            diseases.append(beratLebih)
    elif height > 165 and height <= 170:
        if weight < 57:
            diseases.append(beratKurang)
        elif weight > 73:
            diseases.append(beratLebih)
    elif height > 170 and height <= 175:
        if weight < 61:
            diseases.append(beratKurang)
        elif weight > 78:
            diseases.append(beratLebih)
    elif height > 175 and height <= 180:
        if weight < 65:
            diseases.append(beratKurang)
        elif weight > 83:
            diseases.append(beratLebih)
    elif height > 180 and height <= 185:
        if weight < 70:
            diseases.append(beratKurang)
        elif weight > 88:
            diseases.append(beratLebih)
    elif height > 185 and height <= 190:
        if weight < 74:
            diseases.append(beratKurang)
        elif weight > 93:
            diseases.append(beratLebih)
    

    # Check tekanan darah
    if blood_pressure > 140:
        diseases.append("Tekanan darah tinggi")
    else:
        diseases.append("Tekanan darah tinggi")

    

    # Check kadar gula darah
    if blood_sugar > 120:
        diseases.append("Gula darah tinggi")

    # Check kadar kolestrol
    if cholesterol > 200:
        diseases.append("Kolesterol tinggi")

    return diseases


height = float(input("Tinggi badan (cm): "))
weight = float(input("Berat badan (kg): "))
age = int(input("Umur: "))
blood_pressure = int(input("Tekanan darah: "))
blood_sugar = int(input("Kadar gula darah: "))
cholesterol = int(input("Kadar kolestrol: "))

result = medical_checkup(height, weight, blood_pressure, blood_sugar, cholesterol)

if not result:
    print("Anda dalam kondisi sehat!")
else:
    print("Anda mungkin mengalami:")
    for disease in result:
        print(f"- {disease}")
