#!/usr/bin/env python


class Knapsack:
	def fill_knapsack(self, memo, objects):
		i=len(objects)
		sub_capacity=self.capacity
		while (i>0 and sub_capacity>0):
			object_value=objects[i].get_value()
			object_weight=objects[i].get_weight()
			if object_weight<sub_capacity and not max(memo[i-1][sub_capacity], object_value+memo[i-1][sub_capacity-object_weigth])==memo[i-1][sub_capacity]:
				self.knapsack_elements.append(objects[i])
				sub_capacity-=object_weight
			i-=1			

	def __init__(self, capacity, objects):
		self.capacity=capacity
		memo=[[0 for i in range(0, len(objects)+1)] for i in range(capacity+1)]
		for i in range(1, len(objects)):
			for sub_capacity in range(1, capacity):
					if objects[i].weight() > sub_capacity:
						memo[i][sub_capacity]=memo[i-1][sub_capacity]
					else:
						memo[i][sub_capacity]=max(memo[i-1][sub_capacity], objects[i].value()+memo[i-1][sub_capacity-objects[i].weigth()])
		self.value=memo[len(objects)][capacity]
		self.knapsack_elements=[]
		fill_knapsack(self, memo, objects)

	def get_knapsack_elements():
		return self.knapsack_elements

	def get_value():
		return self.value
			
			
