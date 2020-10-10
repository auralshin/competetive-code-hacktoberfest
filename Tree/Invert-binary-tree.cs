/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Invert {
    public TreeNode InvertTree(TreeNode root) {
        if(root != null)
        {
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
            if(root.left != null)
            {
                root.left = InvertTree(root.left);
            }
            if(root.right != null)
            {
                root.right = InvertTree(root.right);
            }
        }
        return root;
    }
}
