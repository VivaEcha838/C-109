import pandas as pd
import statistics

df = pd.read_csv("data.csv")

height_list = df["Height(Inches)"].to_list()

height_mean = statistics.mean(height_list)
print(height_mean)

height_median = statistics.median(height_list)
print(height_median)

height_mode = statistics.mode(height_list)
print(height_mode)

height_stdev = statistics.stdev(height_list)
print(height_stdev)

height_1st_std_dev_start = (height_mean - height_stdev)

height_1st_std_dev_end = (height_mean + height_stdev)

height_2nd_std_dev_start = (height_mean - (height_stdev*2))

height_2nd_std_dev_end = (height_mean + (height_stdev*2))

height_3rd_std_dev_start = (height_mean - (height_stdev*3))

height_3rd_std_dev_end = (height_mean + (height_stdev*3))

height_listOfData_within_1st_stdev = [result for result in height_list if result > height_1st_std_dev_start and result < height_1st_std_dev_end]

height_listOfData_within_2nd_stdev = [result for result in height_list if result > height_2nd_std_dev_start and result < height_2nd_std_dev_end]

height_listOfData_within_3rd_stdev = [result for result in height_list if result > height_3rd_std_dev_start and result < height_3rd_std_dev_end]

height_percentageOfData_within_1st_stdev = len(height_listOfData_within_1st_stdev)*100 / len(height_list)
print(height_percentageOfData_within_1st_stdev)
height_percentageOfData_within_2nd_stdev = len(height_listOfData_within_2nd_stdev)*100 / len(height_list)
print(height_percentageOfData_within_2nd_stdev)
height_percentageOfData_within_3rd_stdev = len(height_listOfData_within_3rd_stdev)*100 / len(height_list)
print(height_percentageOfData_within_3rd_stdev)