# SCORER Traffic Counter speed measurement script

## Overview
A script that measures the vehicle speed from the output result log of SCORER Traffic Counter. As shown in the image below, the vehicle speed is output when two detection lines are drawn and the distance between the detection lines is input.

![image](https://user-images.githubusercontent.com/4166534/70995489-ffec6880-2113-11ea-8778-14c23d40bef0.png)

In addition, regarding the distance between the detection lines, it is necessary to have a white line as a mark or to actually measure it.

## Requirements
Python 3.5 or above

## Usage
Execute the script with the SCORER Traffic Counter output log and distance as arguments as shown below.

```
# arguments: measure.py [csvfile] [distance(metre)]
python3 measure.py sample.csv 100 > output.csv
```
