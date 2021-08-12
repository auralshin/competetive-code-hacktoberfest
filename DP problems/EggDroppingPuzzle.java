class DropEgg { 
  
  
    /* Find minimum trials
   with e eggs and f floors */
    static int dropEgg(int e, int f) 
    { 
        
        int dp[][] = new int[e + 1][f + 1];  
        int trial = 0; 
  
        //base case
        /* If floor 1 one then 1 trial and
         0 trial for 0 floor*/
        
        for (int i = 1; i <= e; i++) { 
            dp[i][1] = 1; 
            dp[i][0] = 0; 
        } 
        
        //base case
        /* for f floorsandd 1 egg
            number of trials is f*/
        for (j = 1; j <= f; j++) 
            dp[1][j] = j; 
  
        
        for (int i = 2; i <= e; i++) { 
            for (int j = 2; j <= f; j++) { 
                dp[i][j] = Integer.MAX_VALUE; 
                for (int x = 1; x <= j; x++) { 
                    trial = 1 + Math.max( 
                                  dp[i - 1][x - 1], 
                                  dp[i][j - x]); 
                    if (trial < dp[i][j]) 
                        dp[i][j] = trial; 
                } 
            } 
        } 
  
        return dp[n][k]; 
    } 
  
    /* Driver program to  print output*/
    public static void main(String args[]) 
    { 
        int e = 5;
        int f = 12; 
        System.out.println("Min Number of trials" + dropEgg(e,f)); 
    } 
} 
