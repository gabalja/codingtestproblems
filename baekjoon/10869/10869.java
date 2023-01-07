/*
사칙연산 Java 풀이
https://doctcoder.tistory.com/entry/%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args) 
	{
    Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
		System.out.println(a/b);
		System.out.println(a%b);
  }
}
