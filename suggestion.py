class Suggestion:
    def suggestion(self, weight_status, blood_pressure_status, blood_sugar_status, cholesterol_status):
        suggestions = []
        if weight_status == "high":
            suggestions.append("Kurangi asupan kalori harian.")
        elif weight_status == "low":
            suggestions.append("Konsumsi makanan yang kaya akan nutrisi serta latihan fisik.")

        if blood_pressure_status == "high":
            suggestions.append("Kurangi konsumsi garam dan makanan tinggi lemak.")
            suggestions.append("Kurangin aktifitas yang berat")
        elif blood_pressure_status == "low":
            suggestions.append("Konsumsi lebih banyak cairan dan garam.")

        if blood_sugar_status == "high":
            suggestions.append("Kurangi konsumsi makanan manis dan karbohidrat sederhana.")
        elif blood_sugar_status == "low":
            suggestions.append("Konsumsi makanan kaya karbohidrat kompleks dan lakukan pemantauan kadar gula darah secara rutin.")

        if cholesterol_status == "high":
            suggestions.append("Kurangi konsumsi makanan berlemak jenuh dan trans, serta tingkatkan asupan serat makanan.")

        return suggestions