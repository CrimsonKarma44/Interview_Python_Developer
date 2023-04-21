import random
import pandas as pd
import psycopg2


color = [
    'GREEN', 'YELLOW', 'BROWN', 'BLUE', 'PINK', 'WHITE', 'CREAM', 'ORANGE', 'RED', 'ARSH', 'BLEW', 'BLACK']

days = {'MONDAY': [3, 2, 1, 6, 1, 2, 1, 2, 1, 0, 0, 0],
        'TUESDAY': [1, 0, 2, 6, 2, 3, 0, 2, 1, 1, 1, 0],
        'WEDNESDAY': [2, 2, 1, 5, 1, 3, 0, 2, 3, 0, 0, 0],
        'THURSDAY': [2, 1, 1, 7, 1, 3, 1, 2, 1, 0, 0, 0],
        'FRIDAY': [2, 0, 1, 6, 0, 5, 0, 1, 3, 0, 0, 1]}

df = pd.DataFrame(data=days, index=color)
# Which color of shirt is the mean color?
mean = df.mean()

# Which color is the median?
median = df.median()

# BONUS Get the variance of the colors
variance = df.var()

# print(f'mean:\n{mean}\nMedian:\n{median}\nVariance:\n{variance}')


# Save the colours and their frequencies in postgresql database
hostname = ''
database = ''
username = ''
pwd = ''
port_id = 5432
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE Color_frequency(Color VARCHAR(20) PRIMARY KEY, Monday INTEGER, Tuesday INTEGER, Wednesday INTEGER, Thusrday INTEGER, Friday INTEGER)")
    for i in range(len(color)):
        cur.execute(
            f"INSERT INTO Color_frequency VALUES({color[i]}, {days['MONDAY'][i]},{days['TUESDAY'][i]}, {days['WEDNESDAY'][i]}, {days['THURSDAY'][i]}, {days['FRIDAY'][i]})")
    conn.commit()
    conn.close()
    cur.close()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if cur is not None:
        conn.close()

#  BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def slicer(num, listd):
    if listd:
        if num == listd[-1]:
            return True
        else:
            listd.pop()
            return slicer(num, listd)
    else:
        return False


# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
random_num = '0b'
for i in range(4):
    value = str(random.randrange(0, 2))
    random_num += value

print(f'{random_num}: {int(random_num, 2)}')


# Write a program to sum the first 50 fibonacci sequence
def fib(num):
    count = 0
    value1 = 0
    value2 = 1
    while count <= num:
        yield value1
        temp = value2
        value2 += value1
        value1 = temp

        count += 1


summed = 0
for i in fib(50):
    summed += i
    summed
