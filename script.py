# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_damages(damages, conversion):
  results = []
  for damage in damages:
    for conv in conversion:
      if conv in damage:
        results.append(float(damage[:-1])*conversion[conv])
      else:
        results.append("Damages not recorded")
  return results
# test function by updating damages
updated_damages = convert_damages(damages, conversion)


# 2 
# Create a Table
def create_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  for i in range(0,len(names)):
     hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes
# 3
# Organizing by Year
hurricanes = create_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)
# create a new dictionary of hurricanes with year and key
def create_year_dictionary(hurricanes):
    hurricanes_by_year = {}
    for current_cane in hurricanes.values():
        current_year = current_cane['Year']
        if current_year not in hurricanes_by_year:
            year_list = []
            for current_cane in hurricanes.values():
                if current_cane['Year'] == current_year:
                    year_list.append(current_cane)
            hurricanes_by_year[current_year] = year_list
    return hurricanes_by_year

hurricanes_by_year = create_year_dictionary(hurricanes)
#print(hurricanes_by_year[1932])
# 4

# Counting Damaged Areas
def count_areas_affected(hurricanes):
  list_areas = []
  for hurricane in hurricanes.values():
    for area in hurricane["Areas Affected"]:
      if area not in list_areas:
        list_areas.append(area)
  return len(list_areas)      

num_areas_affected = count_areas_affected(hurricanes)
#print(num_areas_affected)


# create dictionary of areas to store the number of hurricanes involved in
# 5 
# Calculating Maximum Hurricane Count
def count_area_affected(hurricanes):
  dict_areas = {}
  counter = 0
  for hurricane in hurricanes.values():
    for area in hurricane["Areas Affected"]:
      if area not in dict_areas.keys():
        dict_areas[area] = 1
      else:
        dict_areas[area] += 1      
  return dict_areas
    
# find most frequently affected area and the number of hurricanes involved in
dict_affected_areas = count_area_affected(hurricanes)

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  max_mortality_cane = ""
  max_mortality = 0
  for cane in hurricanes:
    mort = hurricanes[cane]["Deaths"]
    if(mort > max_mortality):
      max_mortality = mort
      max_mortality_cane = cane
  return (max_mortality_cane, max_mortality)
    
    
# find highest mortality hurricane and the number of deaths
highest_mort = deadliest_hurricane(hurricanes)
print(highest_mort)
# 7
# Rating Hurricanes by Mortality
def rate_by_mortality(hurricanes):
  mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes.keys():
    if hurricanes[hurricane]["Deaths"] == 0:
      mortality[0].append(hurricane)
    elif hurricanes[hurricane]["Deaths"]<100:
      mortality[1].append(hurricane)
    elif hurricanes[hurricane]["Deaths"]<500:
      mortality[2].append(hurricane)
    elif hurricanes[hurricane]["Deaths"]<1000:
      mortality[3].append(hurricane)
    elif hurricanes[hurricane]["Deaths"]<10000:
      mortality[4].append(hurricane)
    else:
      mortality[5].append(hurricane)
  
  return mortality

# categorize hurricanes in new dictionary with mortality severity as key
#print(rate_by_mortality(hurricanes))

# 8 Calculating Hurricane Maximum Damage
def max_damage(hurricanes):
  max_damage_cane = ""
  max_damage = 0
  for cane in hurricanes:
    damage = hurricanes[cane]["Damage"]
    if(not isinstance(damage,str)):
      if max_damage < damage:
        max_damage = damage
        max_damage_cane = cane
 
  return (max_damage_cane, max_damage)
# find highest damage inducing hurricane and its total cost
print(max_damage(hurricanes))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def rate_by_damage(hurricanes,damage_scale):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes.keys():
    if not isinstance(hurricanes[hurricane]["Damage"], str):
      if hurricanes[hurricane]["Damage"] == damage_scale[0]:
        hurricanes_by_damage[0].append(hurricane)
      elif hurricanes[hurricane]["Damage"] < damage_scale[1]:
        hurricanes_by_damage[1].append(hurricane)
      elif hurricanes[hurricane]["Damage"] < damage_scale[2]:
        hurricanes_by_damage[2].append(hurricane)
      elif hurricanes[hurricane]["Damage"] < damage_scale[3]:
        hurricanes_by_damage[3].append(hurricane)
      elif hurricanes[hurricane]["Damage"] < damage_scale[4]:
        hurricanes_by_damage[4].append(hurricane)
      else:
        hurricanes_by_damage[5].append(hurricane)
  return hurricanes_by_damage

damages = rate_by_damage(hurricanes, damage_scale)
print(damages)
