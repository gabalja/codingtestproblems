/*
알람 시계 Java 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%EB%9E%8C-%EC%8B%9C%EA%B3%84-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int hour=sc.nextInt();
      int minute=sc.nextInt();
      if(minute<45)
      {
          hour--;
          minute+=60;
      }
      if(hour<0) hour+=24;
      minute-=45;
      System.out.println(hour+" "+minute);
  }
}
