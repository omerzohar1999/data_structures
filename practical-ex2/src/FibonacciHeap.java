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
        min = null;
        oldest_root = null;
        newest_root = null;

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
            this.trees = 1;
        }
        else{
            addNodeToTopList(to_insert); // also sets current newest_node & increases trees field
            //to_insert.setPrev(this.newest_root);
            //this.newest_root.setNext(to_insert);
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
        if (size <= 1) {
            this.size = 0;
            this.marked = 0;
            this.trees = 0;
            min = null;
            oldest_root = null;
            newest_root = null;
            return;
        }
        size --;
        HeapNode son = min.getChild(), position;
        while (son != null) {
            position = son.getNext();
            removeNodeFromList(son);
            addNodeToTopList(son);
            son = position;
        }
        removeNodeFromList(min);
        min = findNewMin();
    }

    private HeapNode findNewMin(){
        consolidate();
        HeapNode node = oldest_root, minNode = oldest_root;
        int minKey = node.getKey();
        node = node.getNext();
        while(node != null) {
            if (node.getKey() < minKey) {
                minKey = node.getKey();
                minNode = node;
            }
            node = node.getNext();
        }
        return minNode;
    }

    /**
     * @pre: node1.getRank() == node2.getRank()
     * @pre: node.isRoot() && node2.isRoot()
     * @param node1
     * @param node2
     */
    protected HeapNode link(HeapNode node1, HeapNode node2) {
        if (node1.getKey() > node2.getKey()) {
            HeapNode node = node1;
            node1 = node2;
            node2 = node;
        }
        removeNodeFromList(node2);
        // make node2 son of node1
        if (node1.getChild() != null) {
            node1.getChild().setPrev(node2);
        }
        node2.setNext(node1.getChild());
        node2.setPrev(null);
        node1.setChild(node2);
        node2.setParent(node1);
        // maintain fields: marked, rank, links
        unmark(node2);
        node1.setRank(node1.getRank()+1);
        links++;
        return node1;
    }

    void consolidate(){
        HeapNode[] nodesMapping = new HeapNode[(int) (Math.log(size) / Math.log(2)) + 1];
        HeapNode node = oldest_root, position;
        while (node != null) {
            position = node.getNext();
            if(position == null){
                newest_root = node;
            }
            int i = node.getRank();
            while (nodesMapping[i] != null) {
                node = link(node, nodesMapping[i]);
                nodesMapping[i] = null;
                i = node.getRank();
            }
            nodesMapping[i] = node;
            node = position;
        }
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
        while(node != null){
            arr[node.getRank()] += 1;
            node = node.getNext();
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
        // set key according to delta
        x.setKey(x.getKey() - delta);
        // maintain min field
        if (x.getKey() < min.getKey()) {
            min = x;
        }
        // maintain heap invariant
        if ((!x.isRoot()) && x.getKey() < x.getParent().getKey()){
            cascadingCut(x);
        }
    }

    private void removeNodeFromList(HeapNode x){
        unmark(x);
        // take care of parent, if exist
        if (x.isRoot()) {
            if (x == oldest_root) {
                oldest_root = x.getNext();
            }
            if (x == newest_root) {
                newest_root = x.getPrev();
            }
            trees--;
            }
        else {
            HeapNode parent = x.getParent();
            parent.setRank(parent.getRank() - 1);
            if (!x.hasPrev()){
                parent.setChild(x.getNext());
            }
        }
        // remove x from origin list
        if(x.hasPrev()) {
            x.getPrev().setNext(x.getNext());
        }
        if (x.hasNext()){
            x.getNext().setPrev(x.getPrev());
        }
        // detach x
        x.setParent(null);
        x.setNext(null);
        x.setPrev(null);
    }

    private void unmark(HeapNode x) {
        if(x.isMarked()) {
            x.flipMark();
            marked--;
        }
    }

    private void addNodeToTopList(HeapNode x){
        newest_root.setNext(x);
        x.setPrev(newest_root);
        x.setNext(null);
        newest_root = x;
        this.trees++;
    }

    protected void cut(HeapNode x){
        cuts ++;
        removeNodeFromList(x);
        addNodeToTopList(x);
    }

    /**
     * @pre: !min.isMarked()
     * @param son
     */
    void cascadingCut(HeapNode son){
        HeapNode parent = son.getParent();
        cut(son);
        if(parent.isRoot()) {
            return;
        }
        if(parent.isMarked()){
            cascadingCut(parent);
        }
        else {
            parent.flipMark();
            marked ++;
        }
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
        return this.trees + (2 * this.marked);
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
    	return links;
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
    	return cuts;
    }

    private void copyHeapRec(FibonacciHeap copy, HeapNode node, int depth) {
        if (depth == 0) {
            return;
        }
        while (node != null) {
            copy.insert(node.getKey());
            copyHeapRec(copy, node.getChild(), depth--);
            node = node.getNext();
        }
    }

    FibonacciHeap copyHeap(int maxLevel) {
        FibonacciHeap copy = new FibonacciHeap();
        copyHeapRec(copy, min, maxLevel);
        return copy;
    }

    public FibonacciHeap copy() {
        return copyHeap(min.getRank());
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
        if (k >= H.size()) {
            k = H.size();
        }
        HeapNode tree = H.min;
        // determine number of levels
        int maxLevelToCopy = tree.findMaxLevelToCopy(k);
        // add top levels leaves to new Heap
        FibonacciHeap minH = H.copyHeap(maxLevelToCopy);
        // commit deleteMin k times into array
        int[] arr = new int[k];
        for (int i=0; i < arr.length; i++) {
            arr[i] = minH.findMin().getKey();
            minH.deleteMin();
        }
        return arr;
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
            this.rank = 0;
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

       public void setKey(int value){ this.key = value; }

       public void flipMark() {
           this.mark = !this.mark;
       }

       public void setMark(boolean val) { this.mark = val; }

       public void setRank(int val) { this.rank = val; }

       public boolean isLeaf(){
            return this.getChild() == null;
       }
       public boolean isRoot() {
           return this.getParent() == null;
       }

       public boolean hasNext() { return this.next != null; }

       public boolean hasPrev() { return this.prev != null; }

       private static int nChooseK(int n, int k) {
            int dif = n - k, nFactorial = 1, kFactorial = 1, difFactorial = 1;
            for (int i=2; i <=n; i++) {
                nFactorial = nFactorial * i;
                if(i <= k) {
                    kFactorial = kFactorial * i;
                }
                if(i <= dif) {
                    difFactorial = difFactorial * i;
                }
            }
            return nFactorial / (kFactorial * difFactorial);
       }

       /**
        * @pre: this.isRoot()
        * @post: $ret >=0 && $ret < height (== rank)
        * @post: level > rank --> $ret = calculateSizeOfTopLevels(rank)
        * @param k
        * @return int sum == minimal depth that surely contains k node within  above
        */
       int findMaxLevelToCopy(int k) {
           int sum = 0;
            for (int i=0; i < k; i++) {
                sum = sum + nChooseK(k,i);
                if (sum >= k) {
                    return i - 1;
                }
            }
            return rank - 1;
       }

   }

   public static void main(String[] args){

   }
}
