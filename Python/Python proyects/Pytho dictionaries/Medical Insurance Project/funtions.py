# Create calculate_insurance_cost() function below: 
def calculate_insurnce_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print('The estimated insurance cost for this person is ' + str(estimated_cost) + ' dollars.')


maria_insurance_cost = calculate_insurnce_cost(28,0,26.2,3,0)

omar_insurance_cost = calculate_insurnce_cost(35,1,22.2,0,1)
