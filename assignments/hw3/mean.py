"""
Name: Jessica Andrews
mean.py

Problem: A python program designed to output the RMS Average, Harmonic Mean and the
Geometric mean
I certify that this program is entirely my own work

"""
# take in a number of inputs and spit out a output of each RMS Harmonic and Geometric
# the program will output the RMS Average, Harmonic Mean, and the Geometric mean
# 1. ask for inputs and how many inputs
# 2. put the equations into code form
# 3. write a loops to use how many numbers in the loop
import math


def main():

    # variables required for arithmetic to work
    num_in_seq = eval(input("How many values will you use?"))
    add = 0
    mult = 1
    denom = 0
    # for loop containing arithmetic
    for _ in range(num_in_seq):
        var = eval(input("Enter your variables:"))
        add = add + var**2
        aver = add / num_in_seq
        rms_aver = math.sqrt(aver)
        frac = 1/var
        denom = denom + frac
        harmonic_mean = num_in_seq/denom
        mult = mult * var
        geometric_mean = mult**(1/num_in_seq)
# round statements to make sure the numbers are correct as well as print statements
    ans1 = round(rms_aver, 3)
    print(ans1)
    ans2 = round(harmonic_mean, 3)
    print(ans2)
    ans3 = round(geometric_mean, 3)
    print(ans3)


if __name__ == '__main__':
    main()
