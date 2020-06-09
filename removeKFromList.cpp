ListNode<int> * removeKFromList(ListNode<int> *l, int k) {
    using namespace std;
    ListNode<int> *head = new ListNode<int>();
    head->next = l;
    ListNode<int> *pre = head, *now = l;
    while (now != nullptr) {
        ListNode<int> *next = now->next;
        if (now->value == k) {
            delete now;
            now = next;
            pre->next = now;
        } else {
            pre = now;
            now = now->next;
        }
    }
    return head->next;
}
