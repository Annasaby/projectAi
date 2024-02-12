from checking import Checking
from diseases import Diseases
from suggestion import Suggestion

# Inisialisasi AI Medis
medical_ai = Checking()
diseases_ai = Diseases()
suggestion_ai = Suggestion()

bold_start = '\033[1m'
bold_end = '\033[0m'

# Input data pasien (untuk tes, dapat dimasukkan angka apa saja)
print("Silakan isi form dibawah untuk melakukan Medical Checkup")
print(bold_start +"(pastikan anda sedang dalam  keadaan berpuasa)" + bold_end)
age = int(input("Umur: "))
height = float(input("Tinggi badan (cm): "))
weight = float(input("Berat badan (kg): "))
blood_pressure = int(input("Tekanan darah (mmHg): "))
blood_sugar = int(input("Kadar gula darah: "))
cholesterol = int(input("Kadar kolestrol: "))

# Melakukan pemeriksaan medis menggunakan AI
result = medical_ai.medical_checkup(age, height, weight, blood_pressure, blood_sugar, cholesterol)
health_index = result[0]
weight_status = result[1]
blood_pressure_status = result[2]
blood_sugar_status = result[3]
cholesterol_status = result[4]

# Output hasil pemeriksaan medis
if not health_index:
    print(bold_start + "Anda dalam kondisi ideal!" + bold_end)
else:
    print("===============")
    print(bold_start + "Anda mengalami:" + bold_end)
    for i in health_index:
        print(f"- {i}")
    print( )
    
    print(bold_start + "Risiko penyakit yang mungkin bisa anda alami:" + bold_end)
    diseases_list = diseases_ai.possible_diseases(weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status)
    found = set()
    for i in diseases_list:
        if i in found:
            continue
        print(f"- {i}")
        found.add(i)
    print( )
    
    print(bold_start + "Saran yang bisa saya berikan:" + bold_end)
    suggestion_list = suggestion_ai.suggestion(weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status)
    for i in suggestion_list:
        print(f"* {i}")
    print(bold_start + "Jangan lupa menjaga pola makan dan rutin berolahraga" + bold_end)
    print(bold_start + "Analisis di atas mungkin  masih ada kesalahan \n Saya menganjurkan berkonsultasi dengan dokter untuk evaluasi lebih lanjut." + bold_end)
    
