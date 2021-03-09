<!-- ABOUT THE PROJECT -->
## About The Project

This is a project for Embedded System Lab's homework.
It is about using Python to read and using the data from .csv **without** using external library like numpy, pandas, matplotlib, etc.

### Built With

* [Python](https://www.python.org)

## Homework Description
* Remove the data whose value of the TEMP (temperature)   column is '-99.000' or '-999.000'.
* Find out the maximum of the TEMP value from C0A880, C0F9A0, C0G640, C0R190, C0X260.
* Output the ID of the station and the maximum of it in the lexicographical order.
* If you cannot find the maximum, please output 'None'.

<!-- GETTING STARTED -->
## Getting Started

### Running

* Open Terminal and run the command
  
    ```sh
    python3.8 hw1.py
    ```


<!-- ROADMAP -->
## Roadmap

1. Import the module to operate csv files

2. Read the weather data from '107061123.csv', and store the data information.

3. Remove the data whose value of the TEMP (temperature) column is '-99.000' or '-999.000'. Use `for-loop` to check all the 'TEMP' in data, if 'TEMP' is '-99.000' or '-999.000', then replace it as `None`.
    ```python
    for i in data:
      if i['TEMP'] == '-99.000' or i['TEMP'] == '-999.000':
        i['TEMP'] = None
    ```

4. Find out the maximum of the TEMP value from C0A880, C0F9A0, C0G640, C0R190, C0X260. Make a list for C0A880, C0F9A0, C0G640, C0R190, C0X260, and sort it by lexicographical order, and use it to check the main list to store.
    ```python
    id_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
    id_list.sort()
    ```

5. Restore the useful data into five sublists by `append()`, then sort the sublist individually using lambda as the sort key. Although, I need to check if the 'TEMP' value is `None`. If it is `None`, I change the value into minus infinite by using `float('-inf')` for comparing with other floating number, and if it is not `None`, then just change the value into floating number simply.
    ```python
    for i in range(0,5):
      all_list[i].sort(reverse=True, key=lambda x: float('-inf') if x['TEMP'] is None else float(x['TEMP']))
    ```

6. Print out the value based on the format. And also if all the value are `None` (means the maximum value **isn't** existed), it will output 'None'.
    ```python
    output_list = []
    for i in range(0,5):
      if(all_list[i][0]['TEMP'] is not None):
        output_list.append([id_list[i], float(all_list[i][0]['TEMP'])])
      else:
        output_list.append([id_list[i], "None"]) 

    print(output_list)
    ```

<!-- Screenshot -->
## Results

<img src="https://github.com/SYJINTW/NTHU240500_hw1/blob/main/Image/result.png?raw=true">

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [w3schools.com](https://www.w3schools.com/python/)

