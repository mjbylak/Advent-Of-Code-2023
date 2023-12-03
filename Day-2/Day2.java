import java.io.*;
import java.util.Scanner;

public class Day2 {

// public int pullNumber(String input, int i) {
//     int output = 0;
//     separated input.split(" ");

    

//     return output;
// }
public static void main (String[] args) { try {
    FileInputStream fis = new FileInputStream("Day2.txt");
    Scanner sc = new Scanner(fis);

    String colors [] = {"green", "blue", "red"};
    
    int currGame = 0;
    int sum = 0;
    
    while(sc.hasNextLine()) {
        currGame++;
        String input = sc.nextLine();
        int numGreen = 0, numRed = 0, numBlue = 0;

        input = input.replaceAll("[;,]", " ");
        String [] separatedWords = input.split(" ");
        for(int i = 0; i < separatedWords.length;i++){
            if(separatedWords[i].equals(colors[0])) {
                if (Integer.parseInt(separatedWords[i-1]) > numGreen) numGreen = Integer.parseInt(separatedWords[i-1]);
            }
            if(separatedWords[i].equals(colors[1])) {
                if (Integer.parseInt(separatedWords[i-1]) > numBlue) numBlue = Integer.parseInt(separatedWords[i-1]);
            }
            if(separatedWords[i].equals(colors[2])) {
                if (Integer.parseInt(separatedWords[i-1]) > numRed) numRed = Integer.parseInt(separatedWords[i-1]);
            }
        }
        if(numGreen > 13 || numBlue > 14 || numRed > 12){
            continue;
        }
        else sum += currGame;

        // int i = 0;
        // while (i >= 0) {
        //     int gI = input.indexOf(colors[0], i);
        //     int bI = input.indexOf(colors[1], i);
        //     int rI = input.indexOf(colors[2], i);
        // }
        // int greenIndex = input.indexOf(colors[0]);
        // int blueIndex = input.indexOf(colors[1]);
        // int redIndex = input.indexOf(colors[2]); 

    }

    System.out.println(sum);

    sc.close();
    }
    catch(IOException e) { 
        e.printStackTrace(); 
        }
}
}