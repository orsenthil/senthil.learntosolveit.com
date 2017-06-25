public class BSDFactory implements IUnixFactory {
    @Override
    public IBootLoader installBootLoader() {
        return new BSDBootLoader();
    }

    @Override
    public IKernel installKernel() {
        return new BSDKernel();
    }

    @Override
    public IShell installShell() {
        return new CShell();
    }

    @Override
    public IDisplayManager installDisplayManager() {
        return new X11();
    }

    @Override
    public IWindowManager installWindowManager() {
        return new KDE();
    }

    @Override
    public IBaseApplications installApps() {
        return new SystemVUnix();
    }
}
