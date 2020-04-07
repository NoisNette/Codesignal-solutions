ListNode<int> * reverseNodesInKGroups(ListNode<int> * l, int k) {
    ListNode<int> *head = nullptr, *tail = nullptr, *curr = l;
    while (true) {
        if (!curr) {
            break;
        }
        ListNode<int> *g_head = curr, *g_tail = curr;
        curr = curr->next;
        ListNode<int> *tmp = curr;
        bool not_enough = false;
        for (int i = 1; i < k; i++) {
            if (!tmp) {
                not_enough = true;
                break;
            }
            tmp = tmp->next;
        }
        if (not_enough) {
        } else {
            for (int i = 1; i < k; i++) {
                if (!curr) {
                    break;
                }
                ListNode<int> *tmp = curr;
                curr = curr->next;
                tmp->next = g_head;
                g_head = tmp;
            }
            g_tail->next = nullptr;
        }
        if (!head) {
            head = g_head;
            tail = g_tail;
        } else {
            tail->next = g_head;
            tail = g_tail;
        }
        if (not_enough) {
            break;
        }
    }
    return head;
}
