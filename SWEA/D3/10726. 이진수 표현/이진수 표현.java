import java.util.*;

class Solution
{
    static int inputNumber;
    static int lastNBit;
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
            lastNBit = sc.nextInt();
			inputNumber = sc.nextInt();
            
            lastNBit =  (1<<lastNBit)-1;
            if (( inputNumber & lastNBit ) == lastNBit) {
                System.out.printf("#%d ON\n", test_case);
            }
            else {
            	System.out.printf("#%d OFF\n", test_case);
            }


		}
	}
}