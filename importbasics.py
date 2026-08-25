import math
sqrt_25 = math.sqrt(25)
print(f"The square root of 25 is: {sqrt_25}")

#import random
import random
random_number = random.randint(1, 100)
print(f"The random number between 1-100 is  {random_number}")

#import datetime
import datetime
current_date = datetime.datetime.now()
print(f"Current date and time is: {current_date}")
today = datetime.date.today()
print(f"Today's date is: {today}")

#import pandas
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
print("DataFrame created using pandas:")
df = pd.DataFrame(data)
print(df)