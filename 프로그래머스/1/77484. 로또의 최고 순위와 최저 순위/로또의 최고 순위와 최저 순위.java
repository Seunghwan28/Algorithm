class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int zero =0;
        int same=0;
        for(int i =0;i<6;i++) {
            for(int j=0;j<6;j++) {
                if(lottos[i]==0) {
                    zero++;
                }
                else {
                    if(lottos[i]==win_nums[j]) {
                        same++;
                    }
                }
            }
        }
        zero=zero/6;
        answer[0]=7-(same+zero);
        if(answer[0]==7) {answer[0]=6;}
        answer[1]=7-same;
        if(answer[1]==7) {answer[1]=6;}
        return answer;
    }
}