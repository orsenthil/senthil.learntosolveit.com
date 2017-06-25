public class OperatingSystem {
    IUnixFactory unixFactory;

    public OperatingSystem(IUnixFactory unixFactory) {
        this.unixFactory = unixFactory;
    }

    /**
     * installerClient uses only the interfaces declared by AbstractFactory (IUnixFactory) and AbstractProduct
     * (IBootLoader, IKernel, IShell, IDisplayManager, IWindowManager, IBaseApplications) classes.
     */
    public void installerClient() {


        IBootLoader bootLoader = unixFactory.installBootLoader();
        IKernel kernel = unixFactory.installKernel();
        IShell shell = unixFactory.installShell();
        IDisplayManager displayManager = unixFactory.installDisplayManager();
        IWindowManager windowManager = unixFactory.installWindowManager();
        IBaseApplications applications = unixFactory.installApps();

        bootLoader.bootUp();
        kernel.loadKernel();
        shell.loadShell();
        displayManager.installDisplayManager();
        windowManager.installWindowManager();
        applications.installApplications();

    }

    /**
     * client will not know the
     * products the type of bootloader, kernel, shell, display, window manager or applications.
     * That is encapsulated in factory used by the client.
     *
     */
    private static void factoryClient(IUnixFactory factory) {
        OperatingSystem operatingSystem = new OperatingSystem(factory);
        operatingSystem.installerClient();
    }

    public static void main(String[] args) {
        IUnixFactory factory;

        factory = new LinuxFactory();
        factoryClient(factory);

        factory = new BSDFactory();
        factoryClient(factory);

        factory = new UbuntuFactory();
        factoryClient(factory);
    }

}
