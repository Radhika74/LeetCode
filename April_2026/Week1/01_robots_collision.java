class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] index = new Integer[n];
        for (int i=0; i<n; ++i){
            index[i]=i;
        }
        Arrays.sort(index, (a,b) -> positions[a]-positions[b]);
        Stack<Integer> stack = new Stack<>();
        for(int i: index){
            if (directions.charAt(i)=='R'){
                stack.push(i);
                continue;
        }
        
        while (!stack.isEmpty() && healths[i]>i){
            if (healths[stack.peek()] < healths[i]){
                healths[stack.pop()]=0;
                healths[i]--;
            }else if (healths[stack.peek()] > healths[i]){
                healths[stack.peek()]--;
                healths[i]=0;
            }else {
                healths[stack.pop()]=0;
                healths[i]=0;
            }
        } 
    }
        List<Integer> result = new ArrayList<>();
        for (int h: healths){
            if(h>0){
              result.add(h);
            }
       }
        return result;
    }
}