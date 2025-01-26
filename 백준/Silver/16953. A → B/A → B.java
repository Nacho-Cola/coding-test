import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {

    public static int start;
    public static int target;
    public static boolean[] visited; 
    
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        start = sc.nextInt();
        target = sc.nextInt();

        System.out.println(bfs(start));
    }

    public static long bfs(int start) {
        Queue<long[]> queue = new LinkedList<>();
        queue.add(new long[] {start, 1});

        while (!queue.isEmpty()){
            long[] current = queue.poll();
            if (current[0] == target) return current[1];
            if (current[0] < target) {
                queue.add(new long[] {current[0]*2, current[1]+1});
                queue.add(new long[] {current[0]*10+1, current[1]+1});
            }     
        }
        return -1;
    }
    
}
