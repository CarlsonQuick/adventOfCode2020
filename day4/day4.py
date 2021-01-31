import re
def passport():
    pp = {}

full_passport = ['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid']
count_valid = 0

def validate_reqs(pp):
    #byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if int(pp['byr']) < 1920 or int(pp['byr']) > 2002:
        return False
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = int(pp['iyr'])
    if iyr <2010 or iyr > 2020:
        return False

    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = int(pp['eyr'])
    if eyr <2020 or eyr > 2030:
        print('bad eyr', eyr)
        return False

    #hgt (Height) - a number followed by either cm or in:
    length = len(pp['hgt'])
    hgt_units  = pp['hgt'][length-2:length]
    hgt = int(pp['hgt'][0:length-2])
    #             If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.
    if hgt_units == 'cm' and (hgt < 150 or hgt > 193):
        return False
    elif hgt_units=='in' and (hgt < 59 or hgt > 76):
        return False
    elif hgt_units not in ['in','cm']:
        return False
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if re.match('#[0-9a-f]{6}', pp['hcl']) is None:
        return False
    #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    valid_eye_color = ['amb','blu','brn','gry','grn','hzl','oth']
    if pp['ecl'] not in valid_eye_color:
        return False
    #pid (Passport ID) - a nine-digit number, including leading zeroes.
    if  re.match('[0-9]{9}', pp['pid']) is None or len(pp['pid']) > 9:
        return False
    #cid (Country ID) - ignored, missing or not.
    return True

with open('input.txt') as f:
    passports = []
    passport = {}
    for line in f:
        if line == '\n':
            passports.append(passport)
            print(passport)
            passport = {}
        else:
            entries = line.strip().split(' ')
            for entry in entries:
                passport[entry.split(':')[0]] = entry.split(':')[1]
    passports.append(passport)

    valid_passports = []
    invalid_passports = []
    for pp in passports:
        valid = False not in [entry in pp or entry == 'cid' for entry in full_passport]
        try:
            if valid and validate_reqs(pp):
                valid_passports.append(pp)
                count_valid+=1
            else:
                invalid_passports.append(pp)
        except:
            print('parse error')
            invalid_passports.append(pp)

for valid in valid_passports:
    print (valid['ecl'], valid['eyr'], valid['byr'], valid['iyr'], valid['hgt'], valid['pid'], valid['hcl'])
print(count_valid)
