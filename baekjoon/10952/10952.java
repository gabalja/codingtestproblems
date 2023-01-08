/*
A+B - 5 Java 풀이
https://doctcoder.tistory.com/entry/AB-5-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      while(true)
      {
      	int a = sc.nextInt();
        int b = sc.nextInt();
        if(a==0&&b==0) break;
        System.out.println(a+b);
      }
  }
}
