import java.util.Scanner;
import java.util.Stack;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); 

        for (int test_case = 1; test_case <= T; test_case++) {
            int N = sc.nextInt();
            char[][] mineMap = new char[N][N];
            boolean[][] visited = new boolean[N][N];
            int result = 0;

            int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
            int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};

            for (int i = 0; i < N; i++) {
                String row = sc.next();
                mineMap[i] = row.toCharArray();
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (mineMap[i][j] == '.') {
                        int mineCount = 0;
                        for (int k = 0; k < 8; k++) {
                            int nx = i + dx[k];
                            int ny = j + dy[k];
                            if (nx >= 0 && nx < N && ny >= 0 && ny < N && mineMap[nx][ny] == '*') {
                                mineCount++;
                            }
                        }
                        mineMap[i][j] = (char) (mineCount + '0');
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (mineMap[i][j] == '0' && !visited[i][j]) {
                        dfs(mineMap, visited, i, j, N, dx, dy);
                        result++;
                    }
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (mineMap[i][j] != '*' && !visited[i][j]) {
                        result++;
                    }
                }
            }

            System.out.println("#" + test_case + " " + result);
        }
    }

    private static void dfs(char[][] mineMap, boolean[][] visited, int x, int y, int N, int[] dx, int[] dy) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{x, y});

        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int cx = current[0];
            int cy = current[1];

            if (visited[cx][cy]) continue;
            visited[cx][cy] = true;

            if (mineMap[cx][cy] == '0') {
                for (int k = 0; k < 8; k++) {
                    int nx = cx + dx[k];
                    int ny = cy + dy[k];
                    if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && mineMap[nx][ny] != '*') {
                        stack.push(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}
