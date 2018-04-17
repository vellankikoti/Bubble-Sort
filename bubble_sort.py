# Bubble sort Algorithm Implementation

def bubble_sort(list):
	for i in range(0,len(list)):
		for j in range(0,len(list)-1-i):
			if list[j]>list[j+1]:
			#swapping
				list[j],list[j+1] = list[j+1],list[j]
	return list

list = [15,40,20,35,10]
print(bubble_sort(list))

# output:[10,15,20,35,40]