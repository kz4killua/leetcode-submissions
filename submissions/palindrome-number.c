#include <math.h>

bool isPalindrome(int x){
    
    // Negative numbers are not palindromes
    if (x < 0) 
    {
        return false;    
    }
    // Zero is a palindrome
    if (x == 0) 
    {
        return true;
    }
    
    // Check the length (number of digits) of the number
    int digits = log10(x) + 1;
    
    // Keep two pointers to the first and last digits
    int first = 0;
    int last = digits - 1;
    
    while (first < last)
    {
        // Check that the first and last digits are the same
        if (get_digit(x, first) != get_digit(x, last)) 
        {
            return false;
        }
        // Update the pointers
        first++;
        last--;
    }
    
    return true;
}


int get_digit(int x, int i)
{
    /*
    Returns the digit in the i'th place of a number x.
    
    The 0th digit is the digit in the units place.
    */
    int place = pow(10, i + 1);
    int remainder = x % place;
    int digit = remainder / pow(10, i);
    return digit;
}
