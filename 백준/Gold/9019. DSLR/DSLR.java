import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static int test_case;
    public static int target;
    public static int start;
    public static boolean[] visited;
    
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        test_case = sc.nextInt();
        for (int i=0 ; i<test_case ; i++) {
            start = sc.nextInt();
            target = sc.nextInt();
            visited = new boolean[10000];
            System.out.println(bfs(start));
        }
       
    }

    public static class Node {
        int value;
        String path;
        public Node (int value, String path) {
            this.value = value;
            this.path = path;
        }
    }

    public static String bfs(int start) {
        Queue<Node> queue = new LinkedList<>(); 
        queue.add(new Node(start, ""));
        
        while (!queue.isEmpty()) {
            Node currnet = queue.poll();
            if (currnet.value == target) return currnet.path;

            int Dvalue = currnet.value * 2 % 10000;
            if (!visited[Dvalue]) {
                visited[Dvalue] = true;
                queue.add(new Node(Dvalue, currnet.path + 'D'));
            }
            
            int Svalue = (currnet.value == 0) ? 9999 : currnet.value -1;
            if (!visited[Svalue]) {
                visited[Svalue] = true;
                queue.add(new Node(Svalue, currnet.path + 'S'));
            }
            int Lvalue = (currnet.value % 1000) * 10 + (currnet.value / 1000);
            if (!visited[Lvalue]) {
                visited[Lvalue] = true;
                queue.add(new Node(Lvalue, currnet.path + 'L'));
            }
            int Rvalue = (currnet.value / 10) + (currnet.value % 10) *1000;
             if (!visited[Rvalue]) {
                visited[Rvalue] = true;
                queue.add(new Node(Rvalue, currnet.path + 'R'));
            }
        }
        return "";
    }
}
