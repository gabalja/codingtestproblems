/*
최댓값 Java 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%93%EA%B0%92-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
      int maxs=-1;
      int idx=-1;
      for(int i=0;i<9;i++)
      {
      	int inp = sc.nextInt();
        if(inp>maxs)
        {
        	maxs=inp;
            idx=i+1;
        }
      }
      System.out.println(maxs);
      System.out.println(idx);
  }
}
