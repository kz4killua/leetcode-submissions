/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {

    if (!head || !head->next) {
        return head;
    }

    struct ListNode *prev = head;
    struct ListNode *node = head->next;

    while (node) 
    {
        if (node->val == prev->val)
        {
            // Delete the node from the list
            prev->next = node->next;
        }
        else {
            // Update the previous node
            prev = node;
        }

        // Move to the next node
        node = node->next;
    }

    return head;   
}
