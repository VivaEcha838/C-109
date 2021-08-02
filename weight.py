import pandas as pd
import statistics

df = pd.read_csv("data.csv")

weight_list = df["Weight(Pounds)"].to_list()

weight_mean = statistics.mean(weight_list)
print(weight_mean)

weight_median = statistics.median(weight_list)
print(weight_median)

weight_mode = statistics.mode(weight_list)
print(weight_mode)

weight_stdev = statistics.stdev(weight_list)
print(weight_stdev)

weight_1st_std_dev_start = (weight_mean - weight_stdev)

weight_1st_std_dev_end = (weight_mean + weight_stdev)

weight_2nd_std_dev_start = (weight_mean - (weight_stdev*2))

weight_2nd_std_dev_end = (weight_mean + (weight_stdev*2))

weight_3rd_std_dev_start = (weight_mean - (weight_stdev*3))

weight_3rd_std_dev_end = (weight_mean + (weight_stdev*3))

weight_listOfData_within_1st_stdev = [result for result in weight_list if result > weight_1st_std_dev_start and result < weight_1st_std_dev_end]

weight_listOfData_within_2nd_stdev = [result for result in weight_list if result > weight_2nd_std_dev_start and result < weight_2nd_std_dev_end]

weight_listOfData_within_3rd_stdev = [result for result in weight_list if result > weight_3rd_std_dev_start and result < weight_3rd_std_dev_end]

weight_percentageOfData_within_1st_stdev = len(weight_listOfData_within_1st_stdev)*100 / len(weight_list)
print(weight_percentageOfData_within_1st_stdev)
weight_percentageOfData_within_2nd_stdev = len(weight_listOfData_within_2nd_stdev)*100 / len(weight_list)
print(weight_percentageOfData_within_2nd_stdev)
weight_percentageOfData_within_3rd_stdev = len(weight_listOfData_within_3rd_stdev)*100 / len(weight_list)
print(weight_percentageOfData_within_3rd_stdev)