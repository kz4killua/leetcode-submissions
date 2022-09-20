int lengthOfLastWord(char * s){

    int space = -1;
    int letter = -1;

    for (int i = 0; s[i] != '\0'; i++)
    {
        // Store the index of the last letter
        if (s[i] != ' ')
        {
            letter = i;
            // Store the index of the last space (before a letter)
            if ((i != 0) && (s[i - 1] == ' '))
            {
                space = i - 1;
            }
        }
    }
    // Compute the length of the word
    return letter - space;
}
