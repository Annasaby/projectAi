import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


idx_bmi = ctrl.Antecedent(np.arange(0, 30, 1), 'idx_bmi')
cholestrol = ctrl.Antecedent(np.arange(0, 301, 1), 'cholestrol')
blood_sugar = ctrl.Antecedent(np.arange(0, 251, 1), 'blood_sugar')
diabetes_change = ctrl.Consequent(np.arange(0, 16, 1), 'diabetes_change')



idx_bmi['low'] = fuzz.trimf(idx_bmi.universe, [0, 0, 18])
idx_bmi['normal'] = fuzz.trimf(idx_bmi.universe, [16, 20.5 , 25])
idx_bmi['high'] = fuzz.trimf(idx_bmi.universe, [24, 30, 30])



cholestrol['low'] = fuzz.trimf(cholestrol.universe, [0, 0, 150])
cholestrol['normal'] = fuzz.trimf(cholestrol.universe, [140, 190, 240])
cholestrol['high'] = fuzz.trimf(cholestrol.universe, [230, 300, 300])



blood_sugar['low'] = fuzz.trimf(blood_sugar.universe, [0, 0, 80])
blood_sugar['normal'] = fuzz.trimf(blood_sugar.universe, [70, 90, 110])
blood_sugar['high'] = fuzz.trimf(blood_sugar.universe, [100, 200, 200])



diabetes_change['low'] = fuzz.trimf(diabetes_change.universe, [0, 0, 5])
diabetes_change['medium'] = fuzz.trimf(diabetes_change.universe, [5, 6, 7])
diabetes_change['high'] = fuzz.trimf(diabetes_change.universe, [7, 10, 10])



rule1 = ctrl.Rule(idx_bmi['low'] & cholestrol['low'] & blood_sugar['low'] , diabetes_change['low'])
rule2 = ctrl.Rule(idx_bmi['low'] & cholestrol['low'] & blood_sugar['normal'] , diabetes_change['low'])
rule3 = ctrl.Rule(idx_bmi['low'] & cholestrol['low']& blood_sugar['high'] , diabetes_change['medium'])
rule4 = ctrl.Rule(idx_bmi['low'] & cholestrol['normal']& blood_sugar['low'] , diabetes_change['low'])
rule5 = ctrl.Rule(idx_bmi['low'] & cholestrol['normal']& blood_sugar['normal'] , diabetes_change['low'])
rule6 = ctrl.Rule(idx_bmi['low'] & cholestrol['normal']& blood_sugar['high'] , diabetes_change['medium'])
rule7 = ctrl.Rule(idx_bmi['low'] & cholestrol['high']& blood_sugar['low'] , diabetes_change['medium'])
rule8 = ctrl.Rule(idx_bmi['low'] & cholestrol['high']& blood_sugar['normal'] , diabetes_change['medium'])
rule9 = ctrl.Rule(idx_bmi['low'] & cholestrol['high']& blood_sugar['high'] , diabetes_change['high'])

rule10 = ctrl.Rule(idx_bmi['normal'] & cholestrol['low']& blood_sugar['low'] , diabetes_change['low'])
rule11 = ctrl.Rule(idx_bmi['normal'] & cholestrol['low']& blood_sugar['normal'] , diabetes_change['low'])
rule12 = ctrl.Rule(idx_bmi['normal'] & cholestrol['low']& blood_sugar['high'] , diabetes_change['medium'])
rule13 = ctrl.Rule(idx_bmi['normal'] & cholestrol['normal']& blood_sugar['low'] , diabetes_change['low'])
rule14 = ctrl.Rule(idx_bmi['normal'] & cholestrol['normal']& blood_sugar['normal'] , diabetes_change['low'])
rule15 = ctrl.Rule(idx_bmi['normal'] & cholestrol['normal']& blood_sugar['high'] , diabetes_change['medium'])
rule16 = ctrl.Rule(idx_bmi['normal'] & cholestrol['high']& blood_sugar['low'] , diabetes_change['medium'])
rule17 = ctrl.Rule(idx_bmi['normal'] & cholestrol['high']& blood_sugar['normal'] , diabetes_change['medium'])
rule18 = ctrl.Rule(idx_bmi['normal'] & cholestrol['high']& blood_sugar['high'] , diabetes_change['high'])

rule19 = ctrl.Rule(idx_bmi['high'] & cholestrol['low']& blood_sugar['low'] , diabetes_change['medium'])
rule20 = ctrl.Rule(idx_bmi['high'] & cholestrol['low']& blood_sugar['normal'] , diabetes_change['medium'])
rule21 = ctrl.Rule(idx_bmi['high'] & cholestrol['low']& blood_sugar['high'] , diabetes_change['high'])
rule22 = ctrl.Rule(idx_bmi['high'] & cholestrol['normal']& blood_sugar['low'] , diabetes_change['medium'])
rule23 = ctrl.Rule(idx_bmi['high'] & cholestrol['normal']& blood_sugar['normal'] , diabetes_change['medium'])
rule24 = ctrl.Rule(idx_bmi['high'] & cholestrol['normal']& blood_sugar['high'] , diabetes_change['high'])
rule25 = ctrl.Rule(idx_bmi['high'] & cholestrol['high']& blood_sugar['low'] , diabetes_change['high'])
rule26 = ctrl.Rule(idx_bmi['high'] & cholestrol['high']& blood_sugar['normal'] , diabetes_change['high'])
rule27 = ctrl.Rule(idx_bmi['high'] & cholestrol['high']& blood_sugar['high'] , diabetes_change['high'])



checking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])



def diabetes_checking(idx_bmi, cholesterol, blood_sugar):
    checking = ctrl.ControlSystemSimulation(checking_ctrl)
    checking.input['idx_bmi'] = idx_bmi
    checking.input['cholestrol'] = cholesterol
    checking.input['blood_sugar'] = blood_sugar
    checking.compute()

    diabetes_change.view(sim=checking)
    
    return checking.output['diabetes_change']