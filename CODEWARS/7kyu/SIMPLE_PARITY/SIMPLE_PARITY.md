# SIMPLE PARITY

### Challenge

Say you have a string and its length is even. Your goal
is to combine the first, and the last character in that string,
the second, and the second to the last and so on:


'ABCD' => 'ADBC'

If the length of the string is odd you should then return all caps 'IMPAR' 
which is odd in Latin:

'ABCDE' => 'IMPAR'


Now if the length is equal to two simply invert them:

'AB' => 'BA'

At last, CAPITALIZATION MATTERS:

'defg' => 'DGEF'
