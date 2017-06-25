public class GNUApplications implements IBaseApplications{
    @Override
    public void installApplications() {
        System.out.println("Installing: " + this.getClass().getSimpleName());
    }
}
