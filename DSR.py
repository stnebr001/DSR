# necessary packages
import pandas as pd

# reading in data
# the first row is the title of the table and needs to be removed
data = pd.read_excel(r"C:\Users\IC\Desktop\New folder (2)\pone.0212445.s004.xlsx", 
                     sheetname = "estimates", skiprows = [0])
print(data) # checking if data has been read in

## What is the total number of people living with HIV (NoPLHIV) in the listed districts according to the Survey estimate?

ind = data["Estimate"] == "Survey" # find which estimates are from the survey
print(ind)

print(sum(data["NoPLHIV"] * ind)) # find the NoPLHIV total

def totalPLHIV(data,column,condition): # creating a function
    total = sum(data[column] * ind)
    return total

print(totalPLHIV(data,"NoPLHIV",ind)) # answer
print(totalPLHIV(data,"NoPLHIV_LCL",ind)) # lower bound
print(totalPLHIV(data,"NoPLHIV_UCL",ind)) # upper bound

## What is the average NoPLHIV of the two estimates used for “Xhariep”?

ind = data["District"] == "Xhariep" # find the appropriate district
print(ind)

sum(data["NoPLHIV"] * ind) / sum(ind) # find the average NoPLHIV

def meanPLHIV(data,column,ind): # creating a function
    mean = sum(data[column] * ind) / sum(ind)
    return mean

print(meanPLHIV(data,"NoPLHIV",ind)) # answer
print(meanPLHIV(data,"NoPLHIV_LCL",ind)) # lower bound
print(meanPLHIV(data,"NoPLHIV_UCL",ind)) # upper bound

## Add a column and populate it with the number of people not living with HIV for each row

data["NoPNLHIV"] = data["NoPLHIV"] * 100 / data["Prevalence_%"] # NoPNLHIV = Number of People Not Living with HIV
print(data) 

## What is the total NoPLHIV in all the cities (districts with the word “city” or “metro” in the name)?

total = None # setting initial value to None
estimate = "Survey" # the type of estimate so that there's no double counting / could have used averages 
for i in range(len(data)): # for each district
    if "city" in data["District"][i].lower() or "metro" in data["District"][i].lower(): # if it contains the keyword(s)
        if data["Estimate"][i] == estimate: # if it is the proper estimate type
            if total == None: # if total doesn't have a value
                total = data["NoPLHIV"][i] # add a value
            else:
                total += data["NoPLHIV"][i] # add the NoPLHIV to the current total
print(total) # total NoPLHIV in cities

def keyPLHIV(data,keywords,estimate): # creating a function
    total = None # setting initial value to None
    for i in range(len(data)): # for each district
        for key in keywords: # for each keyword
            check = 0 # setting initial check to 0
            if key in data["District"][i].lower(): # if the district contains the keyword
                check = 1 # district passes the check
                break # end looping keywords
        if data["Estimate"][i] == estimate and check == 1: # if the district contains the keyword and is the estimate type
            if total == None: # if total doesn't have a value
                total = data["NoPLHIV"][i] # add a value
            else:
                total += data["NoPLHIV"][i] # add the NoPLHIV to the current total
    return total # return the total 

keyPLHIV(data,["city","metro"],"Survey") # answer

## Write the original data (without the caption - originally row 1) with the extra columns as comma-separated values (CSV) to a new .csv file
data.to_csv(r"C:\Users\IC\Desktop\New folder (2)\new.pone.0212445.s004.csv", index = False)






































