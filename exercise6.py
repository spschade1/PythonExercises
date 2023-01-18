#Ordinal numbers

def ordinalSuffix(number):
    numberStr = str(number)

    if numberStr[-2:] in ('11', '12', '13'):
        return numberStr + 'th'
    
    if numberStr[-1] == '1':
        return numberStr + 'st'
    
    if numberStr[-1] == '2':
        return numberStr + 'nd'
    
    if numberStr[-1] == '3':
        return numberStr + 'rd'
    
    return numberStr + 'th'


print(ordinalSuffix(101))