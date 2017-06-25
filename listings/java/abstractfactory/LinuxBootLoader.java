public class LinuxBootLoader implements IBootLoader {
    @Override
    public void bootUp() {
        System.out.println("Booting: " + this.getClass().getSimpleName());
    }
}
