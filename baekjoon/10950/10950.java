/*
A+B - 3 Java 풀이
https://doctcoder.tistory.com/entry/AB-3-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int t=sc.nextInt();
      for(int i=0;i<t;i++)
      {
          int a=sc.nextInt();
          int b=sc.nextInt();
          System.out.println((a+b));
      }
  }
}
