public class X11 implements IDisplayManager{
    @Override
    public void installDisplayManager() {
        System.out.println("Installing: " + this.getClass().getSimpleName());
    }
}
