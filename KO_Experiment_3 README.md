# EXPERIMENT 3: Python Data Analysis (Pandas)

## I. Intended Learning Outcomes:
1. To recognize the functions and codes that are part of the Pandas library.
2. To be able to apply and utilize the numerous codes and functions while making use of the Pandas library to create a Python software.


## II. Instructions:
For this experiment, you will write Python scripts using the Jupyter Notebook to solve the given problems. You must submit your Jupyter Notebook in the designated submission bin.

### **Download Required File:**
- Download the file from [cars_csv](http://bit.ly/Cars_file) and save it to your default user folder.

### Problem 1:
- **Filename:** `Surname_Pandas-P1.py`
- **Instructions:**
  1. Load the .csv file into a Pandas DataFrame named `cars`.
  2. Display the first five and last five rows of the DataFrame `cars`.

### Problem 2:
- **Filename:** `Surname_Pandas-P2.py`
- **Instructions:**
  Using the `cars` DataFrame from Problem 1, extract the following information:
  1. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7, …).
  2. Display the row that contains the model ‘Mazda RX4’.
  3. Determine how many cylinders (`cyl`) the model ‘Camaro Z28’ has.
  4. Determine the number of cylinders (`cyl`) and gear type (`gear`) for the models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’.

## III. Setup Instructions:

### 1. Install Required Libraries:
Ensure you have Python and Pandas installed.
### 2. Running the Code:
After completing each problem, run your Python script in Jupyter Notebook or from the command line. 

Make sure to save each file with the appropriate naming convention (Surname_Pandas-P1.py, Surname_Pandas-P2.py, etc.).

## IV. Submission:
 Submit your `.py` files and Jupyter Notebook in the dedicated submission folder before the deadline.
 Make sure your code is well-commented and follows the instructions closely.

## Example Output:
```python

import pandas as pd

#read the car_csv file
car=pd.read_csv('cars.csv')

#Display the first five and last five rows of the car
car.iloc[[*range(5), *range(-5, 0)]]

  ```
## VI. HIstory:
- V1 : intial code for problem 1
- V2 : Fixed and added markdown to the code
- V3 : added code for problem 2 with markdowns and code
- V4 : Fixed in line comments 
