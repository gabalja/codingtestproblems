/*
영수증 Java 풀이
https://doctcoder.tistory.com/entry/%EC%98%81%EC%88%98%EC%A6%9D
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int x=sc.nextInt();
      int n=sc.nextInt();
      for(int i=0;i<n;i++)
      {
          int a=sc.nextInt();
          int b=sc.nextInt();
          x-=a*b;
      }
      if(x==0) System.out.println("Yes");
      else System.out.println("No");
  }
}
