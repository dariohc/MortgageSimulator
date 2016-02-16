__author__ = 'Dario'
initial_year = 2016
duration_max = 30
duration = 0
interest_rate = 2.95/100 # percent defined
mortgage = 251439 # initial amount taken
output = open('Output.txt', 'w')

while duration < duration_max:
    year = str(initial_year)
    output.write(year)
    initial_year += 1
    output.write(': ')
    output.write('interest: ')
    year_interest = str(mortgage*interest_rate)
    output.write(year_interest)
    duration += 1
    output.write('\n')
    # print ('this should be year interest', mortgage*interest_rate)

output.close()