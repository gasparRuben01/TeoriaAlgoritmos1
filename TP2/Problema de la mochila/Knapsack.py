#!/usr/bin/env python


class Knapsack:
	def fill_knapsack(self, memo, objects):
		i=len(objects)
		sub_capacity=self.capacity
		while (i>0 and sub_capacity>0):
			k=i-1
			object_value=objects[k].get_value()
			object_weigth=objects[k].get_weigth()
			if object_weigth<=sub_capacity and memo[i-1][sub_capacity]<object_value+memo[i-1][sub_capacity-object_weigth]:
				self.knapsack_elements.append(objects[k])
				sub_capacity-=object_weigth
			i-=1			

	def __init__(self, capacity, objects):
		self.capacity=capacity
		memo=[[0]*(capacity+1) for i in range(len(objects)+1)]
		for i in range(1, len(objects)+1):
			k=i-1
			for sub_capacity in range(1, capacity+1):
					if objects[k].get_weigth() > sub_capacity:
						memo[i][sub_capacity]=memo[i-1][sub_capacity]
					else:
						memo[i][sub_capacity]=max(memo[i-1][sub_capacity], objects[k].get_value()+memo[i-1][sub_capacity-objects[k].get_weigth()])
		self.value=memo[len(objects)][capacity]
		self.knapsack_elements=[]
		self.fill_knapsack(memo, objects)

	def get_elements(self):
		return self.knapsack_elements

	def get_value(self):
		return self.value
			
			
