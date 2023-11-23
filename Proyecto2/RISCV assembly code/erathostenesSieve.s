.data

.text
li s4, 30 #N sieve size
lw s2, 16 #
li a3, 2 #first value of the sieve
li a4, 256 #first addres for the sieve
li s5, 6 # next integer of the square root of 30 (the size of the sieve)
li s7, 4 
mul a5, s7,s4
add a5, a4, s5
#fill the initial array [0,sieveSize-1]
li t0, 0 #counter
add t1, t1, zero #initialize t1  in zero
add t1, t1, a4 #first addres for the sieve
add t0,t0,zero #initialize t0 in zero
add t0, t0, a3 #set first prime number in the sieve
addi s4, s4, 1 #add one to the sieve size, for flow control reasons

fill:
    sw t0, 0(t1) #save whats in t0 to addr in t1
    addi t1, t1, 4 #increment save addr
    addi t0, t0, 1 #increment counter
    beq t0, s4, eliminate #IF THe COUNTER REACHED N+1, STOP
    j fill #loop back to fill


eliminate:
    addi t3, a4, -4 #start in the first position of the sieve
    nextPrime:
    
    addi t3,t3,4
    lw t5, 0(t3)
    #calcula el tamano del salto
    mul s6, t5, s7
    add t6, zero, t3
    beq t5, zero, nextPrime
    bge t5, s5, end
    loopSieve:
        add t6, t6, s6
        sw zero, 0(t6)
        bge t6, a5, nextPrime
        j loopSieve
        
        
end:
call 10 #exit program