/*
두 수 비교하기 Java 풀이
https://doctcoder.tistory.com/entry/%EB%91%90-%EC%88%98-%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      int b=sc.nextInt();
      if(a>b) System.out.println(">");
      else if(a<b) System.out.println("<");
      else System.out.println("==");
  }
}
