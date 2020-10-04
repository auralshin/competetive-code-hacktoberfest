import java.io.*;
import java.sql.SQLOutput;
import java.util.*;
public class karat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter first number");
        String a = sc.nextLine();
        System.out.println("enter second number");
        String b = sc.nextLine();
        String product = multiply(a,b);
        System.out.println(product);

    }

    public static String multiply(String a , String b)
    {
        String p = "";
        int l1 = a.length();
        int l2 = b.length();
        int n=0;
        if(l1>l2)
        {
            for(int i=0;i<l1-l2;i++)
            {
              b = '0' + b;

            }
            n=l1;
        }
        else
        {

            for(int i=0;i<l2-l1;i++)
            {
                a = '0' + a;

            }
            n=l2;
        }

        //System.out.println(a);
        if(n==1)
        {
            p = Integer.toString((a.charAt(0)-'0')*(b.charAt(0)-'0'));
            return p;
        }

        else
        {
            String al = a.substring(0,n/2);
            String ar = a.substring(n/2,n);
            String bl = b.substring(0,n/2);
            String br = b.substring(n/2,n);
            String x1 = multiply(al,bl);
            String x2 = multiply(al,br);
            String x3 = multiply(ar,bl);
            String x4 = multiply(ar,br);
            System.out.println(x4);
            for(int i=0;i<n;i++)
            {
                x1 = x1 + '0';
            }
            System.out.println(x1);
            String p2=add(x2 , x3);
            System.out.println(p2);
            for(int i=0;i<n/2;i++)
            {
                p2 = p2 + '0';
            }
            System.out.println(p2);
            String pr = add(x1, p2);
            System.out.println(pr);
            p = add(pr, x4);

        }
        return p;
    }

    public static String add(String a , String b)
    {
        int n=0;
        int l1 = a.length();
        int l2 = b.length();
        if(l1>l2)
        {
            for(int i=0;i<l1-l2;i++)
            {
                b = '0' + b;
            }
            n=l1;
        }
        else
        {
            for(int i=0;i<l2-l1;i++)
            {
                a = '0' + a;
            }
            n=l2;
        }
        int sum=0,carry=0;
        String s = "";
        for(int i=n-1;i>=0;i--)
        {
            sum = (a.charAt(i)-'0') + (b.charAt(i)-'0')+carry;
            carry = sum/10;
            sum = sum%10;
            s = s + (char)(sum +'0');
        }
        if(carry >0)
        {
            s += (char)(carry + '0');
        }
        s = new StringBuilder(s).reverse().toString();
        return s;

    }


}