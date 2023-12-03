
import java.io.*;
import java.util.Scanner;

public class Day2p2 {

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

        sum += numGreen*numBlue*numRed;

    }

    System.out.println(sum);

    sc.close();
    }
    catch(IOException e) { 
        e.printStackTrace(); 
    }
}
}