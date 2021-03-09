# Part. 1
#=======================================
# Import module
# csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061123.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# TODO:
# Remove the data whose value of the TEMP (temperature) column is '-99.000' or '-999.000'.
for i in data:
   if i['TEMP'] == '-99.000' or i['TEMP'] == '-999.000':
      i['TEMP'] = None
      #data.remove(i)

# Find out the maximum of the TEMP value from C0A880, C0F9A0, C0G640, C0R190, C0X260.

# Way 1
id_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
id_list.sort()

all_list = [[],[],[],[],[]]

for i in data:
   if i['station_id'] == id_list[0]:
      all_list[0].append(i) 
   elif i['station_id'] == id_list[1]:
      all_list[1].append(i) 
   elif i['station_id'] == id_list[2]:
      all_list[2].append(i) 
   elif i['station_id'] == id_list[3]:
      all_list[3].append(i) 
   elif i['station_id'] == id_list[4]:
      all_list[4].append(i) 

for i in range(0,5):
   all_list[i].sort(reverse=True, key=lambda x: float('-inf') if x['TEMP'] is None else float(x['TEMP']))

# Way 2
# define a sort function to sort the data in float type
def mySort(e):
      return float(e['TEMP'])
_list = [[],[],[],[],[]]

# Find max of C0A880
for i in data:
   if i['station_id'] == 'C0A880':
      _list[0].append(i)
_list[0].sort(reverse=True, key=mySort)

# Find C0F9A0
for i in data:
   if i['station_id'] == 'C0F9A0':
      _list[1].append(i)
_list[1].sort(reverse=True, key=mySort)

# Find C0G640
for i in data:
   if i['station_id'] == 'C0G640':
      _list[2].append(i)
_list[2].sort(reverse=True, key=mySort)

# Find C0R190
for i in data:
   if i['station_id'] == 'C0R190':
      _list[3].append(i)
_list[3].sort(reverse=True, key=mySort)


# Find C0X260
for i in data:
   if i['station_id'] == 'C0X260':
      _list[4].append(i)
_list[4].sort(reverse=True, key=mySort)


# Output the ID of the station and the maximum of it in the lexicographical order.
# If you cannot find the maximum, please output 'None'.
output_list = []
for i in range(0,5):
   if(all_list[i][0]['TEMP'] is not None):
      output_list.append([id_list[i], float(all_list[i][0]['TEMP'])])
   else:
     output_list.append([id_list[i], "None"]) 

print(output_list)





