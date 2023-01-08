/*
별 찍기 - 2 Java 풀이
https://doctcoder.tistory.com/entry/%EB%B3%84-%EC%B0%8D%EA%B8%B0-2-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      int t = sc.nextInt();
      for(int i=1;i<=t;i++)
      {
      	for(int j=t-i;j>0;j--)
        {
        	System.out.print(" ");
        }
        for(int k=0;k<i;k++)
        {
        	System.out.print("*");
        }
        System.out.println("");
      }
  }
}
