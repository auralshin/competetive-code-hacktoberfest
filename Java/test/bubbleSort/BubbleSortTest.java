package bubbleSort;

import org.junit.Test;
import java.util.Arrays;
import static org.junit.Assert.assertTrue;

import static bubbleSort.BubbleSort.bubbleSort;

/**
 * Unit testing for bubbleSort.BubbleSort.java
 *
 * @author Chris Wolf
 * @version October 4, 2020
 */
public class BubbleSortTest {
    @Test
    public void testEmptyArray() {
        int[] actual = {};
        int[] expected = {};
        assertTrue(Arrays.equals(bubbleSort(actual), expected));
    }

    @Test
    public void testArraySizeOne() {
        int[] actual = {1};
        int[] expected = {1};
        assertTrue(Arrays.equals(bubbleSort(actual), expected));
    }

    @Test
    public void testArraySizeFiveAlreadyInOrder() {
        int[] actual = {1, 2, 3, 4, 5};
        int[] expected = {1, 2, 3, 4, 5};
        assertTrue(Arrays.equals(bubbleSort(actual), expected));
    }

    @Test
    public void testArraySizeFiveReverseOrder() {
        int[] actual = {5, 4, 3, 2, 1};
        int[] expected = {1, 2, 3, 4, 5};
        assertTrue(Arrays.equals(bubbleSort(actual), expected));
    }

    @Test
    public void testArraySizeFiveNoOrder() {
        int[] actual = {1, 3, 5, 2, 4};
        int[] expected = {1, 2, 3, 4, 5};
        assertTrue(Arrays.equals(bubbleSort(actual), expected));
    }
}
