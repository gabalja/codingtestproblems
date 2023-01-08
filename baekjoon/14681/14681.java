/*
사분면 고르기 Java 풀이
https://doctcoder.tistory.com/entry/%EC%82%AC%EB%B6%84%EB%A9%B4-%EA%B3%A0%EB%A5%B4%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      int b=sc.nextInt();
      if(a>0&&b>0) System.out.println(1);
      if(a<0&&b>0) System.out.println(2);
      if(a<0&&b<0) System.out.println(3);
      if(a>0&&b<0) System.out.println(4);
  }
}
