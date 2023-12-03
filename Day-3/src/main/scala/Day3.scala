import scala.collection.mutable.ArrayBuffer
import scala.io.Source

public static class main {
    // Setting Up file input and line-by-line reading
    val filePath = "Day3Cal.txt"
    val input = Source.fromFile(filePath)
    val scanner = input.getLines()

//main method
while (scanner.hasNext) {
    val input = scanner.next()
    println(input)
}

    input.close()
}