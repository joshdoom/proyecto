def is_number(value, max_lenght: int):
    if value.isdigit() and len(str(value)) <= max_lenght or value == '':
        return True
    else:
        return False

def is_letter(value):
    if  value.isalpha() or value == '':
        return True
    else:
        return False
