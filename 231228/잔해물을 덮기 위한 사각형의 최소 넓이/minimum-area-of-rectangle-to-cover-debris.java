import java.util.Scanner;

public class Main {
    static final int OFFSET = 1000;
    static final int MAX_R = 2000;

    static int n = 2;
    static int[] x1 = new int[n];
    static int[] y1 = new int[n];
    static int[] x2 = new int[n];
    static int[] y2 = new int[n];

    static int[][] checked = new int[MAX_R + 1][MAX_R + 1];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력
        for (int i = 0; i < n; i++) {
            x1[i] = sc.nextInt();
            y1[i] = sc.nextInt();
            x2[i] = sc.nextInt();
            y2[i] = sc.nextInt();

            // OFFSET 적용
            x1[i] += OFFSET;
            y1[i] += OFFSET;
            x2[i] += OFFSET;
            y2[i] += OFFSET;
        }

        // 사각형 색칠
        for (int i = 0; i < n; i++) {
            for (int j = x1[i]; j < x2[i]; j++) {
                for (int k = y1[i]; k < y2[i]; k++) {
                    checked[j][k] = i + 1;
                }
            }
        }

        // 최소 직사각형 넓이 구하기
        int minX = MAX_R;
        int minY = MAX_R;
        int maxX = 0;
        int maxY = 0;

        for (int i = 0; i <= MAX_R; i++) {
            for (int j = 0; j <= MAX_R; j++) {
                if (checked[i][j] == 1) {
                    if (i < minX) {
                        minX = i;
                    }
                    if (i > maxX) {
                        maxX = i;
                    }
                    if (j < minY) {
                        minY = j;
                    }
                    if (j > maxY) {
                        maxY = j;
                    }
                }
            }
        }

        // 최소 직사각형 칠하기
        int area = 0;
        for (int i = minX; i <= maxX; i++) {
            for (int j = minY; j <= maxY ; j++) {
                checked[i][j] = 1;
                area++;
            }
        }

        System.out.println(area);
    }
}