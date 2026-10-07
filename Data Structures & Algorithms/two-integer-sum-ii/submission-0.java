class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int front = 0;
        int back = numbers.length - 1;

        int[] res = null;
        while (front < back) {
            int sum = numbers[front] + numbers[back];
            if (sum < target) {
                front += 1;
            } else if (sum > target) {
                back -= 1;
            } else {
                res = new int[]{front + 1, back + 1};
                break;
            }
        }

        return res;
    }
}
