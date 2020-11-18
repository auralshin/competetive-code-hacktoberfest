import java.util.*;

public class KaratsubaAlgorithm {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Two  Numbers To multiply : ");
		long num1 = sc.nextLong();
		long num2 = sc.nextLong();
		System.out.println("The Prodct Of the Numbers is : " + karastuba(num1, num2));

	}

	public static long karastuba(long num1, long num2) {
		if (num1 < 10 && num2 < 10) {
			return num1 * num2;
		}

		int maxSize = Math.max((Long.toString(num1).length()), (Long.toString(num2).length()));

		int n = (int) Math.ceil(maxSize / 2.0);
		long p = (long) Math.pow(10, n);
		long a = (long) Math.floor(num1 / (double) p);
		long b = num1 % p;
		long c = (long) Math.floor(num2 / (double) p);
		long d = num2 % p;

		long a_c = karastuba(a, c);
		long b_d = karastuba(b, d);
		long e = karastuba(a + b, c + d) - a_c - b_d;

		return (long) (Math.pow(10 * 1L, 2 * n) * a_c + Math.pow(10 * 1L, n) * e + b_d);

	}

}
