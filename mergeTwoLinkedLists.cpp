ListNode<int> * mergeTwoLinkedLists(ListNode<int> * l1, ListNode<int> * l2) {
    using namespace std;
    ListNode<int> *head = new ListNode<int>(), *curr = head;
    while (l1 && l2) {
        if (l1->value < l2->value) {
            curr->next = l1;
            curr = curr->next;
            l1 = l1->next;
        } else {
            curr->next = l2;
            curr = curr->next;
            l2 = l2->next;
        }
    }
    while (l1) {
        curr->next = l1;
        curr = curr->next;
        l1 = l1->next;
    }
    while (l2) {
        curr->next = l2;
        curr = curr->next;
        l2 = l2->next;
    }
    ListNode<int> *tmp = head;
    head = head->next;
    delete tmp;
    return head;
}
