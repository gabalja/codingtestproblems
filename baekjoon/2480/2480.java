/*
주사위 세개 Java 풀이
https://doctcoder.tistory.com/entry/%EC%A3%BC%EC%82%AC%EC%9C%84-%EC%84%B8%EA%B0%9C-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      int b=sc.nextInt();
      int c=sc.nextInt();
      int result;
      if(a==b&&b==c) result=a*1000+10000;
      else if(a==b||a==c) result=a*100+1000;
      else if(b==c) result=b*100+1000;
      else result=Math.max(Math.max(a,b),c)*100;
      System.out.println(result);
  }
}
