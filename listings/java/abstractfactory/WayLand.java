public class WayLand implements IDisplayManager{

    @Override
    public void installDisplayManager() {
        System.out.println("Installing: " + this.getClass().getSimpleName());
    }

}
