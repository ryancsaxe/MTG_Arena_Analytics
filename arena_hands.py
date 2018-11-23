#import utilized tools
#this code is not optimized for speed, so only using built in library
import random

#set number of hands to draw from each deck
num_trials = 100000

#test decks with lands ranging from 10-20
number_of_lands_range = range(10,21)
#generate decks. 0 represents spell, 1 represents land
decks = []
for num_lands in number_of_lands_range:
	num_spells = 40 - num_lands
	deck = [0] * num_spells + [1] * num_lands
	decks.append(deck)

#iterate over the generated decks
for deck in decks:
	#compute land ratio of the deck since bo1 uses this to determine hands
	ratio = sum(deck)/40.0
	#initialize lookup tables for results on B01 and B03
	bo1_lookup = {
		0:0,
		1:0,
		2:0,
		3:0,
		4:0,
		5:0,
		6:0,
		7:0
	}
	bo3_lookup = {
		0:0,
		1:0,
		2:0,
		3:0,
		4:0,
		5:0,
		6:0,
		7:0
	}
	#simulate the trials
	for trial in range(num_trials):
		#generate the hands
		hand1 = random.sample(deck,7)
		hand2 = random.sample(deck,7)
		h1_lands = sum(hand1)
		#the first hand is the only hand for B03, so add to that lookup table
		bo3_lookup[h1_lands] += 1
		h2_lands = sum(hand2)
		#calculate which hand land-ratio is closer to the decks land-ratio
		h1_ratio_diff = abs(ratio - (h1_lands/7.0))
		h2_ratio_diff = abs(ratio - (h2_lands/7.0))
		#add to lookup table the land count for the closer ratio
		if h1_ratio_diff <= h2_ratio_diff:
			bo1_lookup[h1_lands] += 1
		else:
			bo1_lookup[h2_lands] += 1
	#print out the results for the deck
	print "Results for",sum(deck),"lands in deck"
	for i in range(8):
		print "\t",i,"land hands -- Bo1:",bo1_lookup[i]/float(num_trials) * 100,"%\t-- Bo3:",bo3_lookup[i]/float(num_trials) * 100,"%"



