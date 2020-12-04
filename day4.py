d4input = []

with open('d4input.txt','r') as f:
        inlines = f.readlines()
        for line in inlines :
            d4input.append(line.strip('\n'))

count = 0
i = 0

def is_valid(field, input_str) :
    if field == 'eyr' :
        check_index = input_str.find('eyr')
        check_value = int(input_str[(check_index+4):(check_index+8)])
        if int(check_value) >=2020 and int(check_value)<=2030:
            return True

    elif field == 'pid' :
        check_index = input_str.find('pid')
        count_nums = 0
        i = check_index+4
        the_one = input_str[check_index+4:]
        while input_str[i] != ' ' and i < (check_index+3 + len(input_str[check_index+4:])):
            count_nums += 1
            i += 1
        if count_nums == 9 or len(the_one) == 9:
            return True
        else :
            return False

    elif field == 'byr' :
        check_index = input_str.find('byr')
        check_value = int(input_str[(check_index+4):(check_index+8)])
        if int(check_value) >=1920 and int(check_value)<=2002:
            return True
        else :
            return False

    elif field == 'hgt' :
        check_index = input_str.find('hgt')
        i = check_index+4
        count = 0
        while input_str[i] != ' ' and i < (check_index+3 + len(input_str[check_index+4:])):
            count += 1
            i += 1
        the_value = input_str[check_index+4:check_index+5+count].strip(' ')
        if the_value[-2:] == 'cm' :
            if int(the_value[:-2]) >= 150 and int(the_value[:-2]) <=193:
                return True
            else:
                return False
        elif the_value[-2:] == 'in' :
            if int(the_value[:-2]) >= 59 and int(the_value[:-2]) <=76:
                return True
            else:
                return False

    elif field == 'hcl' :
        check_index = input_str.find('hcl')
        i = check_index+4
        if input_str[i] != '#':
            return False
        
        count = 0

        while input_str[i] != ' ' and i < (check_index+3 + len(input_str[check_index+4:])):
            count += 1
            i += 1
        the_value = input_str[check_index+4:check_index+5+count].strip(' ')

        if len(the_value) < 6 or len(the_value) > 8 :
            return False
        acceptable_range = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        
        for j in range(1,7) :
            if the_value[j] not in acceptable_range :
                return False
        
        return True

    elif field == 'ecl' :
        check_index = input_str.find('ecl')
        check_value = input_str[(check_index+4):(check_index+7)]
        acceptable_range = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if check_value in acceptable_range :
            return True
        else :
            return False
    
    elif field == 'iyr' :
        check_index = input_str.find('iyr')
        check_value = int(input_str[(check_index+4):(check_index+8)])
        if int(check_value) >=2010 and int(check_value)<=2020:
            return True
        else :
            return False

# test_str = 'hgt:153cm'

# print(is_valid('hgt', test_str))


while i < len(d4input) :
    has_ecl = False
    has_pid = False
    has_eyr = False
    has_hcl = False
    has_byr = False
    has_iyr = False
    has_cid = False
    has_hgt = False
    while d4input[i] != '' :
        if 'ecl' in d4input[i] :
            has_ecl = is_valid('ecl', d4input[i])
            #print(has_ecl)
        if 'pid' in d4input[i] :
            has_pid = is_valid('pid', d4input[i])
            #print(has_pid)
        if 'eyr' in d4input[i] :
            has_eyr = is_valid('eyr', d4input[i])
            #print(has_eyr)
        if 'hcl' in d4input[i] :
            has_hcl = is_valid('hcl', d4input[i])
            #print(has_hcl)
        if 'byr' in d4input[i] :
            has_byr = is_valid('byr', d4input[i])
            #print(has_byr)
        if 'iyr' in d4input[i] :
            has_iyr = is_valid('iyr', d4input[i])
            #print(has_iyr)
        # if 'cid' in d4input[i] :
        #     has_cid = True
        if 'hgt' in d4input[i] :
            has_hgt = is_valid('hgt', d4input[i])
            #print(has_hgt)
        if has_ecl and has_pid and has_eyr and has_hcl and has_byr and has_iyr and has_hgt :
            count += 1
            break
        if i >= (len(d4input)-1) :
            break
        i += 1
    i += 1

print(count)