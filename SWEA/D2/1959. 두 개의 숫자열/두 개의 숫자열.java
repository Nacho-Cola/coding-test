import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
            int N = sc.nextInt();
            int M = sc.nextInt();
            
            int[] N_array = new int [N];
            int[] M_array = new int [M];
            
            for(int i = 0 ; i < N; i++ ){
            	N_array[i] = sc.nextInt();
            }

            for(int i = 0 ; i < M; i++ ){
            	M_array[i] = sc.nextInt();
            }
            
			if (N > M){
           		int[] temp = N_array;
                N_array = M_array;
                M_array = temp;
                int temp_size = N;
                N = M;
                M = temp_size;
            }
            
            int max_value = Integer.MIN_VALUE;
            for(int i = 0 ; i <= M - N ; i++){
                int sum = 0;
           		for(int j = 0; j < N; j++){
                	sum += M_array[i+j] * N_array[j];
                }
                max_value = Math.max(sum, max_value);
            }
            
			System.out.println("#"+test_case+" "+max_value);
		}
	}
}