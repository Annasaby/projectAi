import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


blood_pressure = ctrl.Antecedent(np.arange(0, 251, 1), 'blood_pressure')
cholesterol = ctrl.Antecedent(np.arange(0, 351, 1), 'cholesterol')
blood_sugar = ctrl.Antecedent(np.arange(0, 251, 1), 'blood_sugar')
stroke_chance = ctrl.Consequent(np.arange(0, 16, 1), 'stroke_chance')



blood_pressure['low'] = fuzz.trimf(blood_pressure.universe, [0, 0, 90])
blood_pressure['normal'] = fuzz.trimf(blood_pressure.universe, [80, 110, 140])
blood_pressure['high'] = fuzz.trimf(blood_pressure.universe, [130, 200, 200])



cholesterol['low'] = fuzz.trimf(cholesterol.universe, [0, 0, 150])
cholesterol['normal'] = fuzz.trimf(cholesterol.universe, [140, 190, 240])
cholesterol['high'] = fuzz.trimf(cholesterol.universe, [230, 300, 300])



blood_sugar['low'] = fuzz.trimf(blood_sugar.universe, [0, 0, 80])
blood_sugar['normal'] = fuzz.trimf(blood_sugar.universe, [70, 90, 110])
blood_sugar['high'] = fuzz.trimf(blood_sugar.universe, [100, 200, 200])



stroke_chance['low'] = fuzz.trimf(stroke_chance.universe, [0, 0, 5])
stroke_chance['medium'] = fuzz.trimf(stroke_chance.universe, [5, 6, 7])
stroke_chance['high'] = fuzz.trimf(stroke_chance.universe, [7, 10, 10])



rule1 = ctrl.Rule(blood_pressure['low'] & cholesterol['low'] & blood_sugar['low'] , stroke_chance['low'])
rule2 = ctrl.Rule(blood_pressure['low'] & cholesterol['low'] & blood_sugar['normal'] , stroke_chance['low'])
rule3 = ctrl.Rule(blood_pressure['low'] & cholesterol['low']& blood_sugar['high'] , stroke_chance['medium'])
rule4 = ctrl.Rule(blood_pressure['low'] & cholesterol['normal']& blood_sugar['low'] , stroke_chance['low'])
rule5 = ctrl.Rule(blood_pressure['low'] & cholesterol['normal']& blood_sugar['normal'] , stroke_chance['low'])
rule6 = ctrl.Rule(blood_pressure['low'] & cholesterol['normal']& blood_sugar['high'] , stroke_chance['medium'])
rule7 = ctrl.Rule(blood_pressure['low'] & cholesterol['high']& blood_sugar['low'] , stroke_chance['medium'])
rule8 = ctrl.Rule(blood_pressure['low'] & cholesterol['high']& blood_sugar['normal'] , stroke_chance['medium'])
rule9 = ctrl.Rule(blood_pressure['low'] & cholesterol['high']& blood_sugar['high'] , stroke_chance['high'])

rule10 = ctrl.Rule(blood_pressure['normal'] & cholesterol['low']& blood_sugar['low'] , stroke_chance['low'])
rule11 = ctrl.Rule(blood_pressure['normal'] & cholesterol['low']& blood_sugar['normal'] , stroke_chance['low'])
rule12 = ctrl.Rule(blood_pressure['normal'] & cholesterol['low']& blood_sugar['high'] , stroke_chance['medium'])
rule13 = ctrl.Rule(blood_pressure['normal'] & cholesterol['normal']& blood_sugar['low'] , stroke_chance['low'])
rule14 = ctrl.Rule(blood_pressure['normal'] & cholesterol['normal']& blood_sugar['normal'] , stroke_chance['low'])
rule15 = ctrl.Rule(blood_pressure['normal'] & cholesterol['normal']& blood_sugar['high'] , stroke_chance['medium'])
rule16 = ctrl.Rule(blood_pressure['normal'] & cholesterol['high']& blood_sugar['low'] , stroke_chance['medium'])
rule17 = ctrl.Rule(blood_pressure['normal'] & cholesterol['high']& blood_sugar['normal'] , stroke_chance['medium'])
rule18 = ctrl.Rule(blood_pressure['normal'] & cholesterol['high']& blood_sugar['high'] , stroke_chance['high'])

rule19 = ctrl.Rule(blood_pressure['high'] & cholesterol['low']& blood_sugar['low'] , stroke_chance['medium'])
rule20 = ctrl.Rule(blood_pressure['high'] & cholesterol['low']& blood_sugar['normal'] , stroke_chance['medium'])
rule21 = ctrl.Rule(blood_pressure['high'] & cholesterol['low']& blood_sugar['high'] , stroke_chance['high'])
rule22 = ctrl.Rule(blood_pressure['high'] & cholesterol['normal']& blood_sugar['low'] , stroke_chance['medium'])
rule23 = ctrl.Rule(blood_pressure['high'] & cholesterol['normal']& blood_sugar['normal'] , stroke_chance['medium'])
rule24 = ctrl.Rule(blood_pressure['high'] & cholesterol['normal']& blood_sugar['high'] , stroke_chance['high'])
rule25 = ctrl.Rule(blood_pressure['high'] & cholesterol['high']& blood_sugar['low'] , stroke_chance['high'])
rule26 = ctrl.Rule(blood_pressure['high'] & cholesterol['high']& blood_sugar['normal'] , stroke_chance['high'])
rule27 = ctrl.Rule(blood_pressure['high'] & cholesterol['high']& blood_sugar['high'] , stroke_chance['high'])



checking_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])



def stroke_checking(blood_pressure, cholesterol, blood_sugar):
    checking = ctrl.ControlSystemSimulation(checking_ctrl)
    checking.input['blood_pressure'] = blood_pressure
    checking.input['cholesterol'] = cholesterol
    checking.input['blood_sugar'] = blood_sugar
    checking.compute()
    
    stroke_chance.view(sim=checking)
    
    return checking.output['stroke_chance']

    
    