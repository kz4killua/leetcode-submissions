

bool isValid(char * s){
    
    char stack[10001];
    int stack_size = 0;
    
    
    for (int i = 0; s[i] != '\0'; i++)
    {
        // Add opening characters to the stack
        if (s[i] == '(' || s[i] == '[' || s[i] == '{')
        {
            stack[stack_size] = s[i];
            stack_size++;
        } 
        else
        {
            // If the stack is empty, return False
            if (stack_size == 0)
            {
                return false;
            }
            // Make sure closing characters match the last item on the stack
            if (
                (s[i] == '}' && stack[stack_size - 1] != '{') ||
                (s[i] == ')' && stack[stack_size - 1] != '(') ||
                (s[i] == ']' && stack[stack_size - 1] != '[')
            )
            {
                return false;
            }
            // Remove the last item on the stack.
            stack_size--;
        }
    }
    
    // At the end, the stack should be empty
    return stack_size == 0;
}
