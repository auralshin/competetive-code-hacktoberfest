import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        input.nextLine();
        
        tests:
        for(int t = 0; t < T; t++)
        {
            String s = input.nextLine();
            int deletions = 0;
            int currentCount = 1;
            for(int i = 1; i < s.length(); i++)
            {
                if(s.charAt(i) != s.charAt(i-1))
                {
                    deletions += currentCount - 1;
                    currentCount = 1;
                    continue;
                }
                currentCount++;
            }
            deletions += currentCount - 1;
            System.out.println(deletions);
        }
    }
}
