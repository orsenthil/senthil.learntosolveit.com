public class Linux implements IKernel{
    /**
     * Load the kernel on top of the system image.
     */
    @Override
    public void loadKernel() {
        System.out.println("Loading: " + this.getClass().getSimpleName());

    }
}
