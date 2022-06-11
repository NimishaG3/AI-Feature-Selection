import numpy as np
import matplotlib.pyplot as plt

# creating the dataset

num_features = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

accuracies = [84.1,95.5,94.3,92.2,90.2,87.8,84.3,82.4,81.7,81.6,80.7,79.8,79.9,79.8,79.5,78.8,78.4,77.8,76.7,76.6,77,75.9,74.9,74.9,73.8,73.6,73.7,73.9,74,73.8,73.4,72.8,72.7,72.3,71.9,71,70.6,69.5,68,68]

fig = plt.figure(figsize = (15, 5))
#y-time x-type of algo
# creating the bar plot
plt.bar(num_features, accuracies, color ='orange',width = 0.3)

x_ticks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
y_ticks = [10,20,30,40,50,60,70,80,90,100]
#specify x-axis labels
#x_labels = ['A', 'B', 'C', 'D', 'E'] 

#add x-axis values to plot
plt.xticks(ticks=x_ticks)
plt.yticks(ticks=y_ticks)

plt.text(1,84.1,'24', ha="center")
plt.text(2,95.5,'2', ha="center")
plt.text(3,94.3,'8', ha="center")
plt.text(4,92.2,'13', ha="center")
plt.text(5,90.2,'35', ha="center")
plt.text(6,87.8,'27', ha="center")
plt.text(7,84.3,'23', ha="center")
plt.text(8,82.4,'9', ha="center")
plt.text(9,81.7,'30', ha="center")
plt.text(10,81.6,'21', ha="center")

plt.text(11,80.7,'5', ha="center")
plt.text(12,79.8,'7', ha="center")
plt.text(13,79.9,'33', ha="center")
plt.text(14,79.8,'22', ha="center")
plt.text(15,79.5,'32', ha="center")
plt.text(16,78.8,'20', ha="center")
plt.text(17,78.4,'6', ha="center")
plt.text(18,77.8,'12', ha="center")
plt.text(19,76.7,'15', ha="center")
plt.text(20,76.6,'26', ha="center")

plt.text(21,77,'40', ha="center")
plt.text(22,75.9,'34', ha="center")
plt.text(23,74.9,'14', ha="center")
plt.text(24,74.9,'11', ha="center")
plt.text(25,73.8,'17', ha="center")
plt.text(26,73.6,'28', ha="center")
plt.text(27,73.7,'37', ha="center")
plt.text(28,73.9,'29', ha="center")
plt.text(29,74,'36', ha="center")
plt.text(30,73.8,'38', ha="center")

plt.text(31,73.4,'39', ha="center")
plt.text(32,72.8,'31', ha="center")
plt.text(33,72.7,'25', ha="center")
plt.text(34,72.3,'18', ha="center")
plt.text(35,71.9,'19', ha="center")
plt.text(36,71,'3', ha="center")
plt.text(37,70.6,'16', ha="center")
plt.text(38,69.5,'1', ha="center")
plt.text(39,68,'4', ha="center")
plt.text(40,68,'10', ha="center")


#add_value_label(num_features,accuracies)

#plt.text(1, , 'abc', fontdict=None, ha="center")
 
plt.xlabel("Number of Features Added")
plt.ylabel("Accuracy(%)")
plt.title("Accuracy v/s Number of features Added: Forward Search on Large Dataset-40")
plt.show()