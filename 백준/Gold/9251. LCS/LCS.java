import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static int[][] dp;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();

        dp = new int[str1.length()+1][str2.length()+1];
        for (int i=1 ; i<=str1.length() ; i++) {
            for (int j=1 ; j<=str2.length() ; j++){
                if (str1.charAt(i-1) == str2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]) ;
                }
            }
        }
        System.out.print(dp[str1.length()][str2.length()]);
    }
}