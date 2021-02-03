#!/usr/bin/env python3

#"1234"   -->  true
#"12345"  -->  false
#"a234"   -->  false

def validate_pin(pin):
	return pin.isnumeric() if len(pin) == 4 or len(pin) ==  6 else False
	
	
print(validate_pin('1240'))
