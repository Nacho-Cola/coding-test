import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int C = sc.nextInt();

        for (int i = 0; i < C; i++) {
            int N = sc.nextInt(); 
            int[] scores = new int[N];

            int sum = 0;
            for (int j = 0; j < N; j++) {
                scores[j] = sc.nextInt();
                sum += scores[j];
            }

            double avg = sum / N;
            int count = 0;

            for (int score : scores) {
                if (score > avg) {
                    count++;
                }
            }

            double percentage = (count * 100.0) / N;
            System.out.printf("%.3f%%\n", percentage);
        }
    }
}
