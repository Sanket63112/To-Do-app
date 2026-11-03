feet_inches = input('Enter feet and inches: ')
print('converts feets and inches to meters:')
def convert_meters(feet_inches):
    part = feet_inches.split(' ')
    feet = float(part[0])
    inches = float(part[1])
    meters = feet*0.3048 + inches*0.0254
    return meters

in_meters = convert_meters(feet_inches)

print(f"{round(in_meters,3)} m")