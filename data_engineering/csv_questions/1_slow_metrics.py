"""
You are a backend engineer at ACME Solutions LLC, a large tech company serving millions of users. However, the company’s services are currently suffering from some performance issues, which they have tasked you to investigate. Services publish execution metrics as very large CSV files, each file being over 50GB in size. These files are stored on a disk somewhere, easily accessible by you.

The CSVs are in the following format:

timestamp,execution_length,metadata

1,20,data1
2,10,data2
3,50,data3
4,30,data4
The director of engineering has asked you to write a program that will:

1. Identify the slow_metrics, which are the metrics with the longest execution_length.

2. Return the preceding_metrics count of metrics immediately before the identified slow_metrics.

Input Parameters:

* slow_metrics: Number of slowest metrics to retrieve.

* preceding_metrics: Number of preceding metrics to include before each slow metric.
"""
