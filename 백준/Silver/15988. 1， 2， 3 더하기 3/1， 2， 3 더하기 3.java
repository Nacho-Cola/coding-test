import java.util.*;

// The main method must be in a class named "Main".
class Main {
    static int N;
    static long[] dp = new long[1000001];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i=4; i<1000001 ; i++) {
            dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) %1_000_000_009;
        }
        
        for (int i=0; i<T ; i++) {
            int target = sc.nextInt();
            System.out.println(dp[target]);
        }
    }
}
