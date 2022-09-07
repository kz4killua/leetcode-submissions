

int numberOfSteps(int num){
    int steps = 0;
    
    while (num) 
    {
        // Check if the number is odd and subtract 1
        if (num % 2) 
        {
            num -= 1;
        }
        // If the number is even, divide by 2
        else 
        {
            num /= 2;
        }
        // Increment the number of steps performed
        steps++;
    }
    return steps;
}
