import java.util.*;
import java.lang.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
	java.io.BufferedReader r = new java.io.BufferedReader (new java.io.InputStreamReader (System.in));
    String s;
    while (!(s=r.readLine()).equals("0")){
    	int result = Integer.parseInt(s);
    	result = ((result*(result+1)*(result*2+1))/6);
    	System.out.println(result);
    } 
	}
}