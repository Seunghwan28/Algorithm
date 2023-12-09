import java.util.*;
import java.io.*;
import java.math.*;
	


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner scanner = new Scanner(System.in); 
		
		String s = br.readLine();
		int[] num = new int[26];
		for(int i =0;i<26;i++) {
			num[i]=-1;
		}
		char[] c = new char[s.length()];
		for(int i =0;i<s.length();i++) {
			c[i] = s.charAt(i);
		}
		for(int i =0; i<s.length();i++) {
			if(num[(int)c[i]-97]==-1) {
				num[(int)c[i]-97] = i;
			}
		}
		for(int i =0;i<26;i++) {
			System.out.print(num[i]+" ");
		}
		
	}
		
}

	