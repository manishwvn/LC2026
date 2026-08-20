// Last updated: 8/20/2026, 2:20:50 AM
function twoSum(nums: number[], target: number): number[] {
    
    let hm = new Map();
    let result = [];
    
    for(let i=0; i <= nums.length; i++){
        if(hm.has(target - nums[i])){
            return [hm.get(target - nums[i]), i]
        }
        
        else{
            hm.set(nums[i], i)
        }
            
    };

};