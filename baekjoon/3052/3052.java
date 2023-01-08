/*
나머지 Java 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%A8%B8%EC%A7%80-%ED%92%80%EC%9D%B4-1
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      int[] arr=new int[42];
      int cnt=0;
      for(int i=0;i<10;i++)
      {
      	int inp = sc.nextInt();
        arr[inp%42]++;
      }
      for(int i=0;i<42;i++)
      {
      	if(arr[i]!=0) cnt++;
      }
      System.out.println(cnt);
  }
}
