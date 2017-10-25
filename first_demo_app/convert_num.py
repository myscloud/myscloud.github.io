
digit_word = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า', 'สิบ']

def convert_num_to_word(num):
    # first simple demo, use just 1 least significant digit
    if type(num) == int:
        last_digit = num % 10
        return digit_word[last_digit]
