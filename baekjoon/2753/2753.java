/*
윤년 Java 풀이
https://doctcoder.tistory.com/entry/%EC%9C%A4%EB%85%84-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      if(a%4==0)
      {
      	if(a%400==0) System.out.println(1);
        else if(a%100!=0) System.out.println(1);
        else System.out.println(0);
      }
      else System.out.println(0);
  }
}
