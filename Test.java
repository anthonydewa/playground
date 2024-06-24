import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

/**
 * test
 */
public class Test {
    // searching 
    public static int linear_search(List<Integer> n, int key) {
        int res = -1;
        for (int i = 0; i < n.size(); i++) {
           if (n.get(i) == key) {
            res = key;
            break;
           }
        }

        return res;
    }

    // sorting
    public static List<Integer> bubble_sort(List<Integer> arr) {
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i; j < arr.size(); j++) {
                Integer prev = arr.get(i);
                Integer curr = arr.get(j);

                if (curr < prev) {
                    arr.set(i, curr);
                    arr.set(j, prev);
                }
            }
        }

        return arr;
    }

    public static List<Integer> selection_sort(List<Integer> arr) {
        for (int i = 0; i < arr.size(); i++) {
            Integer smallest = arr.get(i);
            int smallest_index = i;
            for (int j = i + 1; j < arr.size(); j++) {
                Integer traverse = arr.get(j);

                if (traverse < smallest) {
                    smallest = traverse;
                    smallest_index = j;
                }
            }
            
            // swap
            if (i != smallest_index) {
                Integer temp = arr.get(i);
                arr.set(i, smallest);
                arr.set(smallest_index, temp);
            }
        }

        return arr;
    }
    
    public static List<Integer> merge_sort(List<Integer> arr, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;

            merge_sort(arr, l, m);
            merge_sort(arr, m + 1, r);

            merge_sort_aux_merge(arr, l, m, r);
        }

        return arr;
    }

    public static List<Integer> merge_sort_aux_merge(List<Integer> arr, int l, int m, int r) {
        int size_l = m - l + 1;
        int size_r = r - m;

        int[] L = new int[size_l];
        int[] R = new int[size_r];

        for (int i = 0; i < L.length; i++) {
            L[i] = arr.get(l + i);
        }
        for (int i = 0; i < R.length; i++) {
            R[i] = arr.get(m + 1 + i);
        }

        int i = 0, j = 0;

        int k = l;
        while (i < size_l && j < size_r) {
            if (L[i] <= R[j]) {
                arr.set(k, L[i]);
                i++;
            }
            else {
                arr.set(k, R[i]);
                j++;
            }
            k++;
        }

        while (i < size_l) {
            arr.set(k, L[i]);
            i++;
            k++;
        }

        while (j < size_r) {
            arr.set(k, R[j]);
            j++;
            k++;
        }

        

        return arr;
    }

    public static int findShortestSubstring(String s) {
        // get duplicated character
        HashMap<Character, Integer> hash_table = new HashMap<Character, Integer>();
        String dup_pattern = "";

        for (int i = 0; i < s.length(); i++) {
            Character curr_char = s.charAt(i);

            Integer table_value = hash_table.get(curr_char);
            if (table_value == null) {
                hash_table.put(curr_char, 1);
            } else if (table_value > 0) {
                table_value += 1;
                hash_table.put(curr_char, table_value);
                
                if (table_value >= 2) {
                    dup_pattern += curr_char;
                }
            } 
        }

        if (dup_pattern.length() == 0) {
            return 0;
        }
        int shortest_sub = (int) Math.pow(10, 6);
        String sss = "";
        
        for (int i = 0; i < s.length(); i++) {
            for (int j = i; j < s.length(); j++) {
                String subs = s.substring(i, j + 1);
                
                if (substringContainDupPattern(subs, dup_pattern)) {
                    int current_length = subs.length();

                    if (current_length < shortest_sub) {
                        shortest_sub = current_length;
                        sss = subs;
                    }
                }
            }
        }
        
        return  shortest_sub;
    }
    
    public static boolean substringContainDupPattern(String s, String dup_pattern) {
        int[] count_char = new int[256];
        
        for (int i = 0; i < dup_pattern.length(); i++) {
            char curr = dup_pattern.charAt(i);
            count_char[curr] = count_char[curr] + 1;
        }
        
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (count_char[curr] > 0) {
                count_char[curr] = count_char[curr] - 1;
            }
        }
        
        for (int i = 0; i < 256; i++) {
            if (count_char[i] > 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        // Scanner scanner = new Scanner(System.in);
        // int name = scanner.nextInt();

        // List<Integer> arr = Arrays.asList(3, -1, 100, 23);

        // // List<Integer> dsada = bubble_sort(arr);
        // // List<Integer> dsada = selection_sort(arr);
        // List<Integer> dsada = merge_sort(arr, 0, arr.size() - 1);
        // System.out.println(dsada);

        // int[] sd = new int[] {1, 2, 3, 4, 5};

        // scanner.close();
        int y = findShortestSubstring("bbbb");
        System.out.println(y);

        int[][] a = new int
    }
}