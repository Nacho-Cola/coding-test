import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();  
        int H = sc.nextInt(); 
        int T = sc.nextInt();  

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < N; i++) {
            maxHeap.add(sc.nextInt());
        }

        int count = 0; 
        while (T > 0) {
            int tallest = maxHeap.poll(); 

            if (tallest < H) { 
                System.out.println("YES");
                System.out.println(count);
                return;
            }

            if (tallest == 1) { 
                maxHeap.add(tallest);
                break;
            }

            maxHeap.add(tallest / 2);
            count++;
            T--;
        }

        if (maxHeap.peek() < H) {
            System.out.println("YES");
            System.out.println(count);
        } else {
            System.out.println("NO");
            System.out.println(maxHeap.poll()); 
        }
    }
}
