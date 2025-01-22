import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static ArrayList<ArrayList<Integer>> graph;
    public static int[] color;
    public static boolean ret;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int tc = sc.nextInt();
        
        for (int taseCase=0 ; taseCase<tc ; taseCase++) {
        
            int V = sc.nextInt();
            int E = sc.nextInt();
            
            graph = new ArrayList<>();
            color = new int[V+1];

            for (int i=0 ; i<=V ; i++) {
                graph.add(new ArrayList<>());
            }
            
            for (int i=0 ; i<E ; i++) {
                int a = sc.nextInt();    
                int b = sc.nextInt();    
                graph.get(a).add(b);
                graph.get(b).add(a);
            }

            for (int i=1 ; i<=V ; i++){
                if (color[i] == 0){
                    ret = isBipartiteGraph(i, 1);
                }
                if (!ret) break;
            }
            if (ret) {
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
            
                
        }
    }
    public static boolean isBipartiteGraph(int start, int nodeColor) {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(start);
        color[start] = nodeColor;

        while(!queue.isEmpty()) {
            int curNode = queue.poll();
            for (int node : graph.get(curNode)) {
                if (color[node] == color[curNode]) return false;
                if (color[node] == 0) {
                    color[node] = color[curNode] * -1;
                    queue.add(node);
                }
            }
        }
        return true;
    }
}