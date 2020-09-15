# open file and dedup
src_set = set(open("D:\src.txt").readlines())
src = list(src_set)

# sort
src.sort()

# delimit by '\'
src_list = []
for i in src:
    src_list.append(i.rstrip().split('\\'))  # [FOLDER, RAW/BIN, YYYYMMDD]

# separate by folder
previous_folder = ""
entire_month = []   # used for padding non-existing date
dst = open("D:\dst.txt", 'w')

for i in src_list:
    current_folder = i[0] + '_' + i[1]
    current_date = int(i[2][6:8])
    if previous_folder != current_folder:
        dst.write('\n'.join(entire_month))
        entire_month = ["NULL"] * 31

        previous_folder = current_folder
        dst.write('\n\n' + current_folder + '\n')

    entire_month[current_date -1] = i[2]

dst.write('\n'.join(entire_month))