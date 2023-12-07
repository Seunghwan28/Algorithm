class Solution {
    public int solution(String s) {
        int temp=0;
		int answer =0;
		char[] c = new char[s.length()];
		for(int i =0;i<s.length();i++) {
			c[i]= s.charAt(i);
		}
		char x = c[0];
		for(int i =0;i<s.length();i++) {
			if(x==c[i]) {
					temp++;
				}
				else {
					temp--;
				}
			if((temp==0)&&(i<s.length()-1)) {
				answer++;
				x = c[i+1];
			}
			
		}
        answer++;
        return answer;
    }
}