
// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.List;
import java.util.ArrayList;
import java.util.Random;

class Main {
    /**
     * print integer list
     */
    public static void printList(List<Integer> list) {
        for (int item : list) {
            System.out.print(item + " ");
        }
        System.out.println();
    }

    /**
     * generate random integer List
     */
    public static List<Integer> generateRandomList(int size, int min, int max) {
        List<Integer> list = new ArrayList<>();
        Random rand = new Random();

        for (int i = 0; i < size; i++) {
            int randomNum = rand.nextInt(max - min + 1) + min; // generate between min y max (including max)
            list.add(randomNum);
        }

        return list;
    }

    /**
     * return sorted list
     */
    public static List<Integer> orderList(List<Integer> list, SortType sortType) {
        List<Integer> orderedList = new ArrayList<Integer>(list);
        boolean condition = true;

        while (condition) {
            boolean isOrdered = true;
            for (int i = 0; i < orderedList.size() - 1; ++i) {
                int posA = i;
                int posB = i + 1;
                int a = orderedList.get(posA);
                int b = orderedList.get(posB);

                switch (sortType) {
                    case DESCEND:
                        if (b > a) {
                            orderedList.set(posA, b);
                            orderedList.set(posB, a);
                            isOrdered = false;
                        }
                        break;

                    default:   // Default order: Ascend
                        if (b < a) {
                            orderedList.set(posA, b);
                            orderedList.set(posB, a);
                            isOrdered = false;
                        }
                        break;
                }

            }

            if (isOrdered) {
                condition = false;
            }

        }

        return orderedList;
    }

    public static void main(String[] args) {
        List<Integer> disorderedList = generateRandomList(100, 0, 100);

        System.out.println("List To order");
        printList(disorderedList);

        List<Integer> orderedListAsc = orderList(disorderedList, SortType.ASCEND);
        System.out.println("Ascended Order list");
        printList(orderedListAsc);

        List<Integer> orderedListDesc = orderList(disorderedList, SortType.DESCEND);
        System.out.println("Descended Order list");
        printList(orderedListDesc);

    }
}