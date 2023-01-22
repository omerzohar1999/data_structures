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


    public HeapNode getFirst(){
        return this.newest_root;
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
            to_insert.setPrev(to_insert);
            to_insert.setNext(to_insert);
        }
        else{
            addNodeToTopList(to_insert); // also sets current newest_node & increases trees field
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
        HeapNode son = min.getChild(), position, firstSon = son;
        // "cut" all of min's children
        while (min.getChild() != null) { //changed
            position = son.getNext();
            removeNodeFromList(son);
            if(min == newest_root)
                newest_root = son;
            son.setPrev(min.getPrev());
            min.getPrev().setNext(son);
            son.setNext(min);
            min.setPrev(son);
            trees += 1;
            son = position;
        }
        // remove min, consolidate & find new min
        removeNodeFromList(min);
        min = findNewMin();
    }

    private HeapNode findNewMin(){
        consolidate();
        HeapNode node = newest_root, minNode = newest_root;
        int minKey = node.getKey();
        node = node.getNext();
        while(node != newest_root) { // changed
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
        // determines node1 as the node with the smaller key, and node as the node with the bigger key
        if (node1.getKey() > node2.getKey()) {
            HeapNode node = node1;
            node1 = node2;
            node2 = node;
        }
        // make node2 son of node1 - changed whole part
        removeNodeFromList(node2);
        if (node1.getChild() != null) {
            node2.setNext(node1.getChild());
            node2.setPrev(node1.getChild().getPrev());
            if(node1.getChild().getPrev() == node1.getChild()) {
                node2.setNext(node1.getChild());
                node1.getChild().setNext(node2);
            }
            else
                node1.getChild().getPrev().setNext(node2);
            node1.getChild().setPrev(node2);
        }
        else {
            node2.setPrev(node2);
            node2.setNext(node2);
        }
        node1.setChild(node2);
        node2.setParent(node1);
        // maintain fields: marked, rank, links
        unmark(node2);
        node1.setRank(node1.getRank()+1);
        links++;
        // return the higher node to put in the array
        return node1;
    }

    void consolidate(){
        HeapNode[] nodesMapping = new HeapNode[size+1];
        HeapNode node = newest_root, position;
        boolean flag;
        nodesMapping[node.getRank()] = node; // changed - added
        node = node.getNext(); // changed - added
        while (node != newest_root) { // changed
            // determines next position - changed - removed rows
            position = node.getNext();
            flag = position == newest_root;
            // links two roots with the same rank, if needed
            int i = node.getRank();
            while (nodesMapping[i] != null) {
                node = link(node, nodesMapping[i]);
                nodesMapping[i] = null;
                i = node.getRank();
            }
            // adds current root(linked or not) to the array & goes to next position
            nodesMapping[i] = node;
            if(flag) { break; }
            node = position;
        }
        oldest_root = null;
        newest_root = null;
        HeapNode lastAdded = new HeapNode(0);
        for(int i = 0; i<nodesMapping.length; i++)
        {
            if(nodesMapping[i] != null){
                if(newest_root == null){
                    newest_root = nodesMapping[i];
                    newest_root.setNext(newest_root);
                    newest_root.setPrev(newest_root);
                    lastAdded = newest_root;
                }
                else{
                    lastAdded.setNext(nodesMapping[i]);
                    nodesMapping[i].setPrev(lastAdded);
                    lastAdded = nodesMapping[i];
                    lastAdded.setNext(newest_root);
                    newest_root.setPrev(lastAdded);
                }
                oldest_root = lastAdded;
            }
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
            this.newest_root.setPrev(heap2.oldest_root);
            heap2.oldest_root.setNext(this.newest_root);
            heap2.newest_root.setPrev(this.oldest_root);
            this.oldest_root.setNext(heap2.newest_root);
            oldest_root = heap2.oldest_root;
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
        if(this.size() == 0){
            return new int[0];
        }
        int size = 0;
        HeapNode pointer = this.newest_root;
        boolean beforeFirst = true;
        while(pointer != this.newest_root || beforeFirst){
            beforeFirst = false;
            if(pointer.getRank()>size)
                size=pointer.getRank();
            pointer = pointer.getNext();
        }
        beforeFirst = true;
        int[] arr = new int[size+1];
        HeapNode node = this.newest_root;
        while(node != this.newest_root || beforeFirst){
            beforeFirst = false;
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
                oldest_root = x.getPrev();
            }
            if (x == newest_root) {
                newest_root = x.getNext();
            }
            trees--;
            }
        else {
            HeapNode parent = x.getParent();
            parent.setRank(parent.getRank() - 1);
            if (x != x.getNext()){ // changed
                parent.setChild(x.getNext()); // changed
            }
            else{ // changed - added
                parent.setChild(null);
            }
        }
        // remove x from origin list
        x.getNext().setPrev(x.getPrev()); // changed - do anyway
        x.getPrev().setNext(x.getNext()); // changed - do anyway
        // detach x
        x.setParent(null);
        x.setNext(x); // changed
        x.setPrev(x); // changed
    }

    private void unmark(HeapNode x) {
        if(x.isMarked()) {
            x.flipMark();
            marked--;
        }
    }

    private void addNodeToTopList(HeapNode x){
        newest_root.setPrev(x);
        x.setNext(newest_root);
        x.setPrev(oldest_root);
        oldest_root.setNext(x);
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

    private void insertSons(HeapNode node){
        HeapNode son = node.getChild(), internalNode;
        internalNode = insert(son.getKey()); // changed - added
        internalNode.setPointer(son); // changed - added
        son = son.getNext(); // changed - added
        while(son != node.getChild()) { // changed
            internalNode = insert(son.getKey());
            internalNode.setPointer(son);
            son = son.getNext();
        }
    }


     /**
    * public static int[] kMin(FibonacciHeap H, int k)
    * @pre: trees == 1
    * This static function returns the k smallest elements in a Fibonacci heap that contains a single tree.
    * The function should run in O(k*deg(H)). (deg(H) is the degree of the only tree in H.)
    *
    * ###CRITICAL### : you are NOT allowed to change H.
    */
    public static int[] kMin(FibonacciHeap H, int k)
    {
        if(k==0)
            return new int[0];
        if (k > H.size()) { k = H.size(); }
        FibonacciHeap minH = new FibonacciHeap();
        int[] arr = new int[k];
        HeapNode tree = H.findMin(), node = tree;
        minH.insert(node.getKey());
        minH.findMin().setPointer(node);
        for (int i=0; i < k; i++){
            arr[i] = minH.findMin().getKey();
            if(node.getChild() != null)
                minH.insertSons(node);
            minH.deleteMin();
            node = minH.findMin();
            if(node != null)
                node = node.getPointer();
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
        HeapNode pointer;

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

       HeapNode getPointer(){
           return pointer;
       }

       void setPointer(HeapNode pointer) {
           this.pointer = pointer;
       }

       public void flipMark() {
           this.mark = !this.mark;
       }

       public void setRank(int val) { this.rank = val; }

       public boolean isLeaf(){
            return this.getChild() == null;
       }
       public boolean isRoot() {
           return this.getParent() == null;
       }

       public boolean getMarked(){ return this.mark; }

   }
}
