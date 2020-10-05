package bubbleSort;

/**
 * Class to complete the classic Bubble sort (with XOR swap watching)
 *
 * @author Akbarov Samandar
 * @version October 5, 2020
 */
public class BubbleSortWithoutTempValue {
    /**
     * Standard bubble sort algorithm on an array of numbers
     *
     * @param nums the array to be sorted
     * @return the original array AFTER it has been sorted
     */
    public static int[] bubbleSort(int[] nums) {
        if (nums.length < 2) {
            return nums;
        }
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] > nums[j]) {
                    nums[i] = nums[i]^nums[j];
                    nums[j] = nums[i]^nums[j];
                    nums[i] = nums[i]^nums[j];
                }
            }
        }

        return nums;
    }
}
