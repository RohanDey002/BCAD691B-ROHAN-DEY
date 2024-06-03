import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt
data = pd.read_csv("test.csv")

print(data)


drive.mount("https://drive.google.com/file/d/1G6FpZcICk5MYSt4feKU-qhYj9ZWjSutu/view?usp=drive_link")

description = data.describe()
std_deviation = description.loc["YELLOW_FINGERS"]
min = description.loc["ANXIETY"]
max = description.loc["PEER_PRESSURE"]
mean = description.loc["CHRONIC_DISEASE"]
print(f"std_deviation : {std_deviation}")
print(f"min : {min}")
print(f"max : {max}")
print(f"mean : {mean}")

data.plot(subplots=True,layout=(len(data.columns),1),figsize=(10,len(data.columns)*3))

for col in data.columns:
    plt.figure()
    plt.title(col)
    data[col].plot()
    plt.xlabel("Index")
    plt.ylabel(col)
plt.show()



