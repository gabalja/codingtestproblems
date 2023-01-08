/*
오븐 시계 Java 풀이
https://doctcoder.tistory.com/entry/%EC%98%A4%EB%B8%90-%EC%8B%9C%EA%B3%84-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc=new Scanner(System.in);
      int hour=sc.nextInt();
      int minute=sc.nextInt();
      int time=sc.nextInt();
      minute+=time;
      while(minute>=60)
      {
          minute-=60;
          hour++;
          if(hour>=24) hour-=24;
      }
      System.out.println(hour+" "+minute);
  }
}
