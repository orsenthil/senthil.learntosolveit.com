public class Bash implements IShell {

    @Override
    public void loadShell() {
        System.out.println("Loading: " + this.getClass().getSimpleName());

    }
}
