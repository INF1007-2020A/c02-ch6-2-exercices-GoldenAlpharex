#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_even_keys(dictionary):
	# result = set({})
	# for key, value in dictionary.items():
	# 	if key % 2 == 0:
	# 		result.add(key)
	# return result
	# return {k for k, v in dictionary.items() if k % 2 == 0}  # Compréhension de dictionaire :)
	return {k for k in dictionary.keys() if k % 2 == 0} # En utilisant une fonction plus smart :)

def join_dictionaries(dictionaries):
	# joined_dictionaries = {}
	# for dictionary in dictionaries:
	# 	for k, v in dictionary.items():
	# 		joined_dictionaries[k] = v
	# return joined_dictionaries
	#
	# result = {}
	# for d in dictionaries:
	# 	result.update(d)  # big brain move right there.
	# return result
	#
	return {key: value for dictionary in dictionaries for key, value in dictionary.items()} 

def dictionary_from_lists(keys, values):
	# return {keys[i]: values[i] for i in range(min(len(keys), len(values)))} # Big brain le prof, ce que j'ai fait marchait pas.
	return dict(zip(keys, values)) # Even bigger brain, usage of zip()

def get_greatest_values(dictionary, num_values):
	# liste = []
	# # On sort les values du dictionaire et on les met dans une liste
	# for value in dictionary.values():
	# 	liste.append(value)
	# # On arrange la liste pour qu'elle donne du plus grand au plus petit.
	# liste.sort(reverse = True)
	# # On crée result tel que result va juste avoir num_values éléments dedans.
	# result = liste[:num_values]

	# return result
	return sorted(dictionary.values(), reverse=True)[0:num_values]

def get_sum_values_from_key(dictionaries, key):
	# total = 0
	# for dic in dictionaries:
	# 	if key in dic:
	# 		total += dic[key]
	# return total
	return sum([dic[key] for dic in dictionaries if key in dic])

if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
