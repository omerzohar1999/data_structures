import java.lang.Math;

public class Theory {
    public static FibonacciHeap runHeapQ1(int e) {
        FibonacciHeap heap = new FibonacciHeap();
        int m = (int) Math.pow(2,e);
        for(int i=m-1; i >= -1; i--) {
            heap.insert(m);
        }
        heap.deleteMin();
        for(int i=e; i>=1; i--){
            heap.decreaseKey(null, m+1); // must understand with node will the m - (int) Math.pow(2,i) key
        }
        return heap;
    }

    public static void printQ1() {
        int prevLinks = 0, prevCuts = 0, e;
        long startTime, endTime;
        FibonacciHeap heap;
        System.out.println("m,Run-Time (ms),totalLinks,totalCuts,Potential");
        for(int i=1; i <=4; i++) {
             e = 4*i;
            prevLinks = FibonacciHeap.totalLinks();
            prevCuts = FibonacciHeap.totalCuts();
            startTime = System.currentTimeMillis();
            heap = runHeapQ1(e);
            endTime = System.currentTimeMillis();
            System.out.println("2^" + e + "," + (endTime - startTime) + "," + (FibonacciHeap.totalLinks() - prevLinks)
                         + "," + (FibonacciHeap.totalCuts() - prevCuts) + "," + heap.potential());
        }
    }

    public static FibonacciHeap runHeapQ2(int m) {
        FibonacciHeap heap = new FibonacciHeap();
        for (int i=0; i <= m; i++) {
            heap.insert(i);
        }
        for(int i=1; i <= (3*m/4); i++) {
            heap.deleteMin();
        }
        return heap;
    }

    public static void printQ2(){
        int prevLinks = 0, prevCuts = 0, m;
        long startTime, endTime;
        FibonacciHeap heap;
        System.out.println("m,Run-Time (ms),totalLinks,totalCuts,Potential");
        for(int i=6; i <=14; i += 2) {
            m = (int)Math.pow(3,i) - 1;
            prevLinks = FibonacciHeap.totalLinks();
            prevCuts = FibonacciHeap.totalCuts();
            startTime = System.currentTimeMillis();
            heap = runHeapQ1(m);
            endTime = System.currentTimeMillis();
            System.out.println(m + "," + (endTime - startTime) + "," + (FibonacciHeap.totalLinks() - prevLinks)
                    + "," + (FibonacciHeap.totalCuts() - prevCuts) + "," + heap.potential());
        }
    }

    public static void main(String[] args) {
        printQ1();
        //printQ2();
    }
}
