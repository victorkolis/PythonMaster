#!/usr/bin/env python3

# Rent a car for 1 day and after 7 more days get $50 off your total or 3 more days and get $20 off.

def rental_car_cost(days):
	return days * 40 if 3 > days else days * 40 - 50 if days >= 7 else days * 40 - 20

	
print(rental_car_cost(7))
