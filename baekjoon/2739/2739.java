/*
구구단 Java 풀이
https://doctcoder.tistory.com/entry/%EA%B5%AC%EA%B5%AC%EB%8B%A8-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      for(int i=1;i<10;i++)
      {
      	System.out.println(a+" * "+i+" = "+(a*i));
      }
  }
}
