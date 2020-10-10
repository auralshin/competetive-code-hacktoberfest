//Question: Given an integer N, find and return the count of minimum numbers required to represent N as a sum of squares.
import java.util.*;
public class N_sumofSQuares{
	
	public static int minSum(int n) {
        if (n <= 3) 
            return n; 
        int dp[] = new int[n + 1]; 
        dp[0] = 0; 
        dp[1] = 1; 
        dp[2] = 2; 
        dp[3] = 3; 
        for (int i = 4; i <= n; i++) { 
            dp[i] = i; 
            for (int x = 1; x <= Math.ceil(Math.sqrt(i)); x++) { 
                int temp = x * x; 
                if (temp > i) 
                    break; 
                else
                    dp[i] = Math.min(dp[i], 1 + dp[i - temp]); 
            } 
        }
        return dp[n];
    }

public static void main(String[] args){
			Scanner s=new Scanner(System.in);
            int n = s.nextInt();
            System.out.println(minSum(n));
    }
}

//Contributed By:sumitav