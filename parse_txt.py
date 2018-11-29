import json

file_object  = open("evip_zscore.txt", "r")
data = []
all = file_object.readlines()
for line in all[1:2]:
    split = line.split()

    gene_id = split[0]

    markers1 = str([float(split[1]), float(split[2]), float(split[3]), float(split[4])])
    avg1 = str([(float(split[1]) + float(split[2]) + float(split[3]) + float(split[4]))/4.0])

    first = '{"title": "' + str(gene_id[0:4]) + '-' + str(gene_id[10:]) + '" , "subtitle": "RNF43_WT", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + markers1 + ', "averages":' + avg1 + '}'
    data.append(first)

    markers2 = str([float(split[5]), float(split[6]), float(split[7]), float(split[8])])
    avg2 = str([(float(split[5]) + float(split[6]) + float(split[7]) + float(split[8]))/4.0])

    second = '{"title": "", "subtitle": "GFP", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + markers2 + ', "averages":' + avg2 + '}'
    data.append(second)

    markers3 = str([float(split[9]), float(split[10]), float(split[11]), float(split[12])])
    avg3 = str([(float(split[9]) + float(split[10]) + float(split[11]) + float(split[12]))/4.0])

    third = '{"title": "", "subtitle": "RNF43_659fs", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + markers3 + ', "averages":' + avg3 + '}'
    data.append(third)

    markers4 = str([float(split[13]), float(split[14]), float(split[15]), float(split[16])])
    avg4 = str([(float(split[13]) + float(split[14]) + float(split[15]) + float(split[16]))/4.0])

    fourth = '{"title": "", "subtitle": "RNF43_117fs", "ranges": [0, 8, 8], "measures": [4, 8], "markers":' + markers4 + ', "averages":' + avg4 + '}'
    data.append(fourth)

datajson = json.dumps(data)
print(datajson)

with open('data_reorg.json', 'w') as outfile:
    outfile.write('[')
    outfile.write('\n')
    for dataline in data:
        outfile.write('  ')
        outfile.write(dataline)
        if (dataline != data[-1]):
            outfile.write(',')
        outfile.write('\n')
    outfile.write(']')
