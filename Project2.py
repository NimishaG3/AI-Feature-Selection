import random as rd
import math
import numpy as np
import time

def leave_one_out_cross_validation(search_type, data, current_list, feature_to_test):
  
  correct_classification_counter = 0
  
  if(search_type == 2): #Backward Elimination, remove feature from current set
    current_list.remove(feature_to_test)
  else:
    current_list.append(feature_to_test) #Forward Search, add feature to current set

  #Adapted from the MATLAB code shared in slides
  for i in range(data.shape[0]): 
    #object_to_classify = data[i, 1:]
    label_object_to_classify = data[i,0]
    nearest_neighbor_distance = math.inf;
    nearest_neighbor_location = math.inf;

    for j in range(data.shape[0]): 
      if(j != i):
        curr_distance = 0
        
        for k in current_list:
          curr_distance += pow((data[i,k] - data[j,k]), 2)
        
        curr_distance = math.sqrt(curr_distance)

        if (curr_distance < nearest_neighbor_distance):
          nearest_neighbor_distance = curr_distance
          nearest_neighbor_location = j
          nearest_neighbor_label = data[nearest_neighbor_location,0]

    if(label_object_to_classify == nearest_neighbor_label):
      correct_classification_counter += 1

  final_accuracy = correct_classification_counter / data.shape[0]
  return final_accuracy

#Adapted from the MATLAB code shared in slides
def forward_search(data):
  current_set = []
  curr_best_accuracy = 0
  curr_feature_set = []

  for i in range(1,data.shape[1]):
    print('On the', i, 'th level of the search tree')
    feature_to_add_at_this_level = []
    best_so_far_accuracy = 0

    for k in range(1, data.shape[1]):
      if(k not in current_set):
        print('----Considering adding the', k, 'feature')
        accuracy = leave_one_out_cross_validation('forward_search',data,list(current_set), k)
        #accuracy = test_accuracy(data, current_set, k+1)

        if accuracy > best_so_far_accuracy:
          best_so_far_accuracy = accuracy
          feature_to_add_at_this_level = k

    if(feature_to_add_at_this_level not in current_set):
      current_set.append(feature_to_add_at_this_level)

    if curr_best_accuracy < best_so_far_accuracy: 
      curr_best_accuracy = best_so_far_accuracy
      curr_feature_set = list(current_set)

    print('On level', i, 'i added feature ', feature_to_add_at_this_level, 'to current set with accuracy: ', best_so_far_accuracy)

  output(curr_feature_set, curr_best_accuracy)
  return

def output(curr_feature_set, curr_best_accuracy):
  print('Final output: Feature set = ', curr_feature_set, 'with accuracy =', curr_best_accuracy)
  return

#Adapted from the MATLAB code shared in slides, very minor modifications
def backward_elimination(data):
  current_set = set(list(range(1,data.shape[1])))
  curr_best_accuracy = 0
  curr_feature_set = []

  for i in range(1,data.shape[1]):
    print('On the', i, 'th level of the search tree')
    feature_to_eliminate_at_this_level = []
    best_so_far_accuracy = 0

    for k in range(1, data.shape[1]):
      if(k in current_set):
        print('----Considering removing the', k, 'feature')
        accuracy = leave_one_out_cross_validation(2,data,list(current_set), k)
        #accuracy = test_accuracy(data, current_set, k+1)

        if accuracy > best_so_far_accuracy:
          best_so_far_accuracy = accuracy
          feature_to_eliminate_at_this_level = k

    if(feature_to_eliminate_at_this_level in current_set):
      current_set.remove(feature_to_eliminate_at_this_level)

    if curr_best_accuracy < best_so_far_accuracy: 
      curr_best_accuracy = best_so_far_accuracy
      curr_feature_set = list(current_set)

    print('On level', i, 'i removed feature ', feature_to_eliminate_at_this_level, 'from current set with accuracy: ', best_so_far_accuracy)

  output(curr_feature_set, curr_best_accuracy)
  return

def main():
  print('Enter dataset to use: 1 for small dataset & 2 for large dataset\n')

  choice = input()
  
  if(choice == "1"):
    data = np.loadtxt('SmallData.txt')
  else:
    data = np.loadtxt('LargeData.txt')

  print('Awesome! :D Now choose the algo you want to use: 1 for Forward Search and 2 for Backward Elimination.\n')

  algo = input()

  time1 = time.time()

  if(algo == "1"):
    forward_search(data)
  else:
    backward_elimination(data)

  time2 = time.time() 

  print('Time taken was : %s seconds '% (time2 - time1))

main()
