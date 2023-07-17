/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> set(to_delete.begin(), to_delete.end());

        queue<TreeNode*> q;
        vector<TreeNode*> res;

        q.push(root);
        if(set.count(root->val) == 0) res.push_back(root);

        while(!q.empty()){
            TreeNode * cur = q.front();
            q.pop();

            if(set.count(cur->val) != 0){
                if(cur->left && set.count(cur->left->val) == 0) res.push_back(cur->left);
                if(cur->right && set.count(cur->right->val) == 0) res.push_back(cur->right);
            }

            if(cur->left){
                q.push(cur->left);
                if(set.count(cur->left->val))    cur->left = nullptr;
            }
            if(cur->right){
                q.push(cur->right);
                if(set.count(cur->right->val))   cur->right = nullptr;
            }
        }
        return res;
        
    }
};