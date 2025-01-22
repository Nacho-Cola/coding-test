import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static int[] graph;
    public static boolean[] visited;
    public static boolean[] done;
    public static int count; 
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        int tc = sc.nextInt();
        
        for (int testCase=0 ; testCase< tc ; testCase++) {
            int N = sc.nextInt();
            graph = new int[N+1] ;
            visited = new boolean[N+1];
            done = new boolean[N+1];
            count = 0;
            
            for (int i=1 ; i<=N ; i++) {
                int a = sc.nextInt();
                graph[i] = a;
            }

            for (int i=1 ; i<=N ; i++){
                if (!done[i]) {findCycle(i);}
            }
            
            System.out.println(N-count);
            
        }
       
    }

    public static void findCycle(int start){
        if(done[start]) return;
        int node = graph[start];
        
        if(visited[start]){
            done[start] = true;
            count++;
        }
        
        visited[start] = true;
        findCycle(node);
        done[start] = true;
        visited[start] = false;
    }
}