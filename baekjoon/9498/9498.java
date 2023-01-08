/*
시험 성적 Java 풀이
https://doctcoder.tistory.com/entry/%EC%8B%9C%ED%97%98-%EC%84%B1%EC%A0%81-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int a=sc.nextInt();
      if(a>89) System.out.println("A");
      else if(a>79) System.out.println("B");
      else if(a>69) System.out.println("C");
      else if(a>59) System.out.println("D");
      else System.out.println("F");
  }
}
