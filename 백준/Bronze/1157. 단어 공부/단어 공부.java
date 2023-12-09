import java.util.*;
import java.io.*;
import java.math.*;
	


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		String s = br.readLine();
		s = s.toLowerCase();
		int x=0;
		int[] num = new int[26];
		int[] num2 = new int[26];
		for(int i =0;i<26;i++) {
			num[i] = 0; 
		}
		char[] c = new char[s.length()];
		for(int i =0;i<s.length();i++) {
			c[i] = s.charAt(i);
			num[c[i]-97]++;
			num2[c[i]-97]++;
		}
		
		Arrays.sort(num);
		for(int i =0;i<26;i++) {
			if(num2[i]==num[25]) {
				x=i;
				break;
			}
		}
		if(num[25]>num[24]) {System.out.println((char)(x+65));}
		else {System.out.println("?");}
		
	}
		
}

	