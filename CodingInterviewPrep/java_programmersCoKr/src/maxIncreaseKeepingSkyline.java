import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

// https://leetcode.com/submissions/detail/170889345/
// 2018/08/21 18:30~20:40
//



public class maxIncreaseKeepingSkyline {

    public static int maxIncreaseKeepingSkyline_mine(int[][] grid) {
        int increasibleHeightSum = 0;
        int[] horizontalView = new int[grid.length];
        int[] verticalView = new int[grid[1].length];
        int[][] newGrid = new int[grid.length][grid.length];

        horizontalView = findHorizontalMaxView(grid);
        verticalView = findVerticalMaxView(grid);
        newGrid = buildNewGrid(grid, horizontalView, verticalView);

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                increasibleHeightSum += newGrid[i][j] - grid[i][j];
            }
        }
//        System.out.println("=increasibleHeightSum=");
//        System.out.print(increasibleHeightSum);
        return increasibleHeightSum;
    }

    public static void printer(int[][] grid){
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }

    // find the left/right maxView
    public static int[] findHorizontalMaxView(int[][] grid){
        int[] result = new int[grid.length];
        for (int i = 0; i < grid.length; i++) {
            int temp = grid[i][0];
//            System.out.print(temp + " ");
            for (int j = 0; j < grid.length; j++) {
                if (temp < grid[i][j]){
                    temp = grid[i][j];
                }
            }
            result[i] = temp; // [8, 7, 9, 3]
        }

//        System.out.print("horizontalMaxView = ");
//        for (int i = 0; i < result.length; i++) {
//            System.out.print(result[i] + " ");
//        }
//        System.out.println();
        return result;
    }

    // find the top/bottom maxview
    public static int[] findVerticalMaxView(int[][] grid){
        int[] result = new int[grid[1].length];
        for (int j = 0; j < grid.length; j++) {
            int temp = grid[0][j];
//            System.out.print(temp + " ");
            for (int i = 0; i < grid.length; i++) {
                if (temp < grid[i][j]){
                    temp = grid[i][j];
                }
            }
            result[j] = temp; // [9, 4, 8, 7]
        }

//        System.out.print("verticalMaxView = ");
//        for (int i = 0; i < result.length; i++) {
//            System.out.print(result[i] + " ");
//        }
//        System.out.println();

        return result;
    }

    // build newGrid
    public static int[][] buildNewGrid(int[][] grid, int[] horMaxView, int[] verMaxView){
        int [][] newGrid = new int[grid.length][grid.length];
        for (int i = 0; i < horMaxView.length ; i++) {
            for (int j = 0; j < verMaxView.length; j++) {
                if (horMaxView[i] <= verMaxView[j]){
                    newGrid[i][j] = horMaxView[i];
                }
                else {
                    newGrid[i][j] = verMaxView[j];
                }
            }
        }

//        System.out.println("=newGrid=");
//        printer(newGrid);

        return newGrid;
    }



    // best solution
    public static int maxIncreaseKeepingSkyline_best1(int[][] grid) {
        int[] line1 = new int[grid.length];
        int[] line2 = new int[grid[0].length];

        int sum = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] > line1[i]) line1[i] = grid[i][j];
                if(grid[i][j] > line2[j]) line2[j] = grid[i][j];
                sum += grid[i][j];
            }
        }


        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                sum -= Math.min(line1[i], line2[j]);
            }
        }

        return -sum;
    }


    // 2nd best solution
    public static int maxIncreaseKeepingSkyline_best2(int[][] grid) {
        //首先求每一行的最大值
        int[]row=new int[grid.length];
        for(int i=0;i<grid.length;i++){
            int tmp=0;
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]>tmp){
                    tmp=grid[i][j];
                }
            }
            row[i]=tmp;
        }
        int[]col=new int[grid[0].length];
        for(int i=0;i<grid[0].length;i++){
            int tmp=0;
            for(int j=0;j<grid.length;j++){
                if(grid[j][i]>tmp)
                    tmp=grid[j][i];
            }
            col[i]=tmp;
        }
        //每一行 每一列的最大值都统计出来了
        int res=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                res+=Math.min(row[i],col[j])-grid[i][j];
            }
        }
        return res;
    }

    // 3rd best solution
    public static int maxIncreaseKeepingSkyline_best3(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;

        int[] row = new int[grid.length];
        int[] col = new int[grid[0].length];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                row[i] = Math.max(row[i], grid[i][j]);
                col[j] = Math.max(col[j], grid[i][j]);
            }
        }

        int result = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result += Math.min(row[i], col[j]) - grid[i][j];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[][] oldGrid = {{3,0,8,4},{2,4,5,7},{9,2,6,3},{0,3,1,0}};
//        printer(oldGrid);
//        System.out.println("=MaxViews=");
        System.out.print(maxIncreaseKeepingSkyline_mine(oldGrid));
        System.out.println();
        System.out.print(maxIncreaseKeepingSkyline_best1(oldGrid));
        System.out.println();
        System.out.print(maxIncreaseKeepingSkyline_best2(oldGrid));
        System.out.println();
        System.out.print(maxIncreaseKeepingSkyline_best3(oldGrid));
    }
}
