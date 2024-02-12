class Checking:
    def __init__(self):
        self.health_index = []
        self.weight_status = "normal"
        self.blood_pressure_status = "normal"
        self.blood_sugar_status = "normal"
        self.cholesterol_status = "normal"

    def check_weight(self, height, weight):
        #memeriksa berat badan
        self.height = height / 100
        bmi = weight / (self.height * self.height)
        
        if bmi < 18:
            self.weight_status = "low"
            self.health_index.append("Kekurangan berat badan")
        elif bmi >= 23:
            self.weight_status = "high"
            self.health_index.append("Kelebihan berat badan")

        #memeriksa tekanan darah
    def check_blood_pressure(self, blood_pressure):
        if blood_pressure > 140:
            self.blood_pressure_status = "high"
            self.health_index.append("Tekanan darah sangat tinggi")
        elif blood_pressure > 90 and blood_pressure < 120:
            self.blood_pressure_status = "high"
            self.health_index.append("Tekanan darah tinggi")
        elif blood_pressure < 90:
            self.blood_pressure_status = "low"
            self.health_index.append("Tekanan darah rendah")

        #memeriksa kadar gula darah
    def check_blood_sugar(self, blood_sugar):
        if blood_sugar > 110:
            self.blood_sugar_status = "high"
            self.health_index.append("Kadar Gula darah tinggi")
        elif blood_sugar < 70:
            self.blood_sugar_status = "low"
            self.health_index.append("Kadar Gula darah rendah")

        #memeriksa kadar kolesterol
    def check_cholesterol(self, cholesterol):
        if cholesterol >= 200 and cholesterol < 240:
            self.cholesterol_status = "high"
            self.health_index.append("Kolesterol tinggi")
        elif cholesterol >= 240:
            self.cholesterol_status = "high"
            self.health_index.append("Kolesterol sangat tinggi")
        

    def medical_checkup(self, age, height, weight, blood_pressure, blood_sugar, cholesterol):
        self.check_weight(height, weight)
        self.check_blood_pressure(blood_pressure)
        self.check_blood_sugar(blood_sugar)
        self.check_cholesterol(cholesterol)
        return self.health_index, self.weight_status, self.blood_pressure_status, self.blood_sugar_status, self.cholesterol_status

    

    