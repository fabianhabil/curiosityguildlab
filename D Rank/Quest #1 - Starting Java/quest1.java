import java.util.Scanner;

class quest1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Masukkan nama anda");
        String nama = in.nextLine();
        in.close();
        System.out.println("Welcome Master, " + nama);
    }
}