# MAKE THE DEAD FISH SWIM

### Challenge

Write a simple parser that will parse and run Deadfish.

Dead fish has 4 commands, each 1 character long:

    i increments the value (initially 0)
    d decrements the value
    s squares the value
    o outputs the value into the return array

Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]