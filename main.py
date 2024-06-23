total_stokes = 20

stroke_data = {}
cangjie_data = {}
unicode_data = {}

cnt = 0

exclude_char = ['㽼', '䣟', '㳗', '迬', '壵', '姙', '峑', '恎', '㤬', '恠', '㤛', '㳝', '洤', '茎', '祍', '匨', '垩', '徍', '䂇', '㑠', '㘽', '㛇', '㦳', '柽', '绖', '诳', '钮', '闺', '陧', '䶭']


with open('CNS_stroke.txt') as stroke_data_file:
    lines = stroke_data_file.readlines()
    for line in lines:
        cns_code, n_strokes = line.split()
        strokes = int(n_strokes)
        if not strokes in stroke_data:
            stroke_data[strokes] = []
        stroke_data[strokes].append(cns_code)

with open('CNS_cangjie.txt') as cangjie_data_file:
    lines = cangjie_data_file.readlines()
    for line in lines:
        cns_code, cangjie = line.split()
        cangjie_data[cns_code] = cangjie

with open('CNS2UNICODE_Unicode_1.txt') as unicode_data_file:
    lines = unicode_data_file.readlines()
    for line in lines:
        cns_code, unicode = line.split()
        unicode_data[cns_code] = unicode

with open('CNS2UNICODE_Unicode_2.txt') as unicode_data_file:
    lines = unicode_data_file.readlines()
    for line in lines:
        cns_code, unicode = line.split()
        unicode_data[cns_code] = unicode

with open('CNS2UNICODE_Unicode_3.txt') as unicode_data_file:
    lines = unicode_data_file.readlines()
    for line in lines:
        cns_code, unicode = line.split()
        unicode_data[cns_code] = unicode

for i in range(1, total_stokes):
    for cns_code_1 in stroke_data[i]:
        if not cns_code_1 in cangjie_data:
            continue
        cangjie_1 = cangjie_data[cns_code_1]
        
        if not cangjie_1.startswith('K') or not cangjie_1.endswith('NL'):
            continue

        for cns_code_2 in stroke_data[total_stokes-i]:
            if not cns_code_2 in cangjie_data:
                continue
            cangjie_2 = cangjie_data[cns_code_2]
            if cangjie_2.endswith('G'):
                unicode_1 = unicode_data[cns_code_1]
                unicode_2 = unicode_data[cns_code_2]
                if not len(unicode_1) == 4 or not len(unicode_2) == 4:
                    continue
                char_1 = chr(int(unicode_1, 16))
                char_2 = chr(int(unicode_2, 16))
                if char_1 in exclude_char or char_2 in exclude_char:
                    continue
                cnt += 1
                print(cnt, char_1, char_2)