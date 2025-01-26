import java.util.*;

class Main {
    public static long[] DP ;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for(int testCase=0 ; testCase<tc ; testCase++) {
            int L = sc.nextInt();
            DP = new long[L+1];
            DP[0] = 1;
            for (int i=2 ; i<=L ; i+=2) {
                for (int j=0 ; j<=i-2 ; j++) {
                    DP[i] += (DP[j] * DP[i-j-2])%1000000007;
                    DP[i] %= 1000000007;
                }
            }
            
            System.out.println(DP[L]);
        }
    }
}

