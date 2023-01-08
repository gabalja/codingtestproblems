/*
최소, 최대 Java 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EC%86%8C-%EC%B5%9C%EB%8C%80-%ED%92%80%EC%9D%B4
*/
import java.util.Scanner;

class Main 
{
  public static void main(String[] args)
  {
      Scanner sc = new Scanner(System.in);
			int n = sc.nextInt();
			int maxnum=-2000000;
			int minnum=2000000;
			for(int i=0;i<n;i++)
			{
				int inp = sc.nextInt();
				if(inp>maxnum) maxnum=inp;
				if(inp<minnum) minnum=inp;
			}
			System.out.println(minnum+" "+maxnum);
  }
}
