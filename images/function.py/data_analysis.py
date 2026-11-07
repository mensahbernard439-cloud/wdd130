# Life expectancy data analysis script
# Finds overall extremes and user-specified year statistics.

lowest_life = 999.0
lowest_country = ""
lowest_year = ""

highest_life = 0.0
highest_country = ""
highest_year = ""

filename = "life-expectancy.csv"

# 1. Read file and find overall min and max
with open(filename, "r") as f:
    next(f) # skip header
    
    for line in f:
        parts = line.strip().split(",")
        
        country = parts[0]
        year = parts[2]
        life_exp = float(parts[3])
        
        if life_exp < lowest_life:
            lowest_life = life_exp
            lowest_country = country
            lowest_year = year
            
        if life_exp > highest_life:
            highest_life = life_exp
            highest_country = country
            highest_year = year

print("Overall Max Life Expectancy:", highest_life, "in", highest_country, f"({highest_year})")
print("Overall Min Life Expectancy:", lowest_life, "in", lowest_country, f"({lowest_year})")
print("-" * 50)

# 2. Ask user for a year
target_year = input("Enter the year of interest: ")

total_life = 0
count = 0
year_min = 999.0
year_min_country = ""
year_max = 0.0
year_max_country = ""

# 3. Re-open file to calculate stats for that specific year
with open(filename, "r") as f:
    next(f)
    
    for line in f:
        parts = line.strip().split(",")
        country = parts[0]
        year = parts[2]
        life_exp = float(parts[3])
        
        if year == target_year:
            total_life += life_exp
            count += 1
            
            if life_exp < year_min:
                year_min = life_exp
                year_min_country = country
                
            if life_exp > year_max:
                year_max = life_exp
                year_max_country = country

# Display results
if count > 0:
    avg_life = total_life / count
    print(f"\nStatistics for {target_year}:")
    print(f"Average life expectancy: {avg_life:.2f}")
    print(f"Lowest life expectancy: {year_min} in {year_min_country}")
    print(f"Highest life expectancy: {year_max} in {year_max_country}")
else:
    print(f"\nNo data found for the year {target_year}.")