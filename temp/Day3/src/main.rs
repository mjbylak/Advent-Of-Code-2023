use std::io::{BufRead, BufReader};
use std::fs::File;

pub fn main() {

    let debug = false;

    let f = BufReader::new(File::open("Day3Cal.txt").expect("open failed"));

    let mut schematic = Vec::<Vec<char>>::new();

    for line in f.lines() {
        if debug { println!(); }
        let mut temp = Vec::<char>::new();
        for c in line.expect("lines failed").chars() {
            temp.push(c);
            if debug { print!("{} ", c); }
        }
        schematic.push(temp);
    }


    // Iterate through all elements
    for row in &mut schematic {
        for i in row.iter_mut() {
            if *i == '.' { 
                *i = ' '; 
            }
            print!("{} ", i);
        }
        println!();
    }

    //declare function variables
    let mut sum = 0;
    let mut temp = 0;

    //check if i is digit, then read next i until not digit
    //check all surrounding to see if any are != ' '
    for x in &mut schematic.len() {
        for y in schematic[x].len(){
            if schematic[x][y].is_digit(10) {
                
                //ensure doesn't go out of bounds 
                //ensure stops read on nondigit
                //log all digit locations
                //check all surrounding values for != ' '
                temp.push(schematic[x][y]);

            }
        }
        println!();
    }
    
    
}