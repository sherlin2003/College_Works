import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

class Card implements Comparable <Card> {
    char symbol;
    int number;

    public Card() {
    }

    public Card(char symbol, int number) {
        this.symbol = symbol;
        this.number = number;
    }

    @Override
    public String toString() {
        return "Card{" +
                "symbol=" + symbol +
                ", number=" + number +
                '}';
    }

    @Override
    public int compareTo(Card o) {
        return Character.compare(symbol, o.symbol);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in  = new Scanner(System.in);
        Set<Card> cards = new TreeSet<Card>();

        while(cards.size()<4){
            System.out.println("Enter a card");
            char symbol = in.next().charAt(0);
            int number = in.nextInt();
            cards.add(new Card(symbol, number));
        }

        for(Card c: cards){
            System.out.println(c.toString());
        }
    }
}
