public class UbuntuFactory extends LinuxFactory {
    @Override
    public IDisplayManager installDisplayManager() {
        return new X11();
    }

    @Override
    public IBaseApplications installApps() {
        return new ProprietaryApps();
    }
}
