import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] array_x = new int[N];
    int[] array_y = new int[N];

    int min_x, max_x, min_y, max_y;

    min_x = 10001;
    min_y = 10001;
    max_x = -10001;
    max_y = -10001;
    for (int i = 0; i < N; i++) {
      array_x[i] = sc.nextInt();
      if (array_x[i] > max_x)
        max_x = array_x[i];
      if (array_x[i] < min_x)
        min_x = array_x[i];
      array_y[i] = sc.nextInt();
      if (array_y[i] > max_y)
        max_y = array_y[i];
      if (array_y[i] < min_y)
        min_y = array_y[i];
    }
    System.out.println((max_x - min_x) * (max_y - min_y));
  }

}
