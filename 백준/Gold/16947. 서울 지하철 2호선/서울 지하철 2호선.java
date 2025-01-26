import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    public static int N;
    public static boolean[] isCycle;
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
    
        N = sc.nextInt();
        
        for (int i=0 ; i<=N ; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i=0 ; i<N ; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        isCycle = new boolean[N + 1];
        for (int i=1; i<=N; i++){
            if (checkCycle(i,i,i)){
                break;
            }
        }
        
        int[] result = new int[N + 1];
        for (int i=1 ; i<=N ; i++) {
            if(!isCycle[i]) result[i] = bfs(i);
        }

        for (int i=1; i<=N ; i++) System.out.print(result[i] + " ");
    }


    static class Node {
        int num;
        int distanse;

        public Node (int num, int distanse) {
            this.num = num;
            this.distanse = distanse;
        }
    }

    public static int bfs(int node) {
        
        Queue<Node> queue = new LinkedList<>();
        boolean[] visited = new boolean[N + 1];
        queue.offer(new Node(node, 0));
        visited[node] = true;

        while(!queue.isEmpty()) {
            Node curr = queue.poll();
            if (isCycle[curr.num]) return curr.distanse;

            for (int next : graph.get(curr.num)) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(new Node(next, curr.distanse+1));
                }
            }
        }
        return 0;
    }
    

    public static boolean checkCycle(int prev, int node, int start) {
        isCycle[node] = true;

        for (int next : graph.get(node)) {
            if(!isCycle[next]) {
                if(checkCycle(node, next,start)) {
                    return true;
                }
            } else if (prev != next && next == start) {
                return true;
            }
        }
        isCycle[node] = false;
        
        return false;
    }
}
