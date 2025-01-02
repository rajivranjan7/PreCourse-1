// Time Complexity : O(1)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : Couldn't find a leetcode problem
// Any problem you faced while coding this : no

#include <bits/stdc++.h>
using namespace std;

// A structure to represent a stack
class StackNode
{
public:
    int data;
    StackNode *next;
};

StackNode *newNode(int data)
{
    StackNode *stackNode = new StackNode();
    stackNode->data = data;
    stackNode->next = NULL;
    return stackNode;
}

int isEmpty(StackNode *root)
{
    // Your code here
    return !root;
}

void push(StackNode **root, int data)
{
    // Your code here
    StackNode *node = newNode(data);
    node->next = *root;
    *root = node;
    cout << data << " pushed to stack\n";
}

int pop(StackNode **root)
{
    // Your code here
    if (isEmpty(*root))
    {
        cout << "Stack is empty\n";
        return -1;
    }
    StackNode *node = *root;
    *root = (*root)->next;
    int pop_val = node->data;
    delete node;
    return pop_val;
}

int peek(StackNode *root)
{
    // Your code here
    if (isEmpty(root))
    {
        cout << "Stack is empty\n";
        return -1;
    }
    return root->data;
}

int main()
{
    StackNode *root = NULL;

    push(&root, 10);
    push(&root, 20);
    push(&root, 30);

    cout << pop(&root) << " popped from stack\n";

    cout << "Top element is " << peek(root) << endl;

    return 0;
}