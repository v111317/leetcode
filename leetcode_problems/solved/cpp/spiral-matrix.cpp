#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int i = 0;
        int j = 0;
        int colTraveled = 1;
        int rowTraveled = 1;
        int rows = matrix.size();
        int cols = matrix[0].size();
        bool right = true;
        bool left = false;
        bool down = false;
        bool up = false;
        vector<int> result;
        int k = 0;
        int total = rows*cols;
        for(k=0;k<total;k++) {
            result.push_back(matrix[i][j]);
            if(right) {
                j++;
                colTraveled++;
                if(colTraveled>cols) {
                    rows--;
                    right = false;
                    down = true;
                    j--;
                    i++;
                    colTraveled = 1;
                    rowTraveled = 1;
                }
                continue;
            }
            if(down) {
                i++;
                rowTraveled++;
                if(rowTraveled>rows) {
                    cols--;
                    down = false;
                    left = true;
                    i--;
                    j--;
                    colTraveled = 1;
                    rowTraveled = 1;
                }
                continue;
            }
            if(left) {
                j--;
                colTraveled++;
                if(colTraveled>cols) {
                    rows--;
                    left = false;
                    up = true;
                    j++;
                    i--;
                    colTraveled = 1;
                    rowTraveled = 1;
                }
                continue;
            }
            if(up) {
                i--;
                rowTraveled++;
                if(rowTraveled>rows) {
                    cols--;
                    up = false;
                    right = true;
                    i++;
                    j++;
                    colTraveled = 1;
                    rowTraveled = 1;
                }
                continue;
            }
        }
        return result;
    }
};