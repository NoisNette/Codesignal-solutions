int sum;
void dfs(Tree<int> *t){
    if (t==NULL) return;
    if (t->left!=NULL && t->left->left==NULL && t->left->right==NULL){
        sum+=t->left->value;
    }
    dfs(t->left);
    dfs(t->right);
}
int leftLeavesSum(Tree<int> * t) {
    sum=0;
    dfs(t);
    return sum;
}
