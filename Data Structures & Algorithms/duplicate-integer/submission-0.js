class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let unique = []

        for(let i=0; i < nums.length; i++) {
            if(i==0) {
                unique[0] = nums[0]
            }
            for(let j=0; j < unique.length; j++) {
                if(nums[i+1] == unique[j]) {
                    return true
                } else {
                    unique[i] = nums[i]
                }
            }
        }
        return false
    }
}
