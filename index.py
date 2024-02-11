def medical_checkup(age, height, weight, blood_pressure, blood_sugar, cholesterol):
    # Aturan sederhana berdasarkan data rata-rata penderita penyakit
    health_index = []
    
    beratKurang = "Kekurangan berat badan"
    beratLebih = "Kelebihan berat badan"
    weight_status = "normal"
    blood_pressure_status = "normal"
    blood_sugar_status = "normal"
    cholesterol_status = "normal"
    if height < 150:
        if weight < 32:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 45:
            weight_status = "l"
            health_index.append(beratLebih)
    if height > 150 and height <= 155:
        if weight < 45:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 58:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 155 and height <= 160:
        if weight < 49:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 63:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 160 and height <= 165:
        if weight < 53:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 68:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 165 and height <= 170:
        if weight < 57:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 73:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 170 and height <= 175:
        if weight < 61:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 78:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 175 and height <= 180:
        if weight < 65:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 83:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 180 and height <= 185:
        if weight < 70:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 88:
            weight_status = "l"
            health_index.append(beratLebih)
    elif height > 185 and height <= 190:
        if weight < 74:
            weight_status = "k"
            health_index.append(beratKurang)
        elif weight > 93:
            weight_status = "l"
            health_index.append(beratLebih)

    

    # Check tekanan darah
    if blood_pressure > 140:
        blood_pressure_status = "l"
        health_index.append("Tekanan darah tinggi")
    elif blood_pressure < 90:
        blood_pressure_status = "k"
        health_index.append("Tekanan darah rendah")
        
        
    # Check kadar gula darah
    if blood_sugar > 100:
        blood_sugar_status = "l"
        health_index.append("Gula darah tinggi")
    elif blood_sugar < 70:
        blood_sugar_status = "k"
        health_index.append("Gula darah rendah")
        

    # Check kadar kolestrol
    if cholesterol >= 200 and cholesterol < 240:
        cholesterol_status = "l"
        health_index.append("Kolesterol anda tinggi")
    elif cholesterol >= 240:
        cholesterol_status = "l"
        health_index.append("Kolesterol anda sangat tinggi")
    elif cholesterol < 50:
        health_index.append("Kolestrol anda sangat rendah")
        
        

    return health_index, weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status

def possible_diseases(weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status):
    diseases = []
    if weight_status == "l":
        diseases.append("obesitas")
    elif weight_status == "k":
        diseases.append("cungkring")

    if blood_pressure_status == "l":
        diseases.append("hipertensi")
    elif blood_pressure_status == "k":
        diseases.append("hipotensi")

    if blood_sugar_status == "l":
        diseases.append("diabetes")
    elif blood_sugar_status == "k":
        diseases.append("hipoglikemia")

    if cholesterol_status == "l":
        diseases.append("jantung koroner")

    return diseases

def suggestion(weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status):
    suggestion = []
    if weight_status == "l":
        suggestion.append("kurang-kurangin makan")
    elif weight_status == "k":
        suggestion.append("banyakain makan")

    if blood_pressure_status == "l":
        suggestion.append("jangan kebanyakan makan kambing")
    elif blood_pressure_status == "k":
        suggestion.append("banyakin makan kambing")

    if blood_sugar_status == "l":
        suggestion.append("kurangin makan minum manis")
    elif blood_sugar_status == "k":
        suggestion.append("makan gula?")

    if cholesterol_status == "l":
        suggestion.append("makan rebusan aee")

    return suggestion

age = int(input("Umur: "))
height = float(input("Tinggi badan (cm): "))
weight = float(input("Berat badan (kg): "))
blood_pressure = int(input("Tekanan darah: "))
blood_sugar = int(input("Kadar gula darah (pastikan anda sedang berpuasa): "))
cholesterol = int(input("Kadar kolestrol: "))

result = medical_checkup(age, height, weight, blood_pressure, blood_sugar, cholesterol)
health_index = result[0]
weight_status = result[1]
blood_pressure_status = result[2]
blood_sugar_status = result[3]
cholesterol_status = result[4]
bold_start = '\033[1m'
bold_end = '\033[0m'

if not health_index:
    print(bold_start + "Anda dalam kondisi ideal!" + bold_end)
else:
    print("===============")
    print(bold_start + "Anda mengalami:" + bold_end)
    for index in health_index:
        print(f"- {index}")
    print( )
    
    print(bold_start + "Penyakit yang mungkin bisa anda alami:" + bold_end)
    diseases_list = possible_diseases(weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status)
    for disease in diseases_list:
        print(f"- {disease}")
    print( )
    
    print("Saran yang bisa saya berikan", end=" ")
    suggestion_list = suggestion(weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status)
    for i in suggestion_list:
        print(f"{i}", end=", ")
    print( )
    print("serta jangan lupa olahraga dan minum air putih >_< \n")
