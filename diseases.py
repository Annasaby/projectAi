class Diseases:
    
    def possible_diseases(self, weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status):
            diseases = []
            if weight_status == "high":
                diseases.append("Obesitas")
            elif weight_status == "low":
                diseases.append("Malnutrisi")

            if blood_pressure_status == "high":
                diseases.append("Hipertensi")
                diseases.append("Kardio vaskuler")
                diseases.append("Jantung koroner")
            elif blood_pressure_status == "low":
                diseases.append("Hipotensi")
                diseases.append("Jantung koroner")

            if blood_sugar_status == "high":
                diseases.append("Diabetes")
                diseases.append("Obesitas")
            elif blood_sugar_status == "low":
                diseases.append("Hipoglikemia")

            if cholesterol_status == "high":
                diseases.append("jantung koroner")
            

            return diseases