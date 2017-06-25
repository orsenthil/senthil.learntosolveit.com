public class Gnome implements IWindowManager {
    @Override
    public void installWindowManager() {
        System.out.println("Installing: " + this.getClass().getSimpleName());

    }
}
