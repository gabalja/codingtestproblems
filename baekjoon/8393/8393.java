/*
합 Java 풀이
https://doctcoder.tistory.com/entry/%ED%95%A9-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int n=sc.nextInt();
      int result=0;
      for(int i=0;i<=n;i++) result+=i;
      System.out.println(result);
  }
}
