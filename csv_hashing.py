import csv
import hashlib

#Functions :
def concatenate(filename):
	conc_res = ""

	#Get the col name :
	with open(filename, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		map_csv = dict(list(csv_reader)[0])
		col = list(map_csv.keys())
		my_col = col[2]
		
	#Get the odd row values:
	with open(filename, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		counter = 0
		for row in csv_reader:
			counter+=1
			if(counter%2 != 0):
				conc_res += row[my_col]
				
	return conc_res

def hashing(result):
	return hashlib.md5(result.encode()).hexdigest()

#Sample testing : 
filename = "annual-enterprise-survey-2020-financial-year-provisional-csv.csv"
result = concatenate(filename)
hashed_res = hashing(result)
print(f"concatenated string : {result}\nHashed result : {hashed_res}")

