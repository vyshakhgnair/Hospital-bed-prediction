import pandas as pd


data=pd.read_csv("/home/vyshakhgnair/Desktop/unni/fossera/prediction.csv")
df=pd.DataFrame(data)
#data.describe()


row_list=[]
mean_bed=0
mean_icu=0
mean_oxygen=0
sum_bed=0
sum_icu=0
sum_oxygen=0
count=0
for rows in df.itertuples():
    my_list=[rows.Month,rows.bed_count,rows.icu_count,rows.oxygen_count]
    row_list.append(my_list)

for i in row_list:
    if(i[0]==1):
        count=count+1
        sum_bed=sum_bed+i[1]
        sum_icu=sum_icu+i[2]
        sum_oxygen=sum_oxygen+i[3]

mean_bed=int(sum_bed/count)
mean_icu=int(sum_icu/count)
mean_oxygen=int(sum_oxygen/count)
