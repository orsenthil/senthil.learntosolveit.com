public class BSDBootLoader implements IBootLoader{
    /**
     * Boot up the System Image.
     */
    @Override
    public void bootUp() {
        System.out.println("Booting: " + this.getClass().getSimpleName());

    }
}
