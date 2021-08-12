package com.company;
import java.util.*;
public class Main {

    public static void main(String[] args) {
        Scanner abc=new Scanner(System.in);
        int n;
        System.out.print("ENTER ARRAY SIZE:");
        n=abc.nextInt();
        int[] arr= new int[n];
        System.out.print("ENTER ARRAY ELEMENTS:");
        int i,j,temp;
        for(i=0;i<n;i++)
            arr[i]=abc.nextInt();
        for(i=1;i<n;i++)
        {
            temp=arr[i];
            for(j=i;j>0 && arr[j-1]>temp;j--)
            {
                arr[j]=arr[j-1];
            }
            arr[j]=temp;
        }
        for(i=0;i<n;i++)
            System.out.print(arr[i]+",");


    }
}

