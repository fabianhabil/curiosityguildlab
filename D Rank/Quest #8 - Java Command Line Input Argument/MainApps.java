
class MainApps {
    public static void main(String[] args) {
        boolean isError = false;
        int inputInteger[] = new int[2];
        if (args.length == 2) {
            for (int i = 0; i < args.length; i++) {
                try {
                    inputInteger[i] = Integer.parseInt((args[i]));
                } catch (NumberFormatException e) {
                    System.out.println(args[i] + " is not a number!");
                    isError = true;
                }
            }
            if (isError) {
                System.out.println("Wrong Argument, cant perform math operations.");
                System.out.println("Correct argument: java MainApps <int> <int>");
            } else {
                int addition = inputInteger[0] + inputInteger[1];
                int substraction = inputInteger[0] - inputInteger[1];
                int multiplication = inputInteger[0] * inputInteger[1];
                int modulo = inputInteger[0] % inputInteger[1];
                float division = inputInteger[0] / inputInteger[1];
                System.out.println("Addition " + inputInteger[0] + " + " + inputInteger[1] + " = " + addition);
                System.out.println("Substraction " + inputInteger[0] + " - " + inputInteger[1] + " = " + substraction);
                System.out.println("Multiplication " + inputInteger[0] + " x " + inputInteger[1] + " = " + multiplication);
                System.out.println("Modulo " + inputInteger[0] + " % " + inputInteger[1] + " = " + modulo);
                System.out.println("Division " + inputInteger[0] + " : " + inputInteger[1] + " = " + division);
            }
        } else {
            System.out.println("Wrong Argument!");
            System.out.println("Correct argument: java MainApps <int> <int>");
        }
    }
}