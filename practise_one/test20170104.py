import calendar
months = ['January','February','March','Aprial','May','June','July', 'Auguest','September','October','November','December']
endings = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year = input('Year: ')
month = input('Month(1-12): ')
day = input('Day(1-31):')
####
#monthRange = calendar.monthrange(int(year) ,int(month))[1]
#if(int(day)>monthRange):
#day = input('again:Day(1-'+str(monthRange)+'):')
####
month_number = int(month)
day_number = int(day)
month_name = months[month_number-1]
ordinal = day+endings[day_number-1]
print(month_name+' '+ordinal+'.'+year)
