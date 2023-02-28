# Using a formula that estimates a person’s yearly insurance costs, we will investigate how different factors such as age, sex, BMI, etc. affect the prediction.
# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below

insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print(''' This person's inurance cost is ''' + str(insurance_cost)+ ' dollars')

# Age Factor


# BMI Factor


# Male vs. Female Factor


# Extra Practice