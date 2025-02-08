import java.util.*;


// The main method must be in a class named "Main".
class Main {
    
    static int N;
    static int[] tree;
    static boolean[] visited;
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        
        for (int test_case=0 ; test_case<tc ; test_case++) {
            N = sc.nextInt();
            tree = new int[N+1];  
            
            for (int i=1 ; i<N ; i++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                tree[b] = a ;
            }
            
            int a = sc.nextInt();
            int b = sc.nextInt();
            
            visited = new boolean[N+1];
            System.out.println(bfs(a,b));
        }
    }

    public static int bfs(int a, int b) {
        while (a != 0) {
            visited[a] = true;
            a = tree[a];
        }

        while (b != 0) {
            if (visited[b]) return b; 
            b = tree[b];
        }
        return b;
    }   
}