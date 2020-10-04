package bubbleSort;

/**
 * Class to complete the classic Bubble sort (with no swap watching)
 *
 * @author Chris Wolf
 * @version October 4, 2020
 */
public class BubbleSort {
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
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }

        return nums;
    }
}
