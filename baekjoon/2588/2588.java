/*
곱셈 Java 풀이
https://doctcoder.tistory.com/entry/%EA%B3%B1%EC%85%88-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      int b=sc.nextInt();
      System.out.println(a*(b%10));
      System.out.println(a*((b/10)%10));
      System.out.println(a*(b/100));
      System.out.println(a*b);
  }
}
