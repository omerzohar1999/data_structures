/**
 * FibonacciHeap
 *
 * An implementation of a Fibonacci Heap over integers.
 */
public class FibonacciHeap
{
    static int links = 0;
    static int cuts = 0;
    HeapNode min;
    HeapNode oldest_root;
    HeapNode newest_root;
    int size;
    int marked;
    int trees;
    public FibonacciHeap(){
        this.size = 0;
        this.marked = 0;
        this.trees = 0;

    }
   /**
    * public boolean isEmpty()
    *
    * Returns true if and only if the heap is empty.
    *
    */
    public boolean isEmpty()
    {
    	return this.size == 0;
    }

   /**
    * public HeapNode insert(int key)
    *
    * Creates a node (of type HeapNode) which contains the given key, and inserts it into the heap.
    * The added key is assumed not to already belong to the heap.
    *
    * Returns the newly created node.
    */
    public HeapNode insert(int key)
    {
        HeapNode to_insert = new HeapNode((key));
        if(this.isEmpty()){
            this.newest_root = to_insert;
            this.min = this.newest_root;
            this.oldest_root = this.min;
        }
        else{
            to_insert.setPrev(this.newest_root);
            this.newest_root.setNext(to_insert);
            if(to_insert.getKey() < this.min.getKey()){
                this.min = to_insert;
            }
        }
        this.size += 1;
        return to_insert;
    }

   /**
    * public void deleteMin()
    *
    * Deletes the node containing the minimum key.
    *
    */
    public void deleteMin()
    {
     	return; // should be replaced by student code

    }

   /**
    * public HeapNode findMin()
    *
    * Returns the node of the heap whose key is minimal, or null if the heap is empty.
    *
    */
    public HeapNode findMin()
    {
    	return this.min;
    }

   /**
    * public void meld (FibonacciHeap heap2)
    *
    * Melds heap2 with the current heap.
    *
    */
    public void meld (FibonacciHeap heap2)
    {
        if(!this.isEmpty() && !heap2.isEmpty()) {
            this.newest_root.setNext(heap2.oldest_root);
            heap2.oldest_root.setPrev(this.newest_root);
            this.newest_root = heap2.newest_root;
            this.newest_root.setNext(this.oldest_root);
            this.oldest_root.setPrev(this.newest_root);
            if(this.findMin().getKey() > heap2.findMin().getKey()){
                this.min = heap2.findMin();
            }
        }
        else if(!heap2.isEmpty()){
            this.min = heap2.findMin();
            this.oldest_root = heap2.oldest_root;
            this.newest_root = heap2.newest_root;
        }
        this.size += heap2.size();
        this.marked += heap2.marked;
        this.trees += heap2.trees;
    }

   /**
    * public int size()
    *
    * Returns the number of elements in the heap.
    *
    */
    public int size()
    {
    	return size;
    }

    /**
    * public int[] countersRep()
    *
    * Return an array of counters. The i-th entry contains the number of trees of order i in the heap.
    * (Note: The size of of the array depends on the maximum order of a tree.)
    *
    */
    public int[] countersRep()
    {
    	int[] arr = new int[100];
        HeapNode node = this.oldest_root;
        while(node != this.newest_root){
            arr[node.rank] += 1;
        }
        return arr;
    }

   /**
    * public void delete(HeapNode x)
    *
    * Deletes the node x from the heap.
	* It is assumed that x indeed belongs to the heap.
    *
    */
    public void delete(HeapNode x)
    {
        if(x != this.findMin()){
            this.decreaseKey(x, x.getKey() - this.findMin().getKey() + 1);  // To make x minimum
        }
        this.deleteMin();
    }

   /**
    * public void decreaseKey(HeapNode x, int delta)
    *
    * Decreases the key of the node x by a non-negative value delta. The structure of the heap should be updated
    * to reflect this change (for example, the cascading cuts procedure should be applied if needed).
    */
    public void decreaseKey(HeapNode x, int delta)
    {
    	return; // should be replaced by student code
    }

   /**
    * public int nonMarked()
    *
    * This function returns the current number of non-marked items in the heap
    */
    public int nonMarked()
    {
        return this.size - this.marked;
    }

   /**
    * public int potential()
    *
    * This function returns the current potential of the heap, which is:
    * Potential = #trees + 2*#marked
    *
    * In words: The potential equals to the number of trees in the heap
    * plus twice the number of marked nodes in the heap.
    */
    public int potential()
    {
        return this.trees - (2 * this.marked);
    }

   /**
    * public static int totalLinks()
    *
    * This static function returns the total number of link operations made during the
    * run-time of the program. A link operation is the operation which gets as input two
    * trees of the same rank, and generates a tree of rank bigger by one, by hanging the
    * tree which has larger value in its root under the other tree.
    */
    public static int totalLinks()
    {
    	return links; // should be replaced by student code
    }

   /**
    * public static int totalCuts()
    *
    * This static function returns the total number of cut operations made during the
    * run-time of the program. A cut operation is the operation which disconnects a subtree
    * from its parent (during decreaseKey/delete methods).
    */
    public static int totalCuts()
    {
    	return cuts; // should be replaced by student code
    }

     /**
    * public static int[] kMin(FibonacciHeap H, int k)
    *
    * This static function returns the k smallest elements in a Fibonacci heap that contains a single tree.
    * The function should run in O(k*deg(H)). (deg(H) is the degree of the only tree in H.)
    *
    * ###CRITICAL### : you are NOT allowed to change H.
    */
    public static int[] kMin(FibonacciHeap H, int k)
    {
        int[] arr = new int[100];
        return arr; // should be replaced by student code
    }

   /**
    * public class HeapNode
    *
    * If you wish to implement classes other than FibonacciHeap
    * (for example HeapNode), do it in this file, not in another file.
    *
    */
    public static class HeapNode{

    	public int key;
        int rank;
        boolean mark;
        HeapNode child;
        HeapNode next;
        HeapNode prev;
        HeapNode parent;
    	public HeapNode(int key) {
    		this.key = key;
            this.rank = 1;
            this.mark = false;
    	}

    	public int getKey() {
    		return this.key;
    	}

       public HeapNode getChild() {
           return child;
       }

       public HeapNode getNext() {
           return next;
       }

       public HeapNode getParent() {
           return parent;
       }

       public HeapNode getPrev() {
           return prev;
       }

       public int getRank() {
           return rank;
       }

       public boolean isMarked() {
           return mark;
       }

       public void setChild(HeapNode child) {
           this.child = child;
       }
       public void setParent(HeapNode parent) {
           this.parent = parent;
       }
       public void setNext(HeapNode next) {
           this.next = next;
       }
       public void setPrev(HeapNode prev) {
           this.prev = prev;
       }

       public void flipMark() {
           this.mark = !this.mark;
       }

       public boolean isLeaf(){
            return this.getChild() == null;
       }
       public boolean isRoot() {
           return this.getParent() == null;
       }
   }

   public static void main(String[] args){

   }
}
